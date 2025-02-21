
 import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="🚀 Peak Performance Hub", page_icon="🌟")
st.title("🌟 Peak Performance Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "⚡ Productivity Hacks", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Inspirational Stories",
    "🎯 Goal Setting", "🤔 Self-Reflection", "🧠 Brain Teasers", "🚀 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Peak Performance Hub! 🚀")
    st.markdown("""
    ### Why Focus on Productivity & Motivation?
    ✅ **Stay Inspired**: Start each day with positive energy.  
    ✅ **Build Consistent Habits**: Small steps lead to big success.  
    ✅ **Set and Achieve Goals**: Turn your dreams into reality.  
    ✅ **Develop a Growth Mindset**: Keep learning and improving!  
    """)
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    st.success("Today is a new beginning! Make the most of it! 🚀")
    
    # Add a motivational quote of the day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")
    
    # Added Graph: Weekly Motivation Trend
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)  # Simulated motivation levels
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Productivity Hacks Page
elif page == "⚡ Productivity Hacks":
    st.header("⚡ Boost Your Productivity")
    st.write("Maximize your efficiency with these powerful productivity hacks.")
    
    # Productivity Tips
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity.",
        "📵 **Reduce Distractions** – Limit social media to stay focused.",
        "⏳ **Use the 2-Minute Rule** – If a task takes less than 2 minutes, do it immediately!",
        "🚀 **Batch Similar Tasks** – Work smarter by grouping similar tasks together!"
    ]
    st.write(f"💡 **Tip for Today:** {tips[date.today().day % len(tips)]}")
    
    # Productivity Pie Chart
    fig, ax = plt.subplots()
    sizes = [60, 25, 15]
    labels = ["Focused Work", "Breaks", "Distractions"]
    colors = ["green", "yellow", "red"]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    
    # Productivity Timer
    st.subheader("Pomodoro Timer")
    minutes = st.number_input("Set timer (minutes):", min_value=1, max_value=60, value=25)
    if st.button("Start Timer"):
        with st.empty():
            for secs in range(minutes * 60, 0, -1):
                mm, ss = secs // 60, secs % 60
                st.metric("Time Remaining", f"{mm:02d}:{ss:02d}")
                time.sleep(1)
            st.success("Time's up! Take a break.")
            st.balloons()
    
    # Productivity Checklist
    st.subheader("✅ Productivity Checklist")
    checklist = [
        "Plan your day the night before",
        "Eliminate unnecessary tasks",
        "Use a task management system",
        "Take regular short breaks",
        "Stay hydrated and eat well"
    ]
    for task in checklist:
        st.checkbox(task)
    
    st.success("Stay consistent and you'll see amazing results! 🚀")
