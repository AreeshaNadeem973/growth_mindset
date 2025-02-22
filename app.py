import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title and Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌟")
st.title("🌟 Growth Mindset Challenge")

# Sidebar: Quick Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", 
    "📅 Habit Tracker", 
    "💭 Daily Motivation", 
    "📚 Inspirational Stories",
    "🎯 Goal Setting", 
    "📝 Productivity Tips", 
    "🤔 Self-Reflection", 
    "🧠 Brain Teasers", 
    "🧠 Growth Mindset", 
    "🌱 Mindfulness & Meditation", 
    "🏋️ Fitness & Health", 
    "🧛 Skill Development", 
    "📚 Journaling & Gratitude", 
    "🌟 Community & Sharing"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Growth Journey!")
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    st.success("Today is a new opportunity! Make the most of it! 🚀")
    
    # Weekly Motivation Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Mindfulness & Meditation Page
elif page == "🌱 Mindfulness & Meditation":
    st.header("🌱 Mindfulness & Meditation")
    st.write("Relax and focus with guided meditation.")
    if st.button("Start 5-Minute Meditation"):
        with st.empty():
            for secs in range(5*60, 0, -1):
                mm, ss = secs // 60, secs % 60
                st.metric("Time Remaining", f"{mm:02d}:{ss:02d}")
                time.sleep(1)
        st.success("Great job! Keep practicing mindfulness.")

# Fitness & Health Page
elif page == "🏋️ Fitness & Health":
    st.header("🏋️ Fitness & Health")
    exercises = ["Push-ups", "Squats", "Jumping Jacks", "Plank", "Burpees"]
    st.write("Daily Workout Plan:")
    for exercise in exercises:
        st.checkbox(f"Did you complete {exercise.lower()} today?")
    if st.button("Save Workout Log"):
        st.success("Awesome! Keep up the healthy habits!")
        st.balloons()

# Skill Development Page
elif page == "🧛 Skill Development":
    st.header("🧛 Skill Development")
    skills = ["Coding", "Public Speaking", "Writing", "Time Management", "Creativity"]
    selected_skill = st.selectbox("Choose a skill to improve:", skills)
    st.write(f"Great choice! Here are some resources for {selected_skill}:")
    st.write("- Online courses")
    st.write("- Practice exercises")
    st.write("- Daily challenges")
    if st.button("Track Progress"):
        st.success(f"Your {selected_skill} learning journey has begun!")

# Journaling & Gratitude Page
elif page == "📚 Journaling & Gratitude":
    st.header("📚 Daily Journaling & Gratitude")
    journal_entry = st.text_area("Write about your day:")
    gratitude = st.text_input("What are you grateful for today?")
    if st.button("Save Entry"):
        st.success("Your journal entry has been saved!")

# Community & Sharing Page
elif page == "🌟 Community & Sharing":
    st.header("🌟 Share Your Progress & Inspire Others!")
    user_story = st.text_area("Share your motivation story:")
    if st.button("Submit Story"):
        st.success("Thank you for sharing! Your story might inspire someone today!")
        st.balloons()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Growth Mindset Challenge")

