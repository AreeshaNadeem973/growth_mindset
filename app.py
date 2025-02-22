import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Motivational Books Hub", page_icon="📚")
st.title("📚 Motivational Books Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Book Collection", "📊 Reading Progress", "💡 Daily Inspiration", "🎯 Reading Challenges"
])

# Sample Books Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "image": "https://m.media-amazon.com/images/I/81wgcld4wxL.jpg", "link": "https://www.amazon.com/dp/0735211299"},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "image": "https://m.media-amazon.com/images/I/71ZY0tB-aBL.jpg", "link": "https://www.amazon.com/dp/1443456624"},
    {"title": "Can't Hurt Me", "author": "David Goggins", "image": "https://m.media-amazon.com/images/I/61IJiYp9RAL.jpg", "link": "https://www.amazon.com/dp/1544507852"},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "image": "https://m.media-amazon.com/images/I/71mHaU4VwFL.jpg", "link": "https://www.amazon.com/dp/1577314808"}
]

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Motivational Reading Hub! 📖✨")
    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", use_container_width=True)
    st.markdown("""
    ### Explore, Learn, and Stay Inspired!
    ✅ **Discover top motivational books** 📚  
    ✅ **Track your reading progress** 📊  
    ✅ **Daily quotes to keep you inspired** 💡  
    ✅ **Set reading goals and take on challenges** 🎯  
    """)
    st.success("Start your journey today! 🚀")

# Book Collection Page
elif page == "📖 Book Collection":
    st.header("📖 Explore Motivational Books")
    cols = st.columns(2)
    for idx, book in enumerate(books):
        with cols[idx % 2]:
            st.image(book['image'], width=150)
            st.write(f"**{book['title']}** by {book['author']}")
            if st.button(f"📖 Read {book['title']}", key=book['title']):
                st.markdown(f"[Read Now]({book['link']})")

# Reading Progress Page
elif page == "📊 Reading Progress":
    st.header("📊 Track Your Reading Progress")
    pages_read = st.slider("How many pages have you read today?", 0, 300, 50)
    st.write(f"You've read **{pages_read} pages** today! Keep going! 📖")
    
    # Generate Random Weekly Progress Data
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    progress = np.random.randint(10, 50, size=7)
    
    fig, ax = plt.subplots()
    ax.bar(days, progress, color=['blue', 'green', 'orange', 'red', 'purple', 'yellow', 'cyan'])
    ax.set_title("Weekly Reading Progress")
    ax.set_ylabel("Pages Read")
    ax.set_ylim(0, 50)
    st.pyplot(fig)

# Daily Inspiration Page
elif page == "💡 Daily Inspiration":
    st.header("💡 Daily Book Wisdom")
    quotes = [
        "A reader lives a thousand lives before he dies. - George R.R. Martin",
        "The more that you read, the more things you will know. - Dr. Seuss",
        "Reading is essential for those who seek to rise above the ordinary. - Jim Rohn",
        "Once you learn to read, you will be forever free. - Frederick Douglass"
    ]
    st.success(f"📖 **Quote of the Day:** {np.random.choice(quotes)}")

# Reading Challenges Page
elif page == "🎯 Reading Challenges":
    st.header("🎯 Set and Achieve Reading Goals!")
    goal_pages = st.number_input("Set your daily reading goal (pages):", min_value=10, max_value=300, value=50)
    completed_pages = st.number_input("Pages you read today:", min_value=0, max_value=300, value=0)
    
    # Pie Chart for Progress
    fig, ax = plt.subplots()
    ax.pie([completed_pages, max(0, goal_pages - completed_pages)], labels=["Read", "Remaining"], autopct='%1.1f%%', colors=["green", "gray"])
    ax.set_title("Reading Goal Progress")
    st.pyplot(fig)
    
    if completed_pages >= goal_pages:
        st.success("🎉 Congrats! You've met your goal today!")
    else:
        st.warning("Keep going! You're getting closer to your goal!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Motivational Books Hub")
