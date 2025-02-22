import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# App Title
st.set_page_config(page_title="Book Lovers Hub", page_icon="📚")
st.title("📚 Book Lovers Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Reading Tracker", "💡 Book Recommendations", "📖 Author Spotlights",
    "📝 Book Reviews", "📚 Reading Challenges", "🤔 Literary Quiz", "📜 Classic Literature"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Ultimate Book Lovers Hub! 📖✨")
    
    st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794", use_container_width=True)

    st.markdown("""
    ### Why Reading Matters?
    ✅ **Expand Your Knowledge**: Books open new worlds.  
    ✅ **Improve Focus & Imagination**: A daily reading habit boosts creativity.  
    ✅ **Enhance Vocabulary**: Every book teaches something new.  
    ✅ **Relax & Unwind**: Nothing beats a good story!  
    """)
    st.success("Every book is a new adventure! Start reading today! 📚")

# Reading Tracker
elif page == "📅 Reading Tracker":
    st.header("📅 Track Your Reading Progress")
    books = ["Fiction", "Non-Fiction", "Self-Help", "Science Fiction", "Fantasy"]

    for book in books:
        st.checkbox(f"Did you read a {book.lower()} book today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep up the reading habit!")
        st.balloons()

    # Weekly Reading Progress Graph
    weekly_progress = {book: random.randint(0, 7) for book in books}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='blue')
    ax.set_title("Weekly Reading Progress")
    ax.set_ylabel("Days Read")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Book Recommendations
elif page == "💡 Book Recommendations":
    st.header("💡 Must-Read Books")
    recommendations = [
        "📖 *To Kill a Mockingbird* - Harper Lee",
        "📖 *1984* - George Orwell",
        "📖 *The Great Gatsby* - F. Scott Fitzgerald",
        "📖 *Atomic Habits* - James Clear",
        "📖 *The Hobbit* - J.R.R. Tolkien"
    ]
    st.info(f"📚 **Today's Recommendation:** {random.choice(recommendations)}")

# Author Spotlights
elif page == "📖 Author Spotlights":
    st.header("📖 Meet Iconic Authors")
    authors = [
        ("✍️ **J.K. Rowling**", "Created the magical world of Harry Potter."),
        ("📚 **George Orwell**", "Wrote thought-provoking books like *1984* and *Animal Farm*."),
        ("🖊 **Agatha Christie**", "The queen of mystery novels with classics like *Murder on the Orient Express*.")
    ]
    for name, bio in authors:
        st.subheader(name)
        st.write(bio)

# Book Reviews
elif page == "📝 Book Reviews":
    st.header("📝 Share Your Book Reviews")
    book_title = st.text_input("Book Title:")
    review = st.text_area("Write your review:")
    
    if st.button("Submit Review"):
        st.success("Review submitted successfully!")

# Reading Challenges
elif page == "📚 Reading Challenges":
    st.header("📚 Join a Reading Challenge")
    challenges = [
        "📅 **30-Day Reading Challenge** - Read 15 minutes daily.",
        "📚 **Genre Exploration** - Read one book from 5 different genres.",
        "🕰 **Classic Challenge** - Read at least 3 classic novels this year."
    ]
    st.write(f"🔥 **Today's Challenge:** {random.choice(challenges)}")

# Literary Quiz
elif page == "🤔 Literary Quiz":
    st.header("🤔 Test Your Book Knowledge!")
    quizzes = [
        ("📖 Who wrote *Pride and Prejudice*?", "Jane Austen"),
        ("📚 What is the first book in *The Lord of the Rings* trilogy?", "The Fellowship of the Ring"),
        ("📜 Which Shakespeare play features the characters Rosencrantz and Guildenstern?", "Hamlet")
    ]
    question, answer = quizzes[random.randint(0, len(quizzes) - 1)]
    st.write(question)
    user_answer = st.text_input("Your answer:")
    
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! Well done!")
            st.balloons()
        else:
            st.error(f"Not quite. The correct answer is: {answer}")

# Classic Literature
elif page == "📜 Classic Literature":
    st.header("📜 Timeless Literary Classics")
    classics = [
        "📘 *Moby-Dick* - Herman Melville",
        "📕 *Crime and Punishment* - Fyodor Dostoevsky",
        "📗 *Pride and Prejudice* - Jane Austen",
        "📙 *Great Expectations* - Charles Dickens"
    ]
    st.info(f"📖 **Classic Recommendation:** {random.choice(classics)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Book Lovers Hub")

