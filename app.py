import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Book Lovers Hub", page_icon="📚")
st.title("📚 Welcome to Book Lovers Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Book Reviews", "📚 Reading Tracker", "📅 Book Goals", "📝 Writing Corner", "📊 Reading Stats"
])

# Home Page
if page == "🏡 Home":
    st.header("Discover, Read, and Share Your Love for Books! 📖")
    st.image("https://images.pexels.com/photos/159866/books-bookstore-book-reading-159866.jpeg", width=300)
    
    st.markdown("""
    ### Why Join Book Lovers Hub?
    ✅ **Explore New Books**: Find and review amazing books.  
    ✅ **Track Your Reading**: Keep a log of books you've read.  
    ✅ **Set Book Goals**: Challenge yourself to read more.  
    ✅ **Join the Community**: Share thoughts and reviews.  
    """)
    st.success("Start your reading journey today! 📖✨")

# Book Reviews Page
elif page == "📖 Book Reviews":
    st.header("📖 Book Reviews")
    books = ["Atomic Habits", "The Alchemist", "Deep Work", "Sapiens"]
    selected_book = st.selectbox("Choose a book to review:", books)
    review = st.text_area("Write your review here:")
    if st.button("Submit Review"):
        st.success(f"Thank you for reviewing {selected_book}!")

# Reading Tracker Page
elif page == "📚 Reading Tracker":
    st.header("📚 Track Your Reading Progress")
    books = ["The Power of Habit", "Thinking, Fast and Slow", "1984", "The 5 AM Club"]
    progress = {book: random.randint(10, 100) for book in books}
    
    fig, ax = plt.subplots()
    ax.bar(progress.keys(), progress.values(), color=['red', 'blue', 'green', 'purple'])
    ax.set_title("Reading Progress (%)")
    ax.set_ylabel("Completion")
    st.pyplot(fig)

# Book Goals Page
elif page == "📅 Book Goals":
    st.header("📅 Set Your Reading Goals")
    goal = st.text_input("How many books do you want to read this year?")
    if goal:
        st.write(f"📚 Your Target: {goal} books this year!")
    
    if st.button("Save Goal"):
        st.success("Goal saved successfully! Keep reading!")

# Writing Corner Page
elif page == "📝 Writing Corner":
    st.header("📝 Express Yourself Through Writing")
    story = st.text_area("Start writing your story or book idea:")
    if st.button("Save Story"):
        st.success("Story saved! Keep writing and creating!")
    
# Reading Stats Page
elif page == "📊 Reading Stats":
    st.header("📊 Your Reading Statistics")
    
    books_read = np.random.randint(5, 50, size=12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    fig, ax = plt.subplots()
    ax.plot(months, books_read, marker='o', linestyle='-', color='blue')
    ax.set_title("Books Read Over the Year")
    ax.set_ylabel("Books Read")
    ax.set_xlabel("Months")
    st.pyplot(fig)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Book Lovers Hub")
