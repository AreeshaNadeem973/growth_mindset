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
    "🏡 Dashboard", "📅 Habit Builder", "💡 Daily Inspiration", "🌟 Success Stories",
    "🎯 Goal Mastery", "⚡ Productivity Hacks", "🤔 Reflect & Grow", "🧠 Mind Gym", "🚀 Growth Mindset"
])

# Dashboard (Home Page)
if page == "🏡 Dashboard":
    st.header("Welcome to Peak Performance Hub! 🚀")
    st.markdown("""
    ### Elevate Your Mindset & Productivity
    ✅ **Stay Inspired**: Kickstart your day with motivation.  
    ✅ **Build Powerful Habits**: Small changes, big results.  
    ✅ **Crush Your Goals**: Turn ambition into action.  
    ✅ **Develop a Winning Mindset**: Growth starts here.  
    """)
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    st.success("Every day is a fresh start! Make it count. 🚀")

    # Motivational Quote of the Day
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
    ax.set_title("📈 Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Habit Builder
elif page == "📅 Habit Builder":
    st.header("📅 Build Your Success Habits")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep going!")
        st.balloons()
    
    # Weekly Habit Progress Graph
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='green')
    ax.set_title("📊 Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Daily Inspiration
elif page == "💡 Daily Inspiration":
    st.header("💡 Power Up with Daily Inspiration")
    quotes = [
        "🌟 *Believe in yourself and all that you are!*",
        "🚀 *Small daily improvements lead to stunning results!*",
        "🔥 *Your potential is limitless. Keep pushing forward!*",
        "💡 *Work hard in silence, let success make the noise.*",
        "🌱 *Growth begins at the end of your comfort zone!*",
        "💪 *Success is the sum of small efforts, repeated daily.*"
    ]
    st.success(f"💡 **Today's Inspiration:** {random.choice(quotes)}")

# Success Stories
elif page == "🌟 Success Stories":
    st.header("🌟 Real-Life Success Stories")
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

# Goal Mastery
elif page == "🎯 Goal Mastery":
    st.header("🎯 Set & Conquer Your Goals")
    goal_types = ["Short-term", "Medium-term", "Long-term"]
    for goal_type in goal_types:
        st.subheader(f"{goal_type} Goals")
        goal = st.text_input(f"Enter a {goal_type.lower()} goal:")
        if goal:
            st.write(f"Your {goal_type.lower()} goal: {goal}")

# Productivity Hacks
elif page == "⚡ Productivity Hacks":
    st.header("⚡ Supercharge Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity.",
        "📵 **Reduce Distractions** – Limit social media to stay focused."
    ]
    st.write(f"💡 **Tip for Today:** {random.choice(tips)}")

# Reflect & Grow
elif page == "🤔 Reflect & Grow":
    st.header("🤔 End-of-Day Reflection")
    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    st.write(f"You felt {mood} today.")

# Mind Gym
elif page == "🧠 Mind Gym":
    st.header("🧠 Train Your Brain")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
        ("❓ **I speak without a mouth and hear without ears. What am I?**", "An echo")
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

# Growth Mindset
elif page == "🚀 Growth Mindset":
    st.header("🚀 Develop a Growth Mindset")
    st.markdown("""
    ### What is a Growth Mindset?
    A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    """)
    
    # Growth Mindset Challenge
    challenges = [
        "Try something new today and reflect on what you learned.",
        "Reframe a recent failure as a learning opportunity.",
        "Ask for feedback on a recent project and act on it.",
        "Set a challenging goal and create a plan to achieve it.",
        "Practice positive self-talk when facing a difficult task."
    ]
    st.write(f"Today's Challenge: {random.choice(challenges)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | 🚀 Peak Performance Hub")
