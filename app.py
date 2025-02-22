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
    st.session_state.page = "📖 Reading"
else:
    st.session_state.page = st.sidebar.radio("Go to:", [
        "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights", "📅 Set Your Vision",
        "🏆 Personal Growth Challenges", "💡 Daily Productivity Tips", "🌍 Community Forum"
    ])

# Book Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "image_url": "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg", "category": "Self-Improvement", "description": "A practical guide to building good habits and breaking bad ones."},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71zytzrg6lL.jpg", "category": "Productivity", "description": "Discover the morning routine that can change your life."},
    {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "image_url": "https://bukharibooks.com/wp-content/uploads/2019/07/mindset-2.png", "category": "Psychology", "description": "Understand how a growth mindset leads to success."}
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
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(book["image_url"], width=120)
            with col2:
                st.subheader(book["title"])
                st.write(f"**Author:** {book['author']}")
                st.write(f"📖 {book['description']}")

# Personal Growth Challenges Page
elif st.session_state.page == "🏆 Personal Growth Challenges":
    st.header("🏆 Personal Growth Challenges")
    st.write("Push your limits with these challenges!")
    challenges = ["Read a book in 7 days", "Practice gratitude daily", "Eliminate distractions for 48 hours"]
    for challenge in challenges:
        st.checkbox(challenge)

# Daily Productivity Tips Page
elif st.session_state.page == "💡 Daily Productivity Tips":
    st.header("💡 Daily Productivity Tips")
    tips = [
        "Start your day with a clear goal",
        "Take short breaks to boost focus",
        "Avoid multitasking for better efficiency"
    ]
    st.write(np.random.choice(tips))

# Community Forum Page
elif st.session_state.page == "🌍 Community Forum":
    st.header("🌍 Community Forum")
    st.text_area("Share your thoughts with the community:")
    if st.button("Post"):
        st.success("Your post has been shared!")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")


