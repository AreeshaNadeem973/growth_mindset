import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Configuration
st.set_page_config(page_title="Book Lovers Hub", page_icon="📚")

# Sidebar Navigation
st.sidebar.header("📖 Navigate")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📚 Book Collection", "📖 Reading Progress", "✍️ Book Reviews",
    "📅 Reading Goals", "🧠 Literary Trivia", "🔍 Discover New Books"
])

# Home Page
if page == "🏡 Home":
    st.title("📚 Welcome to Book Lovers Hub")
    st.image("https://images.pexels.com/photos/159866/books-bookstore-book-reading-159866.jpeg", width=400)
    
    st.markdown("""
    ### Why Join?
    - 📖 **Discover & track books**
    - 📝 **Review & share thoughts**
    - 🎯 **Set & achieve reading goals**
    - 🧠 **Challenge your literary knowledge**
    """)
    
    quotes = [
        "A reader lives a thousand lives before he dies. - George R.R. Martin",
        "Reading is essential for those who seek to rise above the ordinary. - Jim Rohn",
        "Books are uniquely portable magic. - Stephen King"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Book Collection
elif page == "📚 Book Collection":
    st.header("📚 Your Personal Book Collection")
    books = ["To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice"]
    selected_book = st.selectbox("Choose a book to explore:", books)
    
    st.write(f"📖 **Selected Book:** {selected_book}")
    st.image("https://source.unsplash.com/200x300/?book", width=150)

# Reading Progress
elif page == "📖 Reading Progress":
    st.header("📖 Track Your Reading Progress")
    progress = st.slider("How much have you read this week?", 0, 100, 50)
    
    fig, ax = plt.subplots()
    ax.bar(["Progress"], [progress], color='blue')
    ax.set_ylim(0, 100)
    ax.set_ylabel("% Completed")
    st.pyplot(fig)

# Book Reviews
elif page == "✍️ Book Reviews":
    st.header("✍️ Share Your Book Reviews")
    book = st.text_input("Book Title:")
    review = st.text_area("Your Review:")
    rating = st.slider("Rate the book (1-5 stars):", 1, 5, 3)
    if st.button("Submit Review"):
        st.success("Review Submitted! 📖")

# Reading Goals
elif page == "📅 Reading Goals":
    st.header("📅 Set Your Reading Goals")
    goal = st.number_input("How many books do you want to read this year?", min_value=1, max_value=100, value=12)
    completed = st.number_input("How many books have you read so far?", min_value=0, max_value=goal, value=3)
    
    progress = (completed / goal) * 100
    fig, ax = plt.subplots()
    ax.pie([progress, 100 - progress], labels=["Completed", "Remaining"], colors=["green", "gray"], autopct='%1.1f%%')
    st.pyplot(fig)

# Literary Trivia
elif page == "🧠 Literary Trivia":
    st.header("🧠 Test Your Book Knowledge")
    trivia = [
        ("Who wrote 'Pride and Prejudice'?", "Jane Austen"),
        ("What is the first book in the Harry Potter series?", "Harry Potter and the Sorcerer's Stone"),
    ]
    question, answer = random.choice(trivia)
    st.write(question)
    user_answer = st.text_input("Your Answer:")
    
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer is: {answer}")

# Discover New Books
elif page == "🔍 Discover New Books":
    st.header("🔍 Find Your Next Read")
    genres = ["Fantasy", "Science Fiction", "Mystery", "Historical Fiction"]
    selected_genre = st.selectbox("Select a genre:", genres)
    st.write(f"📚 **Books in {selected_genre}:**")
    
    recommendations = {
        "Fantasy": ["Harry Potter", "The Hobbit"],
        "Science Fiction": ["Dune", "The Martian"],
        "Mystery": ["Sherlock Holmes", "Gone Girl"],
        "Historical Fiction": ["The Book Thief", "All the Light We Cannot See"]
    }
    st.write(recommendations[selected_genre])

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Book Lovers Hub")
