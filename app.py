import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from datetime import date

# App Title
st.set_page_config(page_title="Book Lovers Hub", page_icon="📚")
st.title("📚 Book Lovers Hub")

# Sidebar Navigation
st.sidebar.header("📌 Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Reading Tracker", "💡 Book Recommendations", "✍️ Write & Share Reviews",
    "📊 Reading Stats", "🎯 Reading Goals", "🤔 Book Quiz", "🔥 Author Spotlights"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Book Lovers Hub! 📖")
    st.image("https://source.unsplash.com/800x400/?books,library", use_container_width=True)
    
    st.markdown("""
    ### Why Join?
    - 📚 Track Your Reading Progress
    - 💡 Discover New Books
    - ✍️ Share Your Reviews
    - 🎯 Set and Achieve Reading Goals
    """)
    st.success("Start your literary journey today! 🚀")

# Reading Tracker
elif page == "📖 Reading Tracker":
    st.header("📖 Track Your Reading Journey")
    books = ["1984", "The Alchemist", "Moby Dick", "Pride and Prejudice"]
    book = st.selectbox("Select the book you're reading:", books)
    progress = st.slider(f"Progress in {book}:", 0, 100, 50)
    if st.button("Update Progress"):
        st.success(f"You've updated your progress in {book} to {progress}%!")
        st.balloons()
    
    # Progress Graph
    progress_data = {b: random.randint(0, 100) for b in books}
    fig, ax = plt.subplots()
    ax.bar(progress_data.keys(), progress_data.values(), color='blue')
    ax.set_title("Reading Progress")
    ax.set_ylabel("% Completed")
    st.pyplot(fig)

# Book Recommendations
elif page == "💡 Book Recommendations":
    st.header("📖 Personalized Book Recommendations")
    genres = ["Fiction", "Self-Help", "Sci-Fi", "Mystery"]
    selected_genre = st.selectbox("Pick a Genre:", genres)
    
    recs = {
        "Fiction": ["The Great Gatsby", "To Kill a Mockingbird"],
        "Self-Help": ["Atomic Habits", "The Power of Now"],
        "Sci-Fi": ["Dune", "Neuromancer"],
        "Mystery": ["Gone Girl", "Sherlock Holmes"]
    }
    st.write(f"📚 Recommended Books for {selected_genre}: {', '.join(recs[selected_genre])}")
    
    # Pie Chart for Popularity
    fig, ax = plt.subplots()
    sizes = [random.randint(10, 40) for _ in recs[selected_genre]]
    ax.pie(sizes, labels=recs[selected_genre], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Write & Share Reviews
elif page == "✍️ Write & Share Reviews":
    st.header("✍️ Write a Book Review")
    book_title = st.text_input("Book Title:")
    review = st.text_area("Write your review:")
    rating = st.slider("Rate the book (1-5):", 1, 5, 3)
    if st.button("Submit Review"):
        st.success(f"Your review for {book_title} has been shared! ⭐ {rating}/5")

# Reading Stats
elif page == "📊 Reading Stats":
    st.header("📊 Your Reading Statistics")
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    pages_read = np.random.randint(10, 50, size=7)
    
    fig, ax = plt.subplots()
    ax.plot(days, pages_read, marker='o', linestyle='-', color='green')
    ax.set_title("Weekly Reading Trend")
    ax.set_ylabel("Pages Read")
    ax.set_ylim(0, 50)
    st.pyplot(fig)

# Reading Goals
elif page == "🎯 Reading Goals":
    st.header("🎯 Set Your Reading Goals")
    goal = st.text_input("Enter your reading goal (e.g., 50 books this year):")
    if goal:
        st.write(f"Your Goal: {goal}")
    milestones = st.text_area("How will you achieve it?")
    if st.button("Save Goal"):
        st.success("Goal saved successfully! Keep going! 💪")

# Book Quiz
elif page == "🤔 Book Quiz":
    st.header("🤔 Test Your Book Knowledge!")
    quiz_questions = {
        "Who wrote '1984'?": "George Orwell",
        "What is the first book in the Harry Potter series?": "Harry Potter and the Sorcerer's Stone"
    }
    question, answer = random.choice(list(quiz_questions.items()))
    user_answer = st.text_input(question)
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer is: {answer}")

# Author Spotlights
elif page == "🔥 Author Spotlights":
    st.header("🔥 Discover Amazing Authors")
    authors = {
        "📖 **J.K. Rowling**": "Author of Harry Potter series.",
        "📘 **George Orwell**": "Wrote '1984' and 'Animal Farm'.",
        "📕 **Agatha Christie**": "Queen of Mystery novels.",
        "📙 **Brandon Sanderson**": "Fantasy writer of Mistborn series."
    }
    for name, bio in authors.items():
        st.subheader(name)
        st.write(bio)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Book Lovers Hub")

