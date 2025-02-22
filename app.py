import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# App Title and Configuration
st.set_page_config(page_title="BookWorm's Learning Journey", page_icon="📚", layout="wide")
st.title("📚 BookWorm's Learning Journey")

# Custom CSS for improved design
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f3e7e9, #e3eeff);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.title("📖 Navigation")
page = st.sidebar.radio("Explore:", ["Home", "Reading List", "Book Notes", "Learning Tracker", "Book Recommendations"])

# Home Page
if page == "Home":
    st.header("Welcome, Book Lover! 🎉")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Your Reading Stats")
        books_read = random.randint(5, 20)
        pages_read = books_read * random.randint(200, 400)
        hours_read = books_read * random.randint(3, 8)
        
        st.metric("Books Read", books_read, f"+{random.randint(1, 3)} this month")
        st.metric("Pages Conquered", pages_read, f"+{random.randint(50, 200)} this week")
        st.metric("Hours of Reading", hours_read, f"+{random.randint(2, 10)} this week")
        
        st.subheader("🎯 Reading Goal")
        goal = 52  # books per year
        progress = (books_read / goal) * 100
        st.progress(progress)
        st.write(f"You've read {books_read} out of {goal} books this year!")
    
    with col2:
        st.subheader("📈 Reading Trend")
        dates = pd.date_range(end=datetime.now(), periods=30).strftime("%d %b").tolist()
        pages = [random.randint(10, 100) for _ in range(30)]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(dates, pages, marker='o', linestyle='-', linewidth=2, markersize=6, color='#FF6B6B')
        ax.set_title("Pages Read Daily", fontsize=16)
        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Pages", fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.fill_between(dates, pages, color='#FF9999', alpha=0.3)
        st.pyplot(fig)

# Reading List Page
elif page == "Reading List":
    st.header("📚 Your Reading Adventure")
    
    st.subheader("Add a New Book")
    col1, col2 = st.columns(2)
    with col1:
        new_book = st.text_input("Book Title")
        new_author = st.text_input("Author")
    with col2:
        new_genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science", "Biography", "Self-Help", "Other"])
        new_pages = st.number_input("Number of Pages", min_value=1, value=200)
    
    if st.button("Add to Reading List"):
        st.success(f"'{new_book}' by {new_author} added to your reading list!")
    
    st.subheader("Your Current Reading List")
    books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "pages": 281, "progress": 65},
        {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction", "pages": 197, "progress": 100},
        {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "Non-Fiction", "pages": 443, "progress": 30},
        {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help", "pages": 320, "progress": 50}
    ]
    
    for book in books:
        col1, col2, col3 = st.columns([3, 1, 1])
        col1.write(f"**{book['title']}** by {book['author']}")
        col2.write(f"{book['genre']} | {book['pages']} pages")
        col3.progress(book['progress'])
    
    st.subheader("📊 Books by Genre")
    genres = ["Fiction", "Non-Fiction", "Science", "Biography", "Self-Help", "Other"]
    book_counts = [random.randint(1, 10) for _ in genres]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(book_counts, labels=genres, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1(np.linspace(0, 1, 6)))
    ax.axis('equal')
    plt.title("Your Reading Diversity", fontsize=16)
    st.pyplot(fig)

# Book Notes Page
elif page == "Book Notes":
    st.header("📝 Capture Your Insights")
    
    st.subheader("Add New Notes")
    note_book = st.selectbox("Select Book", ["To Kill a Mockingbird", "The Alchemist", "Sapiens", "Atomic Habits"])
    note_page = st.number_input("Page Number", min_value=1, value=1)
    note_content = st.text_area("Your Notes")
    
    if st.button("Save Note"):
        st.success(f"Note saved for '{note_book}' on page {note_page}")
    
    st.subheader("Your Recent Notes")
    notes = [
        {"book": "Atomic Habits", "page": 42, "note": "Four laws of behavior change: make it obvious, attractive, easy, and satisfying."},
        {"book": "Sapiens", "page": 115, "note": "Agriculture was history's biggest fraud. It led to harder work and worse nutrition for most people."},
        {"book": "To Kill a Mockingbird", "page": 87, "note": "Atticus Finch: 'You never really understand a person until you consider things from his point of view.'"}
    ]
    
    for note in notes:
        st.markdown(f"**{note['book']}** (Page {note['page']})")
        st.info(note['note'])
        st.markdown("---")
    
    st.subheader("📊 Notes Distribution")
    books = ["To Kill a Mockingbird", "The Alchemist", "Sapiens", "Atomic Habits"]
    note_counts = [random.randint(5, 20) for _ in books]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(books, note_counts, color=plt.cm.Accent(np.linspace(0, 1, 4)))
    ax.set_ylabel("Number of Notes")
    ax.set_title("Notes Taken per Book")
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}', ha='center', va='bottom')
    
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

