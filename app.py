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
        background-color: #FAF3E0;
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
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.title("📚 BookWorm's Haven")
page = st.sidebar.radio("Explore:", ["Home", "Reading Challenge", "Book Discovery", "Literary Quotes", "Reading Stats"])

# Home Page
if page == "Home":
    st.title("📖 Welcome to BookWorm's Haven")
    st.subheader("Your Personal Library & Reading Companion")
    
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
        st.image(current_book["cover"], width=150)
        st.write(f"**{current_book['title']}**")
        st.write(f"By {current_book['author']}")
        st.progress(current_book['progress'])
        st.write(f"{current_book['progress']}% completed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.subheader("📊 Quick Stats")
        col_x, col_y, col_z = st.columns(3)
        books_read = random.randint(20, 40)
        col_x.metric("Books Read", books_read, f"+{random.randint(1, 3)} this month")
        col_y.metric("Pages Read", books_read * random.randint(200, 400), f"+{random.randint(50, 200)} this week")
        col_z.metric("Reading Streak", f"{random.randint(5, 30)} days", f"+{random.randint(1, 7)} days")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.subheader("✨ Recommended Reads")
    next_books = [
        {"title": "Dune", "author": "Frank Herbert", "cover": "https://images-na.ssl-images-amazon.com/images/I/81ym3QUd3KL.jpg"},
        {"title": "Project Hail Mary", "author": "Andy Weir", "cover": "https://images-na.ssl-images-amazon.com/images/I/91Bd7P8UwxL.jpg"}
    ]
    col_a, col_b = st.columns(2)
    for i, book in enumerate(next_books):
        with [col_a, col_b][i]:
            st.image(book["cover"], width=120)
            st.write(f"**{book['title']}**")
            st.write(f"By {book['author']}")
    st.markdown('</div>', unsafe_allow_html=True)

# Other pages remain unchanged

# Footer
st.markdown("---")
st.markdown("📚 Dive into new worlds, one page at a time. © 2025 BookWorm's Haven")



