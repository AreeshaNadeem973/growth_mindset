import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="Success & Growth Hub", page_icon="🌟")
st.title("🌟 Success & Growth Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Explore Topics")
page = st.sidebar.radio("Navigate to:", [
    "🏡 Home", "🔄 Daily Habits", "🌱 Growth Mindset", "🧘 Mental Wellness",
    "🎯 Goal Mastery", "💡 Productivity Hacks", "📚 Learning & Skills", "💰 Financial Growth"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Success & Growth Hub! 🚀")
    st.markdown("""
    ### Why Focus on Personal Growth?
    ✅ **Daily Improvement**: Small changes lead to big success.  
    ✅ **Mental Clarity**: A strong mind leads to a strong life.  
    ✅ **Productivity Boost**: Work smarter, not harder.  
    ✅ **Financial Wisdom**: Secure your future with smart decisions.  
    """)
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    st.success("Success is built daily! Keep pushing forward! 🚀")
    
    # Motivational Quote
    quotes = [
        "Your only limit is your mind.",
        "Success is the sum of small efforts, repeated daily.",
        "Believe in yourself and you are halfway there.",
        "Growth is the result of persistence and learning."
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Daily Habits
elif page == "🔄 Daily Habits":
    st.header("🔄 Build Strong Daily Habits")
    habits = ["Exercise", "Read", "Meditate", "Healthy Eating", "Plan Your Day"]
    
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Consistency is key! 🚀")
    
# Growth Mindset
elif page == "🌱 Growth Mindset":
    st.header("🌱 Develop a Growth Mindset")
    st.markdown("""
    A growth mindset is the belief that you can develop abilities through dedication and hard work.
    
    ### Growth Mindset Tips:
    1. Embrace challenges
    2. Learn from criticism
    3. Celebrate effort, not just results
    4. Be inspired by others’ success
    """)
    
# Mental Wellness
elif page == "🧘 Mental Wellness":
    st.header("🧘 Improve Your Mental Wellness")
    st.markdown("""
    Your mind is your greatest asset. Take care of it. 
    
    ✅ Practice mindfulness and meditation.  
    ✅ Avoid burnout by balancing work and rest.  
    ✅ Engage in hobbies that relax and recharge you.  
    """)
    
# Goal Mastery
elif page == "🎯 Goal Mastery":
    st.header("🎯 Master the Art of Goal Setting")
    goal = st.text_input("Set a new goal:")
    if goal:
        st.write(f"Your goal: {goal}")
    
    if st.button("Save Goal"):
        st.success("Goal saved successfully! Stay committed! 🚀")

# Productivity Hacks
elif page == "💡 Productivity Hacks":
    st.header("💡 Boost Your Productivity")
    tips = [
        "🕒 Use the Pomodoro technique for better focus.",
        "📋 Prioritize tasks using the Eisenhower Matrix.",
        "📵 Reduce distractions by setting app limits.",
        "📖 Continuous learning enhances efficiency."
    ]
    st.write(f"💡 **Tip for Today:** {random.choice(tips)}")
    
# Learning & Skills
elif page == "📚 Learning & Skills":
    st.header("📚 Keep Learning & Growing")
    st.markdown("""
    🎓 Learn something new every day! 
    
    ✅ Read books & articles.  
    ✅ Take online courses.  
    ✅ Practice critical thinking.  
    ✅ Engage in discussions with experts.
    """)
    
# Financial Growth
elif page == "💰 Financial Growth":
    st.header("💰 Develop Smart Financial Habits")
    st.markdown("""
    Secure your financial future with these steps:  
    
    ✅ Save at least 10% of your income.  
    ✅ Invest wisely for long-term benefits.  
    ✅ Track your spending and cut unnecessary costs.  
    ✅ Learn about financial literacy.  
    """)
    
# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Success & Growth Hub")

