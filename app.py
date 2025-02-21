import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="🚀 Peak Performance Hub", page_icon="🌟")
st.title("🚀 Peak Performance Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Inspirational Stories",
    "🎯 Goal Setting", "📝 Productivity Hacks", "🤔 Self-Reflection", "🧠 Brain Teasers", "🧠 Growth Mindset"
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
    
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")
    
# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Habit Tracker")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep up the good work!")
        st.balloons()

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Your Daily Dose of Motivation")
    quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small daily improvements lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*"
    ]
    st.success(f"💡 **Today's Motivation:** {random.choice(quotes)}")

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Real-Life Success Stories")
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")
    st.write("Setting clear goals is the first step towards achieving them.")
    goal = st.text_input("Enter your goal:")
    if goal:
        st.write(f"Your goal: {goal}")
    
# Productivity Hacks
elif page == "📝 Productivity Hacks":
    st.header("📝 Boost Your Productivity")
    st.write("Here are some powerful productivity hacks:")
    st.markdown("""
    - 🕒 **Time Blocking** – Schedule time for tasks to improve focus.
    - 📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.
    - 📵 **Digital Detox** – Reduce screen time for better concentration.
    """)

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")
    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    st.write(f"You felt {mood} today.")

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    st.write("Solve this riddle:")
    riddle = "What has keys but can't open locks?"
    st.write(riddle)
    user_answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if user_answer.lower() == "piano":
            st.success("Correct! Well done!")
        else:
            st.error("Not quite. The correct answer is: A piano")

# Growth Mindset
elif page == "🧠 Growth Mindset":
    st.header("🧠 Develop a Growth Mindset")
    st.markdown("""
    ### What is a Growth Mindset?
    A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    """)
