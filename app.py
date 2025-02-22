import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Next-Gen Power", page_icon="🚀")
st.title("Next-Gen Power: Mindset, Innovation & Success")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
if "current_book" in st.session_state:
    st.session_state.page = "📚 Reading"
else:
    st.session_state.page = st.sidebar.radio("Go to:", [
        "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights", "🗓 Set Your Vision", "💪 Daily Challenges", "🎥 Video Recommendations", "🔍 AI-Powered Book Suggestions"
    ])

# Additional Pages Data
daily_challenges = [
    "Write down three things you're grateful for today.",
    "Spend 10 minutes meditating on your goals.",
    "Read 10 pages of a book that inspires you.",
    "Reach out to someone and give them a genuine compliment.",
    "Try a new productivity technique today!"
]

video_recommendations = [
    {"title": "The Power of Habit", "url": "https://www.youtube.com/watch?v=OMBS5eCcPzg"},
    {"title": "How to Build a Growth Mindset", "url": "https://www.youtube.com/watch?v=M1CHPnZfFmU"},
    {"title": "The Psychology of Motivation", "url": "https://www.youtube.com/watch?v=9giPsqtRZ3M"}
]

# Home Page
if st.session_state.page == "🏡 Home":
    st.header("🚀 Welcome to Next-Gen Power")
    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", use_container_width=True)
    st.markdown("""
    ### Unlock Your Full Potential with Knowledge!
    ✅ **Master the Art of Success** 📚  
    ✅ **Track Your Personal Growth** 📊  
    ✅ **Join a Community of Innovators** 💡  
    """)
    st.success("Start your journey to greatness today! 🚀")

# Daily Challenges Page
elif st.session_state.page == "💪 Daily Challenges":
    st.header("💪 Daily Challenges for Growth")
    challenge = np.random.choice(daily_challenges)
    st.info(f"Today's Challenge: {challenge}")

# Video Recommendations Page
elif st.session_state.page == "🎥 Video Recommendations":
    st.header("🎥 Top Video Recommendations")
    for video in video_recommendations:
        st.subheader(video["title"])
        st.video(video["url"])

# AI-Powered Book Suggestions Page
elif st.session_state.page == "🔍 AI-Powered Book Suggestions":
    st.header("🔍 Personalized Book Suggestions")
    st.write("AI-powered recommendations coming soon!")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")
