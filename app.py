import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Configuration
st.set_page_config(page_title="🚀 Peak Performance Hub", page_icon="🔥", layout="wide")

# Sidebar Navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3094/3094876.png", width=100)
st.sidebar.title("🚀 Peak Performance Hub")
st.sidebar.markdown("### Elevate Your Mindset & Productivity")

page = st.sidebar.radio("Navigate", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Success Stories",
    "🎯 Goal Setting", "📝 Productivity Hacks", "🤔 Self-Reflection", "🧠 Brain Teasers", "🔝 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.image("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0", use_column_width=True)
    st.title("Welcome to 🚀 Peak Performance Hub")
    
    st.markdown("""
    ## Why Join?
    ✅ **Stay Inspired** – Daily motivation to uplift your spirits.  
    ✅ **Build Habits** – Track your progress towards success.  
    ✅ **Set Goals** – Structure your dreams into reality.  
    ✅ **Sharpen Your Mind** – Solve brain teasers and boost intelligence.  
    """)
    
    st.success("💡 *Remember, every expert was once a beginner!*")

    # Quote of the Day
    quotes = [
        "Dream big, work hard, stay focused! 🔥",
        "Challenges are opportunities in disguise. 🚀",
        "Success is a journey, not a destination. 🌍",
        "Consistency beats talent when talent doesn’t work hard. ⚡"
    ]
    st.info(f"📢 **Quote of the Day:** {random.choice(quotes)}")

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.title("📅 Habit Tracker – Build Consistency")
    habits = ["Exercise 🏋️", "Read 📖", "Meditate 🧘", "Drink Water 💧", "Journaling ✍️"]

    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today? ✅")

    if st.button("Save Progress"):
        st.success("Great job! Keep pushing forward! 🔥")
        st.balloons()

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.title("💭 Daily Motivation – Power Up Your Day")
    quotes = [
        "💪 *Your only limit is you!*",
        "🚀 *Every day is a new opportunity to be better!*",
        "🔥 *Hard work always beats talent!*",
        "💡 *Your potential is limitless!*"
    ]
    st.success(f"🔝 **Today's Motivation:** {random.choice(quotes)}")

    # Motivation Level
    motivation_level = st.slider("How motivated are you today? 🎯", 0, 100, 50)
    fig, ax = plt.subplots()
    ax.bar(["Motivation Level"], [motivation_level], color='orange')
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Success Stories
elif page == "📖 Success Stories":
    st.title("📖 Inspiring Success Stories")
    st.markdown("### Learn from those who turned struggles into success!")

    stories = [
        {
            "name": "💡 **Elon Musk**",
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Elon_Musk_%28cropped%29.jpg",
            "story": "From failing SpaceX launches to revolutionizing Tesla, Elon Musk never stopped innovating.",
            "lesson": "🚀 **Lesson:** Failures are just stepping stones to success!"
        },
        {
            "name": "📚 **J.K. Rowling**",
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/ab/J._K._Rowling_2010.jpg",
            "story": "Rejected 12 times before Harry Potter became a global phenomenon.",
            "lesson": "📖 **Lesson:** Keep believing in your dreams!"
        },
        {
            "name": "🏀 **Michael Jordan**",
            "image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Michael_Jordan_in_2014.jpg",
            "story": "Cut from his high school team but became the greatest basketball player ever.",
            "lesson": "🔥 **Lesson:** Hard work beats everything!"
        }
    ]

    for s in stories:
        st.image(s["image"], width=250)
        st.subheader(s["name"])
        st.write(s["story"])
        st.success(s["lesson"])
        st.markdown("---")

# Goal Setting
elif page == "🎯 Goal Setting":
    st.title("🎯 Set Your Goals & Achieve Them")
    goal_types = ["Short-term ⏳", "Mid-term 📆", "Long-term 🏆"]

    for goal_type in goal_types:
        st.subheader(f"{goal_type} Goals")
        goal = st.text_input(f"Set a {goal_type.lower()} goal:")
        if goal:
            st.write(f"✅ Your goal: {goal}")

# Productivity Hacks
elif page == "📝 Productivity Hacks":
    st.title("📝 Supercharge Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Assign dedicated time for deep work.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix.",
        "📵 **Limit Distractions** – Set social media limits.",
        "💤 **Rest & Recharge** – Sleep fuels productivity."
    ]
    st.write(f"💡 **Tip of the Day:** {random.choice(tips)}")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.title("🤔 Reflect & Improve")
    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    st.write(f"You felt {mood} today.")

    st.text_area("Today's Accomplishments:")
    st.text_area("Challenges Faced:")
    st.text_area("Lessons Learned:")
    st.text_area("Gratitude Notes:")

    if st.button("Save Reflection"):
        st.success("✅ Reflection saved!")

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.title("🧠 Brain Teasers – Sharpen Your Mind")
    riddles = [
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
        ("❓ **I speak without a mouth and hear without ears. What am I?**", "An echo")
    ]
    
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    user_answer = st.text_input("Your answer:")
    
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The answer is: {answer}")

# Growth Mindset
elif page == "🔝 Growth Mindset":
    st.title("🔝 Develop a Growth Mindset")
    st.markdown("""
    ### Key Principles:
    ✅ Embrace Challenges  
    ✅ Persist Through Setbacks  
    ✅ Learn from Feedback  
    ✅ Keep Growing & Improving  
    """)

    # Growth Mindset Challenge
    challenges = [
        "Try something new and reflect on it.",
        "Reframe a recent failure as a learning opportunity.",
        "Ask for feedback and act on it.",
        "Practice positive self-talk."
    ]
    st.write(f"🔝 **Today's Challenge:** {random.choice(challenges)}")

    if st.button("Accept Challenge"):
        st.success("Great! Keep growing! 🔥")

# Footer
st.markdown("---")
st.markdown("🔹 Built with ❤️ using Streamlit | © 2025 🚀 Peak Performance Hub")
