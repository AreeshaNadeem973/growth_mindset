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
    "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Self-Reflection", "🧠 Brain Teasers", "🧠 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Daily Motivation & Productivity Hub! 🚀")
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
    
    # Weekly Motivation Trend Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Habit Tracker")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep up the good work! 🎉")
        st.balloons()
    
    # Weekly Habit Progress Graph
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='green')
    ax.set_title("Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)
    
    # Streak Counter
    streak = st.session_state.get('streak', 0)
    st.write(f"🔥 Current Streak: {streak} days")
    if st.button("Increment Streak"):
        streak += 1
        st.session_state.streak = streak
        st.success(f"New streak: {streak} days!")

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
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
    
    # User Story Submission
    st.subheader("Share Your Own Inspirational Story")
    user_story = st.text_area("Your story:")
    if st.button("Submit Story"):
        st.success("Thank you for sharing your story!")

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")
    goal_types = ["Short-term", "Medium-term", "Long-term"]
    for goal_type in goal_types:
        st.subheader(f"{goal_type} Goals")
        goal = st.text_input(f"Enter a {goal_type.lower()} goal:")
        if goal:
            st.write(f"Your {goal_type.lower()} goal: {goal}")
    
    if st.button("Save Goals"):
        st.success("Goals saved successfully! 🎯")
        st.balloons()

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
    ]
    st.write(f"💡 **Tip for Today:** {random.choice(tips)}")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")
    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    st.write(f"You felt {mood} today.")

    accomplishments = st.text_area("What did you accomplish today?")
    if st.button("Save Reflection"):
        st.success("✅ Reflection saved! Keep growing! 🚀")

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
    ]
    
    question, answer = random.choice(riddles)
    st.write(question)
    user_answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! Well done! 🎉")
        else:
            st.error(f"Not quite. The correct answer is: {answer}")

# Growth Mindset
elif page == "🧠 Growth Mindset":
    st.header("🧠 Develop a Growth Mindset")
    st.markdown("""
    ### What is a Growth Mindset?
    A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    """)
    
    challenges = [
        "Try something new today and reflect on what you learned.",
        "Reframe a recent failure as a learning opportunity.",
    ]
    st.write(f"Today's Challenge: {random.choice(challenges)}")
    
    if st.button("I Accept the Challenge"):
        st.success("Great! Embrace the challenge and grow! 🎉")
        st.balloons()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Daily Motivation & Productivity Hub")
