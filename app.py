import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Next-Gen Power", page_icon="🚀")
st.title("Mindset & Success Hub: Unlock Your Potential")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
st.session_state.page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights", "📅 Set Your Vision", "🎯 Daily Growth Challenge", "🧠 Mindset Quiz", "📋 Goal Tracker", "💬 Community Polls"
])

# Home Page
if st.session_state.page == "🏡 Home":
    st.header("🚀 Welcome to Next-Gen Power")
    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", use_container_width=True)
    st.markdown("""
    ### Unlock Your Full Potential with Knowledge!
    ✅ **Master the Art of Success** 📖  
    ✅ **Track Your Personal Growth** 📊  
    ✅ **Join a Community of Innovators** 💡  
    """)
    st.success("Start your journey to greatness today! 🚀")

# Daily Growth Challenge
elif st.session_state.page == "🎯 Daily Growth Challenge":
    st.header("🎯 Your Daily Growth Challenge")
    challenges = [
        "Write down three things you're grateful for.",
        "Read a chapter of a book that inspires you.",
        "Practice deep breathing for 5 minutes.",
        "Take a 10-minute walk outside and reflect.",
        "Set a small goal and complete it today."
    ]
    challenge = random.choice(challenges)
    st.write(f"🔹 **Today's Challenge:** {challenge}")
    if st.button("✅ Mark as Done"):
        st.success("Great job! Keep building momentum! 💪")

# Mindset Quiz
elif st.session_state.page == "🧠 Mindset Quiz":
    st.header("🧠 Test Your Growth Mindset")
    questions = [
        ("Do you believe intelligence can be developed?", ["Yes", "No"]),
        ("How do you handle failure?", ["Learn from it", "Avoid it"]),
        ("Do you set long-term goals?", ["Yes", "No"])
    ]
    score = 0
    for q, options in questions:
        answer = st.radio(q, options)
        if answer == options[0]:
            score += 1
    if st.button("Submit Answers"):
        st.success(f"Your Growth Mindset Score: {score}/{len(questions)}")

# Goal Tracker
elif st.session_state.page == "📋 Goal Tracker":
    st.header("📋 Track Your Goals")
    goal = st.text_input("Set a new goal:")
    if st.button("Save Goal"):
        st.success("Your goal is now set! Keep growing! 🚀")

# Community Polls
elif st.session_state.page == "💬 Community Polls":
    st.header("💬 Community Poll: What's Your Success Mantra?")
    options = ["Hard Work", "Consistency", "Smart Work", "Resilience"]
    vote = st.radio("Select your mantra:", options)
    if st.button("Vote"):
        st.success("Thanks for voting! See what others think too! 📊")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")

