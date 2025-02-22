import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import date

# App Title
st.set_page_config(page_title="Book Lovers Hub", page_icon="📚")
st.title("📚 Welcome to Book Lovers Hub")

# Sidebar Navigation
st.sidebar.header("📌 Navigate")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Reading Tracker", "📚 Book Reviews", "📜 Quotes & Wisdom",
    "📝 Writing Corner", "📊 Genre Popularity", "🎯 Reading Goals", "🧠 Fun Book Facts"
])

# Home Page
if page == "🏡 Home":
    st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794", use_container_width=True)
    st.header("Discover, Track, and Love Books More Than Ever! 📖")
    
    st.markdown("""
    ### Why Join the Book Lovers Hub?
    ✅ **Track Your Reading Progress** – Stay on top of your book list.  
    ✅ **Write & Share Reviews** – Help others find great books.  
    ✅ **Daily Literary Wisdom** – Get inspired with bookish quotes.  
    ✅ **Set & Achieve Reading Goals** – Push yourself to read more.  
    """)
    
    st.success("📖 Start your reading journey today!")

# Reading Tracker
elif page == "📖 Reading Tracker":
    st.header("📖 Track Your Reading Progress")
    books = ["Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Fantasy"]
    for book in books:
        st.checkbox(f"Finished a {book} book this week?")
    
    if st.button("Update Progress"):
        st.success("Great job! Keep up the reading streak!")
        st.balloons()
    
    # Weekly Reading Progress Graph
    progress = {book: random.randint(0, 7) for book in books}
    fig, ax = plt.subplots()
    ax.bar(progress.keys(), progress.values(), color=["#FF5733", "#33FF57", "#3357FF", "#F39C12", "#9B59B6"])
    ax.set_title("Weekly Reading Progress")
    ax.set_ylabel("Books Finished")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Book Reviews
elif page == "📚 Book Reviews":
    st.header("📚 Share & Read Book Reviews")
    book_name = st.text_input("Enter Book Name:")
    review = st.text_area("Write your review:")
    if st.button("Submit Review"):
        st.success("Review submitted successfully!")
    
    # Review Sentiment Pie Chart
    fig, ax = plt.subplots()
    sizes = [70, 20, 10]
    labels = ["Positive Reviews", "Neutral", "Negative"]
    colors = ["green", "yellow", "red"]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Quotes & Wisdom
elif page == "📜 Quotes & Wisdom":
    st.header("📜 Daily Literary Wisdom")
    quotes = [
        "A reader lives a thousand lives before he dies. - George R.R. Martin",
        "So many books, so little time. - Frank Zappa",
        "Books are a uniquely portable magic. - Stephen King",
        "Reading is essential for those who seek to rise above the ordinary. - Jim Rohn"
    ]
    st.success(f"💡 **Today's Quote:** {random.choice(quotes)}")
    
    # Reading vs. Screen Time Graph
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    reading_time = np.random.randint(30, 90, size=7)
    screen_time = np.random.randint(60, 120, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, reading_time, marker='o', linestyle='-', color='blue', label='Reading Time (min)')
    ax.plot(days, screen_time, marker='s', linestyle='--', color='red', label='Screen Time (min)')
    ax.set_title("Reading vs. Screen Time")
    ax.legend()
    st.pyplot(fig)

# Writing Corner
elif page == "📝 Writing Corner":
    st.header("📝 Express Your Thoughts")
    story = st.text_area("Write a short story or book idea:")
    if st.button("Submit Story"):
        st.success("Story saved! Keep writing!")
    
    # Word Count Bar Chart
    word_counts = {"Short Story": 500, "Article": 1000, "Novel": 30000}
    fig, ax = plt.subplots()
    ax.bar(word_counts.keys(), word_counts.values(), color=["#3498DB", "#E74C3C", "#2ECC71"])
    ax.set_title("Word Count Estimates")
    ax.set_ylabel("Words")
    st.pyplot(fig)

# Genre Popularity
elif page == "📊 Genre Popularity":
    st.header("📊 Popular Book Genres")
    genres = ["Mystery", "Fantasy", "Romance", "Sci-Fi", "Non-Fiction"]
    popularity = np.random.randint(40, 100, size=5)
    fig, ax = plt.subplots()
    ax.barh(genres, popularity, color="purple")
    ax.set_title("Popularity of Genres")
    ax.set_xlabel("Popularity Score")
    st.pyplot(fig)

# Reading Goals
elif page == "🎯 Reading Goals":
    st.header("🎯 Set Your Reading Goals")
    goal = st.text_input("Enter your reading goal (e.g., 50 books a year):")
    if goal:
        st.write(f"Your Goal: {goal}")
    if st.button("Save Goal"):
        st.success("Goal saved successfully!")

# Fun Book Facts
elif page == "🧠 Fun Book Facts":
    st.header("🧠 Did You Know?")
    facts = [
        "📖 The world's largest book is 5 meters wide!",
        "📚 There are over 129 million books in existence.",
        "🧐 The most expensive book ever sold cost $30.8 million!",
        "📙 The longest novel ever written has over 4 million words."
    ]
    st.info(random.choice(facts))
    
    # Fun Fact Graph - Book Lengths
    book_lengths = {"Novella": 25000, "Novel": 80000, "Epic Novel": 200000}
    fig, ax = plt.subplots()
    ax.bar(book_lengths.keys(), book_lengths.values(), color=["#D35400", "#8E44AD", "#2980B9"])
    ax.set_title("Average Book Lengths")
    ax.set_ylabel("Words")
    st.pyplot(fig)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Book Lovers Hub")
