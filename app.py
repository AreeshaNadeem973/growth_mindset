import streamlit as st
import random

# App Title
st.set_page_config(page_title="📚 Reading Hub", page_icon="📖")
st.title("📖 Welcome to the Reading Hub!")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Reading Tracker", "📖 Book Recommendations", "✍️ Book Reviews",
    "🎯 Reading Goals", "📜 Literary Quotes", "🧠 Reading Challenges", "📝 Writing Corner"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Personal Reading Hub! 📚")
    st.markdown("""
    ### Why Reading Matters?
    ✅ **Expand Your Knowledge**: Learn something new every day.  
    ✅ **Improve Focus & Imagination**: Books transport you to different worlds.  
    ✅ **Reduce Stress**: Reading helps you relax and unwind.  
    ✅ **Develop a Lifelong Habit**: Build a consistent reading routine.  
    """)
    st.image("https://media.istockphoto.com/id/1168362768/photo/book-open-with-magical-light.jpg", use_container_width=True)
    st.success("Today is a great day to start a new book! 📖")

# Reading Tracker
elif page == "📅 Reading Tracker":
    st.header("📅 Track Your Reading Progress")
    books = st.text_area("Enter the books you're currently reading:")
    if st.button("Save Progress"):
        st.success("Great job! Keep reading!")
        st.balloons()
    
    # Add a reading streak counter
    streak = st.session_state.get('reading_streak', 0)
    st.write(f"🔥 Current Reading Streak: {streak} days")
    if st.button("Increment Streak"):
        streak += 1
        st.session_state.reading_streak = streak
        st.success(f"New streak: {streak} days!")

# Book Recommendations
elif page == "📖 Book Recommendations":
    st.header("📖 Book Recommendations")
    categories = {
        "Fiction": "'To Kill a Mockingbird' by Harper Lee",
        "Mystery": "'Gone Girl' by Gillian Flynn",
        "Fantasy": "'Harry Potter and the Sorcerer’s Stone' by J.K. Rowling",
        "Science Fiction": "'Dune' by Frank Herbert",
        "Non-Fiction": "'Sapiens' by Yuval Noah Harari",
        "Self-Help": "'Atomic Habits' by James Clear"
    }
    genre = st.selectbox("Choose a genre:", list(categories.keys()))
    st.write(f"📚 Recommended Book: {categories[genre]}")

# Book Reviews
elif page == "✍️ Book Reviews":
    st.header("✍️ Write and Read Book Reviews")
    book_title = st.text_input("Enter the book title:")
    review = st.text_area("Write your review:")
    if st.button("Submit Review"):
        st.success("Review submitted successfully! 📖")

# Reading Goals
elif page == "🎯 Reading Goals":
    st.header("🎯 Set Your Reading Goals")
    goal = st.text_input("Enter your reading goal (e.g., Read 20 books this year):")
    if st.button("Save Goal"):
        st.success(f"Goal saved: {goal}")
        st.balloons()

# Literary Quotes
elif page == "📜 Literary Quotes":
    st.header("📜 Inspiring Literary Quotes")
    quotes = [
        "A reader lives a thousand lives before he dies. - George R.R. Martin",
        "Until I feared I would lose it, I never loved to read. One does not love breathing. - Harper Lee",
        "So many books, so little time. - Frank Zappa",
        "There is no friend as loyal as a book. - Ernest Hemingway"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Reading Challenges
elif page == "🧠 Reading Challenges":
    st.header("🧠 Take a Reading Challenge!")
    challenges = [
        "Read a book by an author from a different country.",
        "Read a book with more than 500 pages.",
        "Read a book that was published over 100 years ago.",
        "Read a book that was adapted into a movie."
    ]
    st.write(f"📖 **Your Challenge Today:** {random.choice(challenges)}")
    if st.button("I Accept the Challenge"):
        st.success("Great! Enjoy your reading journey! 📚")
        st.balloons()

# Writing Corner
elif page == "📝 Writing Corner":
    st.header("📝 Express Yourself Through Writing")
    st.write("Use this space to write your thoughts, poetry, or a short story!")
    user_text = st.text_area("Start writing:")
    if st.button("Save Writing"):
        st.success("Writing saved successfully! ✍️")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Reading Hub")
