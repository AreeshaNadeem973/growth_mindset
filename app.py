import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt

# App Title
st.set_page_config(page_title="🏋️ Fitness Hub", layout="wide")
st.title("🏋️ Fitness Hub - Your Personal Fitness Tracker")

# Sidebar Navigation
st.sidebar.header("📌 Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Dashboard", "💪 Workout Tracker", "🥗 Meal Planner",
    "📊 Health Analytics", "🎯 Goal Setter", "🏆 Achievements", "🌍 Community"
])

# Initialize session state
if 'workouts' not in st.session_state:
    st.session_state.workouts = []
if 'meals' not in st.session_state:
    st.session_state.meals = []
if 'goals' not in st.session_state:
    st.session_state.goals = []

# Dashboard Page
if page == "🏠 Dashboard":
    st.header("Welcome to Fitness Hub! 🏋️")
    st.markdown("""
    - **Track Your Workouts** 💪
    - **Plan Your Meals** 🥗
    - **Monitor Health Analytics** 📊
    - **Set & Achieve Goals** 🎯
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Workouts Logged", len(st.session_state.workouts))
    col2.metric("Meals Tracked", len(st.session_state.meals))
    col3.metric("Active Goals", len(st.session_state.goals))

# Workout Tracker Page
elif page == "💪 Workout Tracker":
    st.header("💪 Log Your Workouts")
    with st.form("workout_form"):
        exercise = st.text_input("Exercise Name:")
        duration = st.number_input("Duration (mins):", min_value=5, max_value=180, step=5)
        intensity = st.slider("Intensity (1-10):", 1, 10, 5)
        submit = st.form_submit_button("Log Workout")
        if submit:
            st.session_state.workouts.append({"exercise": exercise, "duration": duration, "intensity": intensity, "date": datetime.now()})
            st.success("Workout logged!")
    
    if st.session_state.workouts:
        st.subheader("Workout Summary")
        fig, ax = plt.subplots()
        durations = [w['duration'] for w in st.session_state.workouts]
        labels = [w['exercise'] for w in st.session_state.workouts]
        ax.bar(labels, durations, color=['red', 'blue', 'green', 'yellow', 'pink'])
        ax.set_ylabel('Duration (mins)')
        ax.set_title('Workouts')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Meal Planner Page
elif page == "🥗 Meal Planner":
    st.header("🥗 Plan Your Meals")
    with st.form("meal_form"):
        meal = st.text_input("Meal Name:")
        calories = st.number_input("Calories:", min_value=50, max_value=2000, step=50)
        submit = st.form_submit_button("Log Meal")
        if submit:
            st.session_state.meals.append({"meal": meal, "calories": calories, "date": datetime.now()})
            st.success("Meal logged!")
    
    if st.session_state.meals:
        st.subheader("Meal Summary")
        fig, ax = plt.subplots()
        calories = [m['calories'] for m in st.session_state.meals]
        labels = [m['meal'] for m in st.session_state.meals]
        ax.bar(labels, calories, color=['orange', 'purple', 'cyan', 'lime', 'magenta'])
        ax.set_ylabel('Calories')
        ax.set_title('Meals')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Health Analytics Page
elif page == "📊 Health Analytics":
    st.header("📊 Track Your Health")
    weight = st.number_input("Weight (kg):", min_value=30.0, max_value=200.0, step=0.1)
    height = st.number_input("Height (m):", min_value=1.0, max_value=2.5, step=0.01)
    if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

# Goal Setter Page
elif page == "🎯 Goal Setter":
    st.header("🎯 Set Your Fitness Goals")
    with st.form("goal_form"):
        goal_name = st.text_input("Goal:")
        target_date = st.date_input("Target Date:")
        submit = st.form_submit_button("Set Goal")
        if submit:
            st.session_state.goals.append({"goal": goal_name, "target_date": target_date})
            st.success("Goal set!")
    
    if st.session_state.goals:
        st.subheader("Your Goals")
        for g in st.session_state.goals:
            st.write(f"🎯 {g['goal']} (Target: {g['target_date']})")

# Achievements Page
elif page == "🏆 Achievements":
    st.header("🏆 Your Achievements")
    workout_count = len(st.session_state.workouts)
    meal_count = len(st.session_state.meals)
    goal_count = len(st.session_state.goals)
    achievements = [
        ("Fitness Starter", "Log 5 workouts", workout_count >= 5),
        ("Meal Tracker", "Log 10 meals", meal_count >= 10),
        ("Goal Achiever", "Set 3 goals", goal_count >= 3)
    ]
    for ach in achievements:
        st.write(f"{'🏅' if ach[2] else '🔒'} {ach[0]} - {ach[1]}")

# Community Page
elif page == "🌍 Community":
    st.header("🌍 Connect with the Fitness Community")
    st.text_area("Share your fitness journey:")
    st.button("Post")

# Footer
st.markdown("---")
st.markdown("🏋️ *Built with ❤️ using Streamlit. Stay Fit, Stay Strong!*")
