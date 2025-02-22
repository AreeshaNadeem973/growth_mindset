import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import date

# App Title
st.set_page_config(page_title="Motivation & Productivity Hub", page_icon="🌟")
st.title("🌟 Motivation & Productivity Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💡 Daily Inspiration", "📖 Success Stories",
    "🎯 Goal Setting", "📊 Productivity Stats", "📝 Self-Reflection", "🧠 Brain Boost"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Motivation & Productivity Hub! 🚀")
    st.image("https://source.unsplash.com/featured/?motivation", use_container_width=True)
    st.markdown("""
    ### Stay Inspired & Achieve More!
    ✅ **Daily Motivation & Tips**  
    ✅ **Track Your Habits & Goals**  
    ✅ **Boost Your Brain with Challenges**  
    ✅ **Improve Productivity with Data Insights**  
    """)
    st.success("Every day is a new opportunity! Make it count! 🚀")
    
    # Motivational Quote
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Believe in yourself and all that you are!",
        "Small daily improvements lead to stunning results!",
        "Your potential is endless. Keep going!"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Daily Habits")
    habits = ["Exercise", "Reading", "Meditation", "Healthy Eating", "Journaling"]
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep it up!")
        st.balloons()

    # Habit Progress Graph
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='green')
    ax.set_title("Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Daily Inspiration
elif page == "💡 Daily Inspiration":
    st.header("💡 Get Inspired Today!")
    inspirations = [
        "Start where you are. Use what you have. Do what you can.",
        "Your future is created by what you do today, not tomorrow.",
        "Success doesn't come from what you do occasionally, but from what you do consistently.",
    ]
    st.success(f"🌟 **Today's Inspiration:** {random.choice(inspirations)}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Real-Life Success Stories")
    stories = {
        "Elon Musk": "Started multiple companies and transformed industries.",
        "J.K. Rowling": "Rejected 12 times before publishing Harry Potter.",
        "Michael Jordan": "Was cut from his high school team but became an icon."
    }
    for name, story in stories.items():
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set & Achieve Your Goals")
    goal = st.text_input("Your Goal:")
    steps = st.text_area("Steps to achieve it:")
    if st.button("Save Goal"):
        st.success("Goal saved successfully!")

# Productivity Stats
elif page == "📊 Productivity Stats":
    st.header("📊 Analyze Your Productivity")
    categories = ["Deep Work", "Breaks", "Distractions"]
    values = [random.randint(20, 60) for _ in categories]
    fig, ax = plt.subplots()
    ax.pie(values, labels=categories, autopct='%1.1f%%', colors=['blue', 'yellow', 'red'])
    ax.set_title("Time Spent on Productivity")
    st.pyplot(fig)

# Self-Reflection
elif page == "📝 Self-Reflection":
    st.header("📝 End-of-Day Reflection")
    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    accomplishments = st.text_area("What did you accomplish today?")
    gratitude = st.text_area("What are you grateful for today?")
    if st.button("Save Reflection"):
        st.success("Reflection saved! Keep growing!")

# Brain Boost
elif page == "🧠 Brain Boost":
    st.header("🧠 Challenge Your Brain")
    riddles = [
        ("What has keys but can't open locks?", "A piano"),
        ("What has to be broken before you can use it?", "An egg")
    ]
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    user_answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! Well done!")
        else:
            st.error(f"Not quite. The correct answer is: {answer}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Motivation & Productivity Hub")
