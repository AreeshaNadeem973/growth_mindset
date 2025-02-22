import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌟", layout="wide")

# Dark Mode Toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode")
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True) if dark_mode else None

# Points & Badges System
st.sidebar.header("🎖️ Your Progress")
points = st.sidebar.number_input("Current Points", min_value=0, value=st.session_state.get('points', 0), step=1)
st.session_state.points = points
badges = ["Beginner", "Learner", "Achiever", "Master"]
st.sidebar.write(f"🏅 Badge: {badges[min(points//10, len(badges)-1)]}")

# Navigation
page = st.sidebar.radio("📌 Navigate to:", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation",
    "📖 Inspirational Stories", "🎯 Goal Setting", "📝 Productivity Tips",
    "🤔 Self-Reflection", "🧠 Brain Teasers", "🧠 Growth Mindset", "🌍 Community"
])

# Home Page
if page == "🏡 Home":
    st.title("🌟 Welcome to Growth Mindset Challenge!")
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    st.success("Today is a new beginning! Make the most of it! 🚀")

    # Quote of the Day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

    # Motivation Trend Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# AI-Based Book & Video Recommendations
elif page == "🧠 Growth Mindset":
    st.header("🧠 Growth Mindset Challenge")
    books = [
        "Mindset - Carol S. Dweck",
        "Atomic Habits - James Clear",
        "Grit - Angela Duckworth",
        "The Power of Now - Eckhart Tolle",
    ]
    videos = [
        "https://www.youtube.com/watch?v=KUWn_TJTrnU",  # Growth Mindset Video
        "https://www.youtube.com/watch?v=Z-zNHHpXoMM"   # Atomic Habits Summary
    ]
    st.write(f"📚 **Recommended Book:** {random.choice(books)}")
    st.write(f"🎥 **Watch this video:** [Click here]({random.choice(videos)})")

# Community Page
elif page == "🌍 Community":
    st.header("🌍 Community Sharing")
    st.write("Share your progress, insights, and challenges with others!")
    user_story = st.text_area("Share your story or tip:")
    if st.button("Post to Community"):
        st.success("✅ Shared successfully! Inspire others! ✨")

# Leaderboard
st.sidebar.header("🏆 Leaderboard")
leaderboard = {"Alice": 120, "Bob": 90, "Charlie": 80, "You": points}
sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
st.sidebar.table(sorted_leaderboard)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Growth Mindset Challenge")
