import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# App Title and Configuration
st.set_page_config(page_title="BookWorm's Haven", page_icon="📚", layout="wide")

# Custom CSS for improved design
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-attachment: fixed;
        background-size: cover;
    }
    .stButton>button {
        background-color: #1E3F5A;
        color: white;
        border-radius: 20px;
        border: 2px solid #FFD700;
    }
    .stTextInput>div>div>input {
        border-radius: 20px;
    }
    .book-cover {
        width: 120px;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .content-box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.title("📚 BookWorm's Haven")
page = st.sidebar.radio("Explore:", ["Home", "Reading Challenge", "Book Discovery", "Literary Quotes", "Reading Stats"])

# Home Page
if page == "Home":
    st.title("📚 Welcome to BookWorm's Haven")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("📖 Currently Reading")
        current_book = {
            "title": "The Midnight Library",
            "author": "Matt Haig",
            "progress": 65,
            "cover": "https://images-na.ssl-images-amazon.com/images/I/81YzHKeWq7L.jpg"
        }
        col_a, col_b = st.columns([1, 3])
        with col_a:
            st.image(current_book["cover"], use_column_width=True, caption="Book Cover")
        with col_b:
            st.write(f"**{current_book['title']}**")
            st.write(f"By {current_book['author']}")
            st.progress(current_book['progress'])
            st.write(f"{current_book['progress']}% completed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("🎯 Reading Challenge")
        goal = 52  # books per year
        books_read = random.randint(20, 40)
        progress = (books_read / goal) * 100
        st.progress(progress)
        st.write(f"You've read {books_read} out of {goal} books this year!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("📊 Quick Stats")
        col_x, col_y, col_z = st.columns(3)
        col_x.metric("Books Read", books_read, f"+{random.randint(1, 3)} this month")
        col_y.metric("Pages Read", books_read * random.randint(200, 400), f"+{random.randint(50, 200)} this week")
        col_z.metric("Reading Streak", f"{random.randint(5, 30)} days", f"+{random.randint(1, 7)} days")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("📚 Next in Queue")
        next_books = [
            {"title": "Dune", "author": "Frank Herbert", "cover": "https://images-na.ssl-images-amazon.com/images/I/81ym3QUd3KL.jpg"},
            {"title": "Project Hail Mary", "author": "Andy Weir", "cover": "https://images-na.ssl-images-amazon.com/images/I/91Bd7P8UwxL.jpg"}
        ]
        for book in next_books:
            st.image(book["cover"], width=100, caption=f"{book['title']} by {book['author']}")
        st.markdown('</div>', unsafe_allow_html=True)

# Reading Challenge Page
elif page == "Reading Challenge":
    st.title("🎯 Reading Challenge")
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Set Your Reading Goal")
    goal = st.number_input("How many books do you want to read this year?", min_value=1, value=52)
    if st.button("Set Goal"):
        st.success(f"Great! Your goal is set to read {goal} books this year.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Your Progress")
    books_read = random.randint(20, 40)
    progress = (books_read / goal) * 100
    st.progress(progress)
    st.write(f"You've read {books_read} out of {goal} books!")
    
    # Create a colorful bar chart for monthly progress
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    books_per_month = [random.randint(1, 8) for _ in range(12)]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(months, books_per_month, color=plt.cm.viridis(np.linspace(0, 1, 12)))
    ax.set_ylabel('Books Read')
    ax.set_title('Monthly Reading Progress')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}', ha='center', va='bottom')
    
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

# Book Discovery Page
elif page == "Book Discovery":
    st.title("🔍 Book Discovery")
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Find Your Next Great Read")
    genre = st.selectbox("Choose a genre:", ["Fiction", "Non-Fiction", "Mystery", "Science Fiction", "Fantasy", "Biography"])
    mood = st.select_slider("Select your reading mood:", options=["Relaxing", "Inspiring", "Thrilling", "Educational", "Mind-bending"])
    
    if st.button("Discover Books"):
        st.success("Based on your preferences, here are some books you might enjoy:")
        
        # Simulated book recommendations
        recommendations = [
            {"title": "The Midnight Library", "author": "Matt Haig", "genre": "Fiction", "cover": "https://images-na.ssl-images-amazon.com/images/I/81YzHKeWq7L.jpg"},
            {"title": "Atomic Habits", "author": "James Clear", "genre": "Non-Fiction", "cover": "https://images-na.ssl-images-amazon.com/images/I/81wgcld4wxL.jpg"},
            {"title": "Project Hail Mary", "author": "Andy Weir", "genre": "Science Fiction", "cover": "https://images-na.ssl-images-amazon.com/images/I/91Bd7P8UwxL.jpg"}
        ]
        
        col1, col2, col3 = st.columns(3)
        for i, book in enumerate(recommendations):
            with [col1, col2, col3][i]:
                st.image(book["cover"], use_column_width=True)
                st.write(f"**{book['title']}**")
                st.write(f"By {book['author']}")
                st.write(f"Genre: {book['genre']}")
    st.markdown('</div>', unsafe_allow_html=True)

# Literary Quotes Page
elif page == "Literary Quotes":
    st.title("💬 Literary Quotes")
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Quote of the Day")
    quotes = [
        {"quote": "It does not do to dwell on dreams and forget to live.", "author": "J.K. Rowling", "book": "Harry Potter and the Sorcerer's Stone"},
        {"quote": "The only way out of the labyrinth of suffering is to forgive.", "author": "John Green", "book": "Looking for Alaska"},
        {"quote": "It was the best of times, it was the worst of times.", "author": "Charles Dickens", "book": "A Tale of Two Cities"}
    ]
    quote = random.choice(quotes)
    st.info(f'"{quote["quote"]}" - {quote["author"]}, {quote["book"]}')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Add Your Favorite Quote")
    new_quote = st.text_area("Enter the quote:")
    new_author = st.text_input("Author:")
    new_book = st.text_input("Book:")
    if st.button("Add Quote"):
        st.success("Your quote has been added to the collection!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Quote Collection")
    for quote in quotes:
        st.write(f'"{quote["quote"]}"')
        st.write(f'- {quote["author"]}, {quote["book"]}')
        st.markdown("---")
    st.markdown('</div>', unsafe_allow_html=True)

# Reading Stats Page
elif page == "Reading Stats":
    st.title("📊 Reading Stats")
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Reading Habits")
    
    # Reading time distribution
    times = ['Morning', 'Afternoon', 'Evening', 'Night']
    percentages = [random.randint(10, 40) for _ in range(4)]
    percentages = [p / sum(percentages) * 100 for p in percentages]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(percentages, labels=times, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1(np.linspace(0, 1, 4)))
    ax.axis('equal')
    plt.title("When Do You Read?")
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Genre Exploration")
    
    # Genre distribution
    genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Sci-Fi', 'Fantasy', 'Biography']
    books_per_genre = [random.randint(1, 20) for _ in genres]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(genres, books_per_genre, color=plt.cm.viridis(np.linspace(0, 1, len(genres))))
    ax.set_ylabel('Books Read')
    ax.set_title('Books Read by Genre')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}', ha='center', va='bottom')
    
    plt.xticks(rotation=45)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("Reading Speed")
    avg_speed = random.randint(200, 400)
    st.metric("Average Reading Speed", f"{avg_speed} words per minute")
    st.info(f"At this rate, you could finish a 300-page book in about {300*250/avg_speed:.1f} hours!")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("📚 Dive into new worlds, one page at a time. © 2023 BookWorm's Haven")





