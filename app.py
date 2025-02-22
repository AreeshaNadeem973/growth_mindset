import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Next-Gen Power", page_icon="🚀")
st.title("Next-Gen Power: Mindset, Innovation & Success")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
st.session_state.page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey",
    "📝 Share Your Insights", "📅 Set Your Vision", "🔥 Daily Challenges",
    "🎥 Video Recommendations"
])

# Book Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "image_url": "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg", "category": "Self-Improvement", "description": "A practical guide to building good habits and breaking bad ones."},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71zytzrg6lL.jpg", "category": "Productivity", "description": "Discover the morning routine that can change your life."}
]
book_titles = [book["title"] for book in books]
categories = list(set(book["category"] for book in books))

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

# Book Collection Page
elif st.session_state.page == "📚 Transform Your Mindset":
    st.header("📚 Transform Your Mindset with Powerful Reads")
    selected_category = st.selectbox("Choose a Category:", ["All"] + categories)
    filtered_books = books if selected_category == "All" else [book for book in books if book["category"] == selected_category]
    for book in filtered_books:
        st.image(book["image_url"], width=120)
        st.subheader(book["title"])
        st.write(f"**Author:** {book['author']}")
        st.write(f"**Category:** {book['category']}")
        st.write(f"📖 {book['description']}")
        if st.button(f"📖 Read More", key=book['title']):
            st.session_state.current_book = book
            st.session_state.page = "📖 Reading"
            st.rerun()

# Growth Journey Page
elif st.session_state.page == "📊 Your Growth Journey":
    st.header("📊 Your Growth Journey")
    progress = np.random.randint(0, 100, size=len(book_titles))
    fig, ax = plt.subplots()
    ax.pie(progress, labels=book_titles, autopct='%1.1f%%', startangle=140)
    ax.set_title("Your Reading Progress")
    st.pyplot(fig)

# Share Your Insights Page
elif st.session_state.page == "📝 Share Your Insights":
    st.header("📝 Share Your Insights & Reflections")
    book = st.selectbox("Select a Book", book_titles)
    review = st.text_area("What did you learn?")
    if st.button("Submit Your Reflection"):
        st.success("Your thoughts have been saved!")

# Vision & Goals Page
elif st.session_state.page == "📅 Set Your Vision":
    st.header("📅 Set Your Vision for Success")
    goal = st.text_input("What’s your next goal?")
    if st.button("Save Your Goal"):
        st.success("Your vision is now set! Keep growing!")

# Daily Challenges Page
elif st.session_state.page == "🔥 Daily Challenges":
    st.header("🔥 Your Daily Challenge")
    challenges = [
        "Wake up 30 minutes earlier than usual.",
        "Write down three things you’re grateful for.",
        "Read for 20 minutes today.",
        "Take a 10-minute mindfulness break.",
        "Do one small act of kindness."
    ]
    st.success(random.choice(challenges))

# Video Recommendations Page
elif st.session_state.page == "🎥 Video Recommendations":
    st.header("🎥 Watch & Learn")
    videos = {
        "The Power of Habit": "https://www.youtube.com/watch?v=OMbsGBlpP30",
        "Morning Routine for Success": "https://www.youtube.com/watch?v=2KufeZmEvXo",
        "Growth Mindset Explained": "https://www.youtube.com/watch?v=KUWn_TJTrnU"
    }
    for title, url in videos.items():
        st.subheader(title)
        st.video(url)

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")
