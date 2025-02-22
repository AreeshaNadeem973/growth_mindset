import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Motivational Book Hub", page_icon="📚")
st.title("📚 Welcome to Motivational Book Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Book Collection", "📊 Reading Progress", "📝 Reviews & Thoughts", "📅 Reading Goals"
])

# Home Page
if page == "🏡 Home":
    st.header("📚 Welcome to Motivational Book Hub")
    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", use_container_width=True)  # Updated Image Size
    st.markdown("""
    ### Explore & Grow with Motivational Books!
    ✅ **Read Life-Changing Books** 📖  
    ✅ **Track Your Reading Progress** 📊  
    ✅ **Share Your Thoughts & Reviews** 📝  
    """)
    st.success("Start your journey to success today! 🚀")

# Book Collection Page
elif page == "📖 Book Collection":
    st.header("📚 Explore Motivational Books")
    books = [
        {"title": "Atomic Habits", "url": "https://example.com/atomic-habits", "image": "https://images.pexels.com/photos/1005324/pexels-photo-1005324.jpeg"},
        {"title": "The 5 AM Club", "url": "https://example.com/5am-club", "image": "https://images.pexels.com/photos/1261730/pexels-photo-1261730.jpeg"},
        {"title": "The Power of Now", "url": "https://example.com/power-of-now", "image": "https://images.pexels.com/photos/46274/books-education-school-literature-46274.jpeg"},
        {"title": "Think and Grow Rich", "url": "https://example.com/think-grow-rich", "image": "https://images.pexels.com/photos/159866/books-bookstore-book-reading-159866.jpeg"},
        {"title": "Awaken The Giant Within", "url": "https://example.com/awaken-giant", "image": "https://images.pexels.com/photos/2918514/pexels-photo-2918514.jpeg"},
        {"title": "The Magic of Thinking Big", "url": "https://example.com/magic-thinking-big", "image": "https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg"}
    ]
    
    cols = st.columns(2)
    for index, book in enumerate(books):
        with cols[index % 2]:
            st.image(book["image"], use_container_width=True)
            if st.button(f"📖 Read {book['title']}", key=book['title']):
                st.session_state["selected_book"] = book
                st.experimental_rerun()

# Dynamic Book Reading Page
if "selected_book" in st.session_state:
    book = st.session_state["selected_book"]
    st.header(f"📖 {book['title']}")
    st.image(book["image"], use_container_width=True)
    st.markdown(f"[Read Now]({book['url']})")
    if st.button("🔙 Back to Collection"):
        del st.session_state["selected_book"]
        st.experimental_rerun()

# Reading Progress Page
elif page == "📊 Reading Progress":
    st.header("📊 Track Your Reading Progress")
    books = ["Atomic Habits", "The 5 AM Club", "The Power of Now", "Think and Grow Rich"]
    progress = np.random.randint(0, 100, size=len(books))
    fig, ax = plt.subplots()
    ax.barh(books, progress, color=['#FF5733', '#33FF57', '#3357FF', '#F3FF33'])
    ax.set_title("Reading Progress (%)")
    ax.set_xlabel("Completion %")
    st.pyplot(fig)

# Reviews & Thoughts Page
elif page == "📝 Reviews & Thoughts":
    st.header("📝 Share Your Thoughts on Books")
    book = st.selectbox("Select a Book", ["Atomic Habits", "The 5 AM Club", "The Power of Now", "Think and Grow Rich"])
    review = st.text_area("Write your review:")
    if st.button("Submit Review"):
        st.success("Review submitted successfully!")

# Reading Goals Page
elif page == "📅 Reading Goals":
    st.header("📅 Set Your Reading Goals")
    goal = st.text_input("Your Reading Goal:")
    if st.button("Save Goal"):
        st.success("Goal saved successfully! Keep reading!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Motivational Book Hub")
