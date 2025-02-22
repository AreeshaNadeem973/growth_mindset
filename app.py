import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random

# App Title
st.set_page_config(page_title="Next-Gen Power", page_icon="🚀")
st.title("Next-Gen Power: Mindset, Innovation & Success")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"
if "current_book" not in st.session_state:
    st.session_state.current_book = None
if "completed_books" not in st.session_state:
    st.session_state.completed_books = []

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
st.session_state.page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights",
    "📅 Set Your Vision", "🎯 Daily Challenge", "🎥 Video Inspirations", "🧠 AI Book Suggestions", "💬 Community Discussion", "🏆 Achievements & Badges"
])

# Book Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Improvement"},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "category": "Productivity"},
    {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "category": "Psychology"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "category": "Self-Help"},
    {"title": "Awaken the Giant Within", "author": "Tony Robbins", "category": "Motivation"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "category": "Wealth"}
]

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

# Daily Challenge
elif st.session_state.page == "🎯 Daily Challenge":
    st.header("🎯 Your Daily Challenge")
    challenges = [
        "Write down 3 things you're grateful for today.",
        "Spend 30 minutes reading a new book.",
        "Wake up 1 hour earlier and plan your day.",
        "Reach out to a mentor or inspiring person.",
        "Limit social media usage to 30 minutes.",
    ]
    challenge_of_the_day = random.choice(challenges)
    st.subheader(f"🔥 Today's Challenge: {challenge_of_the_day}")
    if st.button("I Completed This! ✅"):
        st.success("Awesome! Keep the momentum going! 🚀")

# Video Inspirations
elif st.session_state.page == "🎥 Video Inspirations":
    st.header("🎥 Get Inspired with Success Stories")
    videos = [
        {"title": "How to Train Your Mind for Success", "url": "https://www.youtube.com/watch?v=2XUFptF7hRU"},
        {"title": "The Power of a Growth Mindset", "url": "https://www.youtube.com/watch?v=KUWn_TJTrnU"},
        {"title": "Atomic Habits: The Power of Small Wins", "url": "https://www.youtube.com/watch?v=U_nzqnXWvSo"}
    ]
    for video in videos:
        st.subheader(video["title"])
        st.video(video["url"])

# AI Book Suggestions
elif st.session_state.page == "🧠 AI Book Suggestions":
    st.header("🧠 Personalized Book Recommendations")
    user_interest = st.selectbox("Select an interest:", ["Productivity", "Self-Help", "Psychology", "Wealth", "Motivation"])
    suggestions = [book["title"] for book in books if book["category"] == user_interest]
    if suggestions:
        st.success(f"📚 Recommended for you: {random.choice(suggestions)}")
    else:
        st.warning("No books found in this category.")

# Community Discussion
elif st.session_state.page == "💬 Community Discussion":
    st.header("💬 Join the Conversation")
    discussion_topic = st.text_area("What’s on your mind?")
    if st.button("Post"):
        st.success("Your discussion has been shared!")

# Achievements & Badges
elif st.session_state.page == "🏆 Achievements & Badges":
    st.header("🏆 Your Achievements")
    if len(st.session_state.completed_books) > 0:
        st.success(f"You've completed {len(st.session_state.completed_books)} books! 🎉")
    else:
        st.info("Start reading to unlock achievements!")
    
# Reading Progress (Existing Page)
elif st.session_state.page == "📊 Your Growth Journey":
    st.header("📊 Your Growth Journey")
    progress = np.random.randint(0, 100, size=len(books))
    fig, ax = plt.subplots()
    ax.pie(progress, labels=[book["title"] for book in books], autopct='%1.1f%%', startangle=140)
    ax.set_title("Your Reading Progress")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")

