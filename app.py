import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import time

# App Configuration
st.set_page_config(page_title="Limitless Growth Hub 🚀", page_icon="🌟")
st.title("🚀 Limitless Growth Hub: Unlock Your Full Potential")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "🧠 Growth Mindset", "⏳ Productivity Hacks", "🎯 Goal Setting",
    "📅 Habit Building", "💪 Overcoming Challenges", "💰 Career & Finance", "📖 Self-Reflection"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Limitless Growth Hub! 🌱")
    st.markdown("""
    ### Why Focus on Growth?
    ✅ **Develop a Strong Mindset** for success.  
    ✅ **Master Productivity & Time Management** to achieve more.  
    ✅ **Set & Crush Your Goals** with proven strategies.  
    ✅ **Build Habits That Last** and transform your life.  
    ✅ **Learn & Grow Continuously** for lifelong success.
    """)
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    st.success("Your journey to unlimited growth starts today! 🚀")

# Growth Mindset Page
elif page == "🧠 Growth Mindset":
    st.header("🧠 Develop a Growth Mindset")
    st.write("A growth mindset helps you embrace challenges and improve continuously.")
    st.subheader("Key Principles:")
    st.write("- Embrace challenges as opportunities.")
    st.write("- Learn from feedback and failures.")
    st.write("- Keep putting in effort and stay persistent.")
    
    # Daily Challenge
    challenges = [
        "Try something new and reflect on what you learned.",
        "Reframe a recent failure as a learning experience.",
        "Ask for constructive feedback and implement it.",
        "Set a challenging goal and take action.",
        "Practice positive self-talk when facing a challenge."
    ]
    st.write(f"🌟 **Today's Challenge:** {random.choice(challenges)}")

# Productivity Hacks Page
elif page == "⏳ Productivity Hacks":
    st.header("⏳ Boost Your Productivity")
    st.write("Time is your most valuable asset. Use it wisely!")
    
    tips = [
        "Use the Pomodoro technique to stay focused.",
        "Start your day with the most important task.",
        "Avoid multitasking, focus on one task at a time.",
        "Take regular breaks to maintain energy levels.",
        "Use a to-do list to track daily tasks."
    ]
    st.write(f"💡 **Tip for Today:** {random.choice(tips)}")
    
    # Productivity Chart
    fig, ax = plt.subplots()
    sizes = [60, 25, 15]
    labels = ["Deep Work", "Breaks", "Distractions"]
    colors = ["green", "yellow", "red"]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Goal Setting Page
elif page == "🎯 Goal Setting":
    st.header("🎯 Set & Achieve Your Goals")
    st.write("Success begins with clear goals and an action plan.")
    
    goal = st.text_input("Enter your goal:")
    steps = st.text_area("Steps to achieve this goal:")
    if st.button("Save Goal"):
        st.success("Goal saved! Now take action! 🚀")

# Habit Building Page
elif page == "📅 Habit Building":
    st.header("📅 Build Powerful Habits")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Wake Up Early"]
    
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    if st.button("Save Progress"):
        st.success("Keep up the good work! 🔥")
        st.balloons()

# Overcoming Challenges Page
elif page == "💪 Overcoming Challenges":
    st.header("💪 Face Challenges with Confidence")
    st.write("Every challenge is an opportunity to grow.")
    
    obstacles = [
        "Fear of failure", "Lack of motivation", "Time management issues",
        "Procrastination", "Self-doubt"
    ]
    selected_obstacle = st.selectbox("Which challenge are you facing?", obstacles)
    
    solutions = {
        "Fear of failure": "Focus on progress, not perfection.",
        "Lack of motivation": "Find your 'why' and remind yourself daily.",
        "Time management issues": "Prioritize your tasks and use time blocking.",
        "Procrastination": "Use the 5-minute rule—just start!",
        "Self-doubt": "Replace negative thoughts with empowering beliefs."
    }
    st.write(f"✅ Solution: {solutions[selected_obstacle]}")

# Career & Finance Growth Page
elif page == "💰 Career & Finance":
    st.header("💰 Build Wealth & Career Success")
    st.write("Take control of your finances and career growth.")
    
    finance_tips = [
        "Save at least 20% of your income.",
        "Invest in self-education.",
        "Build multiple income streams.",
        "Create a monthly budget and stick to it.",
        "Focus on skills that increase your earning potential."
    ]
    st.write(f"💡 **Finance Tip:** {random.choice(finance_tips)}")

# Self-Reflection Page
elif page == "📖 Self-Reflection":
    st.header("📖 Reflect & Improve Daily")
    st.write("End each day with self-reflection and gratitude.")
    
    mood = st.select_slider("How was your day?", options=["😔", "😐", "🙂", "😊", "😃"])
    st.write(f"You felt {mood} today.")
    accomplishments = st.text_area("What did you achieve today?")
    lessons = st.text_area("What did you learn today?")
    
    if st.button("Save Reflection"):
        st.success("Reflection saved! Keep growing! 🌱")
        st.balloons()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Limitless Growth Hub")