# Learning Tracker Page
elif page == "Learning Tracker":
    st.header("🧠 Track Your Learning Journey")
    
    st.subheader("Log Your Learning")
    learn_date = st.date_input("Date", datetime.now())
    learn_book = st.selectbox("Book", ["To Kill a Mockingbird", "The Alchemist", "Sapiens", "Atomic Habits"])
    learn_topic = st.text_input("What did you learn?")
    learn_application = st.text_area("How can you apply this knowledge?")
    
    if st.button("Log Learning"):
        st.success(f"Learning from '{learn_book}' logged successfully!")
    
    st.subheader("Your Learning Streak")
    dates = pd.date_range(end=datetime.now(), periods=30)
    learnings = [random.choice([0, 1]) for _ in range(30)]  # 0 for no learning, 1 for learning
    
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.imshow([learnings], cmap="YlGn", aspect="auto")
    ax.set_xticks(range(len(dates)))
    ax.set_xticklabels(dates.strftime("%d %b"), rotation=90)
    ax.set_yticks([])
    
    for i, learning in enumerate(learnings):
        ax.text(i, 0, "📚" if learning else "❌", ha="center", va="center")
    
    plt.title("30-Day Learning Streak")
    st.pyplot(fig)
    
    current_streak = len(list(takewhile(lambda x: x == 1, reversed(learnings))))
    st.metric("Current Learning Streak", f"{current_streak} days", f"+{current_streak}")
    
    st.subheader("📊 Learning Topics Word Cloud")
    from wordcloud import WordCloud
    
    topics = "learning reading books knowledge growth mindset education literature fiction non-fiction self-improvement curiosity wisdom insights comprehension analysis critical-thinking vocabulary imagination empathy perspective"
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(topics)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

# Book Recommendations Page
elif page == "Book Recommendations":
    st.header("📚 Discover Your Next Great Read")
    
    st.subheader("What are you in the mood for?")
    mood = st.select_slider("Select your reading mood:", options=["Relaxing", "Inspiring", "Thrilling", "Educational", "Mind-bending"])
    genre_preference = st.multiselect("Select preferred genres:", ["Fiction", "Non-Fiction", "Mystery", "Science Fiction", "Biography", "Self-Help"])
    
    if st.button("Get Recommendations"):
        st.success("Based on your preferences, here are some books you might enjoy:")
        
        recommendations = [
            {"title": "The Midnight Library", "author": "Matt Haig", "genre": "Fiction"},
            {"title": "Educated", "author": "Tara Westover", "genre": "Biography"},
            {"title": "The Silent Patient", "author": "Alex Michaelides", "genre": "Mystery"},
            {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "genre": "Non-Fiction"},
            {"title": "Project Hail Mary", "author": "Andy Weir", "genre": "Science Fiction"}
        ]
        
        for book in recommendations:
            st.markdown(f"**{book['title']}** by {book['author']} - *{book['genre']}*")
    
    st.subheader("📊 Popular Books This Month")
    books = ["The Midnight Library", "Atomic Habits", "Where the Crawdads Sing", "Educated", "The Silent Patient"]
    ratings = [random.uniform(4.0, 5.0) for _ in books]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(books, ratings, color=plt.cm.Spectral(np.linspace(0, 1, 5)))
    ax.set_xlim(0, 5)
    ax.set_xlabel("Average Rating")
    ax.set_title("Top Rated Books This Month")
    
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, f'{ratings[i]:.2f}', 
                ha='left', va='center')
    
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("📚 Expand your mind, one book at a time. © 2023 BookWorm's Learning Journey")




