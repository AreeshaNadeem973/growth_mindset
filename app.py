import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Configuration
st.set_page_config(page_title="🚀 Peak Performance Hub", page_icon="⚡", layout="wide")
st.title("🚀 Peak Performance Hub: Unlock Your Potential")

# Sidebar Navigation
st.sidebar.header("📌 Navigate")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Success Stories",
    "🎯 Goal Setting", "📝 Productivity Hacks", "🤔 Self-Reflection", "🧠 Brain Boosters", "🧠 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Peak Performance Hub! 🌟")
    st.markdown("""
    **Why This Hub?**
    - 🚀 *Boost Productivity* – Stay focused and achieve more.
    - 💡 *Stay Inspired* – Daily motivation to keep you going.
    - 🎯 *Achieve Your Goals* – Turn dreams into reality.
    - 📈 *Track Progress* – Small steps lead to big success.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://source.unsplash.com/400x300/?motivation,success", use_column_width=True)
    with col2:
        st.image("https://source.unsplash.com/400x300/?growth,mindset", use_column_width=True)
    
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis"
    ]
    st.success(f"💡 **Quote of the Day:** {random.choice(quotes)}")
    
    # Motivation Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Your Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(50, 100)
    st.pyplot(fig)

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Build Powerful Habits")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep going! 🔥")
        st.balloons()
    
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='green')
    ax.set_title("Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Get Your Daily Dose of Motivation")
    motivation_quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small improvements daily lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*"
    ]
    st.success(f"💡 **Today's Motivation:** {random.choice(motivation_quotes)}")
    
    motivation_level = st.slider("Rate your motivation level today:", 0, 100, 50)
    fig, ax = plt.subplots()
    ax.bar(["Motivation Level"], [motivation_level], color='orange')
    ax.set_ylabel("Percentage")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Be Inspired by These Stories")
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
        ("🌍 **Oprah Winfrey**", "Overcame adversity to become a media mogul."),
        ("🎶 **Ed Sheeran**", "Slept on sofas while pursuing music, now a global star.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
        st.image("https://source.unsplash.com/400x250/?success,achievement", use_column_width=True)

# Productivity Hacks
elif page == "📝 Productivity Hacks":
    st.header("📝 Supercharge Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "📵 **Reduce Distractions** – Limit social media to stay focused."
    ]
    st.write(f"💡 **Tip for Today:** {random.choice(tips)}")

# Growth Mindset
elif page == "🧠 Growth Mindset":
    st.header("🧠 Develop a Growth Mindset")
    st.markdown("""
    **Key Principles:**
    1. Embrace challenges
    2. Persist in setbacks
    3. Learn from criticism
    4. See effort as the path to mastery
    """)
    
    st.subheader("💡 Growth Mindset Challenge")
    challenges = [
        "Try something new today and reflect on what you learned.",
        "Reframe a recent failure as a learning opportunity.",
        "Ask for feedback on a recent project and act on it."
    ]
    st.write(f"Today's Challenge: {random.choice(challenges)}")
    
    if st.button("I Accept the Challenge"):
        st.success("Great! Embrace the challenge and grow! 🚀")
        st.balloons()

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Peak Performance Hub")
