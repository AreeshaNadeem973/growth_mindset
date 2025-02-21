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
    "🏡 Home", "📅 Habit Tracker", "💡 Daily Wisdom", "📖 Inspirational Stories",
    "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Self-Reflection", "🧠 Brain Boost"
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
    
    # Motivational Quote of the Day
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

    # Weekly Habit Progress Graph
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='green')
    ax.set_title("Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Daily Wisdom
elif page == "💡 Daily Wisdom":
    st.header("💡 Your Daily Dose of Wisdom")
    
    wisdom_quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small daily improvements lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*", 
        "💡 *Work hard in silence, let success make the noise.*",
        "🌱 *Your only limit is the one you set yourself!*"
    ]
    st.success(f"💡 **Today's Wisdom:** {random.choice(wisdom_quotes)}")

    # Weekly Focus Trend Graph (Fixed Error)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    focus_levels = np.random.randint(50, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, focus_levels, marker='o', linestyle='--', color='purple')
    ax.set_title("Weekly Focus Trend")
    ax.set_ylabel("Focus Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Real-Life Success Stories")
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
        ("🌍 **Nelson Mandela**", "Spent 27 years in prison and changed a nation.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")
    
    goal = st.text_input("Enter your main goal:")
    if goal:
        st.write(f"Your Goal: {goal}")
    
    steps = st.text_area("Steps to achieve your goal:")
    if steps:
        st.write("Your action plan:")
        for step in steps.split('\n'):
            st.write(f"- {step}")

    if st.button("Save Goal"):
        st.success("Goal saved successfully!")

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity."
    ]
    st.write(f"💡 **Tip for Today:** {random.choice(tips)}")

    # Productivity Pie Chart
    fig, ax = plt.subplots()
    sizes = [60, 25, 15]
    labels = ["Focused Work", "Breaks", "Distractions"]
    colors = ["green", "yellow", "red"]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")

    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    st.write(f"You felt {mood} today.")

    accomplishments = st.text_area("What did you accomplish today?")
    challenges = st.text_area("What challenges did you face?")
    gratitude = st.text_area("What are you grateful for today?")

    if st.button("Save Reflection"):
        st.success("✅ Reflection saved! Keep growing!")
        st.balloons()

# Brain Boost
elif page == "🧠 Brain Boost":
    st.header("🧠 Brain-Boosting Challenges")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg")
    ]
    
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    user_answer = st.text_input("Your answer:")
    
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! Well done!")
            st.balloons()
        else:
            st.error(f"Not quite. The correct answer is: {answer}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Daily Motivation & Productivity Hub")
