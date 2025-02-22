import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Motivational Books Hub", page_icon="📚")
st.title("📚 Welcome to Motivational Books Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Book Categories", "📚 Top Motivational Books", "📊 Reading Progress",
    "📝 Daily Book Quotes", "🎯 Reading Challenges", "🧠 Brain-Boosting Reads"
])

# Home Page
if page == "🏡 Home":
    st.header("🚀 Ignite Your Motivation Through Books!")
    st.image("https://images.pexels.com/photos/417062/pexels-photo-417062.jpeg", use_container_width=True)
    st.markdown("""
    ### Why Read Motivational Books?
    ✅ **Gain Inspiration** – Learn from the best minds.  
    ✅ **Develop Success Habits** – Transform your mindset.  
    ✅ **Improve Productivity** – Apply life-changing principles.  
    ✅ **Stay Focused** – Achieve your dreams with powerful insights!  
    """)
    st.success("Start your reading journey today! 🚀")

# Book Categories
elif page == "📖 Book Categories":
    st.header("📖 Explore Different Motivational Book Genres")
    categories = ["Self-Help", "Business & Success", "Mindset & Growth", "Biographies", "Spiritual & Well-being"]
    selected_category = st.selectbox("Choose a category:", categories)
    
    books = {
        "Self-Help": ["Atomic Habits", "The 5 AM Club"],
        "Business & Success": ["Rich Dad Poor Dad", "The Lean Startup"],
        "Mindset & Growth": ["Mindset: The New Psychology of Success", "Grit"],
        "Biographies": ["Steve Jobs", "Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future"],
        "Spiritual & Well-being": ["The Power of Now", "The Untethered Soul"]
    }
    
    st.write("📚 Recommended Books:")
    for book in books[selected_category]:
        st.write(f"- {book}")

# Top Motivational Books
elif page == "📚 Top Motivational Books":
    st.header("🌟 Must-Read Motivational Books")
    st.write("Here are some of the best books to inspire and empower you:")
    books = [
        "Atomic Habits - James Clear",
        "The 7 Habits of Highly Effective People - Stephen Covey",
        "The Power of Now - Eckhart Tolle",
        "Think and Grow Rich - Napoleon Hill",
        "The Magic of Thinking Big - David J. Schwartz"
    ]
    for book in books:
        st.markdown(f"📖 **{book}**")

# Reading Progress Graph
elif page == "📊 Reading Progress":
    st.header("📊 Track Your Reading Progress")
    books = ["Atomic Habits", "The 7 Habits", "The Power of Now", "Think & Grow Rich"]
    progress = np.random.randint(20, 100, size=len(books))
    fig, ax = plt.subplots()
    ax.barh(books, progress, color=['#FF5733', '#33FF57', '#3357FF', '#F3FF33'])
    ax.set_xlabel("Reading Progress (%)")
    ax.set_title("Your Book Completion Progress")
    st.pyplot(fig)

# Daily Book Quotes
elif page == "📝 Daily Book Quotes":
    st.header("📜 Inspirational Quotes from Motivational Books")
    quotes = [
        "The secret of getting ahead is getting started. – Mark Twain",
        "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
        "Do what you can, with what you have, where you are. – Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill"
    ]
    st.success(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Reading Challenges
elif page == "🎯 Reading Challenges":
    st.header("🎯 Set Your Reading Challenge")
    target_books = st.number_input("How many books do you aim to read this month?", min_value=1, max_value=20, value=4)
    completed_books = st.slider("Books Completed So Far", 0, target_books, 0)
    
    fig, ax = plt.subplots()
    ax.pie([completed_books, target_books - completed_books], labels=["Completed", "Remaining"], autopct='%1.1f%%', colors=['#4CAF50', '#FFC107'])
    ax.set_title("Your Reading Challenge Progress")
    st.pyplot(fig)

    if completed_books >= target_books:
        st.success("Congratulations! You've achieved your reading goal! 🎉")
    else:
        st.info(f"Keep going! {target_books - completed_books} books left to reach your goal! 📚")

# Brain-Boosting Reads
elif page == "🧠 Brain-Boosting Reads":
    st.header("🧠 Books to Sharpen Your Mind")
    books = [
        "Deep Work - Cal Newport",
        "The Art of Thinking Clearly - Rolf Dobelli",
        "A Mind for Numbers - Barbara Oakley",
        "Super Thinking - Gabriel Weinberg & Lauren McCann"
    ]
    for book in books:
        st.markdown(f"📖 **{book}**")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Motivational Books Hub")
