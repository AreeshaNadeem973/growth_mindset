import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="Daily Motivation & Productivity Hub", page_icon="🌟")
st.title("🌟 Daily Motivation & Productivity Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Inspirational Stories",
    "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Self-Reflection", "🧠 Brain Teasers", "📊 Progress Analytics"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Daily Motivation & Productivity Hub! 🚀")
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg", use_container_width=True)
    st.markdown("""
    ### Why Focus on Productivity & Motivation?
    ✅ **Stay Inspired**: Start each day with positive energy.  
    ✅ **Build Consistent Habits**: Small steps lead to big success.  
    ✅ **Set and Achieve Goals**: Turn your dreams into reality.  
    ✅ **Develop a Growth Mindset**: Keep learning and improving!  
    """)
    
    st.success("Today is a new beginning! Make the most of it! 🚀")
    
    # Add a motivational quote of the day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

    # Added Graph: Weekly Productivity Levels
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    productivity_levels = np.random.randint(50, 100, size=7)  # Simulated productivity levels
    fig, ax = plt.subplots()
    ax.plot(days, productivity_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Productivity Levels")
    ax.set_ylabel("Productivity (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Habit Tracker Page
elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Daily Habits")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep up the good work!")
        st.balloons()
    
    # Weekly Habit Completion Graph
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='green')
    ax.set_title("Weekly Habit Completion")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Daily Motivation Page
elif page == "💭 Daily Motivation":
    st.header("💭 Get Inspired Every Day!")
    st.info(f"💡 **Today's Motivation:** {random.choice(quotes)}")
    
    motivation_level = st.slider("Rate your motivation level today:", 0, 100, 50)
    fig, ax = plt.subplots()
    ax.bar(["Motivation Level"], [motivation_level], color='orange')
    ax.set_ylabel("Percentage")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Success Stories to Keep You Going")
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
        ("🌍 **Nelson Mandela**", "Spent 27 years in prison and changed a nation."),
        ("🎶 **Ed Sheeran**", "Slept on sofas while pursuing music, now a global icon.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Progress Analytics Page
elif page == "📊 Progress Analytics":
    st.header("📊 Track Your Progress")
    
    labels = ["Productivity", "Motivation", "Consistency", "Focus"]
    values = [random.randint(50, 100) for _ in labels]
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['blue', 'green', 'orange', 'red'])
    ax.set_ylabel("Performance (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Your Weekly Performance")
    st.pyplot(fig)
    
    st.success("Keep improving and tracking your progress!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Daily Motivation & Productivity Hub")

