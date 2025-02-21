import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time

# App Title
st.title("🏋️ Fitness Hub: Your Ultimate Health Companion")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Home", "📊 Workout Tracker", "🍎 Meal Planner", "📈 Health Analytics",
    "🎯 Goal Setter", "🏆 Achievements", "🌍 Community"
])

# Initialize session state
if 'workouts' not in st.session_state:
    st.session_state.workouts = []
if 'meals' not in st.session_state:
    st.session_state.meals = []
if 'goals' not in st.session_state:
    st.session_state.goals = []

# Home Page
if page == "🏠 Home":
    st.header("Welcome to Fitness Hub! 🏋️")
    st.markdown("""
    ### Your Personalized Health & Fitness Assistant
    ✅ **Track Workouts**: Log and analyze your exercises  
    ✅ **Plan Meals**: Maintain a balanced diet with meal tracking  
    ✅ **Monitor Health**: Check your BMI and health stats  
    ✅ **Set Goals**: Stay motivated with goal tracking  
    ✅ **Join Community**: Engage with fellow fitness enthusiasts  
    """)
    
    # Quick Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Workouts", len(st.session_state.workouts))
    with col2:
        st.metric("Meals Logged", len(st.session_state.meals))
    with col3:
        st.metric("Active Goals", len(st.session_state.goals))

# Workout Tracker
elif page == "📊 Workout Tracker":
    st.header("📊 Track Your Workouts")
    
    # Input form
    with st.form("workout_form"):
        workout_type = st.selectbox("Workout Type:", ["Cardio", "Strength", "Yoga", "HIIT", "Other"])
        duration = st.number_input("Duration (minutes):", min_value=10, max_value=180, step=5)
        notes = st.text_area("Workout Notes:")
        if st.form_submit_button("Log Workout"):
            st.session_state.workouts.append({
                "date": datetime.now(),
                "type": workout_type,
                "duration": duration,
                "notes": notes
            })
            st.success("Workout logged successfully!")
            st.balloons()

# Meal Planner
elif page == "🍎 Meal Planner":
    st.header("🍎 Plan Your Meals")
    
    with st.form("meal_form"):
        meal_type = st.selectbox("Meal Type:", ["Breakfast", "Lunch", "Dinner", "Snack"])
        meal_details = st.text_area("Meal Details:")
        if st.form_submit_button("Log Meal"):
            st.session_state.meals.append({
                "date": datetime.now(),
                "type": meal_type,
                "details": meal_details
            })
            st.success("Meal logged successfully!")
            st.balloons()

# Health Analytics
elif page == "📈 Health Analytics":
    st.header("📈 Health Analytics")
    
    weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=200)
    height = st.number_input("Enter your height (cm):", min_value=100, max_value=250)
    
    if st.button("Calculate BMI"):
        bmi = weight / ((height / 100) ** 2)
        st.write(f"Your BMI: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")

# Goal Setter
elif page == "🎯 Goal Setter":
    st.header("🎯 Set and Track Goals")
    
    with st.form("goal_form"):
        goal_title = st.text_input("Goal:")
        target_date = st.date_input("Target Date:")
        if st.form_submit_button("Set Goal"):
            st.session_state.goals.append({
                "title": goal_title,
                "target_date": target_date,
                "completed": False
            })
            st.success("Goal set successfully!")
            st.balloons()

# Achievements
elif page == "🏆 Achievements":
    st.header("🏆 Your Achievements")
    
    total_workouts = len(st.session_state.workouts)
    completed_goals = len([g for g in st.session_state.goals if g["completed"]])
    
    achievements = [
        {"name": "Fitness Enthusiast", "desc": "Complete 10 workouts", "achieved": total_workouts >= 10},
        {"name": "Goal Crusher", "desc": "Achieve 3 goals", "achieved": completed_goals >= 3}
    ]
    
    for ach in achievements:
        st.write(f"**{ach['name']}** - {ach['desc']}")
        st.markdown("✅" if ach["achieved"] else "🔒")

# Community
elif page == "🌍 Community":
    st.header("🌍 Join the Fitness Community")
    st.write("Share your progress, tips, and motivation with others!")
    post = st.text_area("Share your update:")
    if st.button("Post"):
        st.success("Post shared with the community!")
        st.balloons()

# Footer
st.markdown("---")
st.markdown("🏋️ *Developed with ❤️ using Streamlit. Stay fit, stay healthy!*")
