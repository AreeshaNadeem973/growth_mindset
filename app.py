import streamlit as st
import random

# App Title
st.set_page_config(page_title="📚 Reading Hub", page_icon="📖")
st.title("📚 Reading Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 My Bookshelf", "⭐ Book Recommendations", "📝 Book Reviews",
    "🎯 Reading Goals", "⏳ Reading Progress", "💡 Author Insights", "🧠 Book Trivia"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Personal Reading Hub! 📖")
    st.image("https://images.unsplash.com/photo-1512820790803-83ca734da794", use_container_width=True)
    st.markdown("""
    ### Why Read More Books?
    ✅ **Expand Your Knowledge**: Books are the gateway to new ideas.
    ✅ **Improve Focus & Creativity**: Enhance your imagination and thinking.
    ✅ **Reduce Stress**: Reading helps in relaxation and mindfulness.
    ✅ **Achieve Your Reading Goals**: Track your progress and stay motivated!
    """)
    st.success("Start your reading journey today! 📖")

# My Bookshelf
elif page == "📖 My Bookshelf":
    st.header("📖 Your Personal Bookshelf")
    st.write("Track books you've read and want to read.")
    books = ["Atomic Habits", "The Alchemist", "1984", "To Kill a Mockingbird", "Sapiens"]
    for book in books:
        st.checkbox(f"Read: {book}")
    if st.button("Save Progress"):
        st.success("Bookshelf updated! Keep reading! 📚")

# Book Recommendations
elif page == "⭐ Book Recommendations":
    st.header("⭐ Personalized Book Recommendations")
    genres = {"Fiction": "The Great Gatsby", "Self-Help": "The 7 Habits of Highly Effective People",
              "Science": "Brief Answers to the Big Questions", "History": "Sapiens"}
    genre = st.selectbox("Choose a genre:", list(genres.keys()))
    st.subheader(f"📖 Recommended Book: {genres[genre]}")
    st.image("https://via.placeholder.com/150", caption=genres[genre])
    st.write(f"Explore **{genres[genre]}** and expand your knowledge!")

# Book Reviews
elif page == "📝 Book Reviews":
    st.header("📝 Share & Read Book Reviews")
    st.subheader("Submit Your Review")
    book_name = st.text_input("Book Title:")
    review = st.text_area("Your Review:")
    rating = st.slider("Rate the book:", 1, 5, 3)
    if st.button("Submit Review"):
        st.success("Review submitted successfully! ✅")

# Reading Goals
elif page == "🎯 Reading Goals":
    st.header("🎯 Set Your Reading Goals")
    books_goal = st.number_input("Set a goal: Number of books to read this year", min_value=1, step=1)
    st.write(f"📚 Your goal: Read {books_goal} books this year!")
    if st.button("Save Goal"):
        st.success("Reading goal saved! Keep going! 📖")

# Reading Progress
elif page == "⏳ Reading Progress":
    st.header("⏳ Track Your Reading Progress")
    books_read = st.slider("How many books have you read so far?", 0, 50, 5)
    st.progress(books_read / 50)
    st.write(f"📖 You have read {books_read} books so far! Keep it up!")

# Author Insights
elif page == "💡 Author Insights":
    st.header("💡 Insights from Famous Authors")
    authors = {"J.K. Rowling": "Failure is the foundation of success.",
               "Stephen King": "Books are uniquely portable magic.",
               "Mark Twain": "A person who won't read has no advantage over one who can't read."}
    author = st.selectbox("Choose an author:", list(authors.keys()))
    st.write(f"📖 **{author}** once said: *'{authors[author]}'*")

# Book Trivia
elif page == "🧠 Book Trivia":
    st.header("🧠 Test Your Book Knowledge")
    questions = {"Who wrote 'Pride and Prejudice'?": "Jane Austen",
                 "Which book features the character Sherlock Holmes?": "A Study in Scarlet",
                 "What is the best-selling book of all time?": "The Bible"}
    question = random.choice(list(questions.keys()))
    st.write(question)
    answer = st.text_input("Your Answer:")
    if st.button("Check Answer"):
        if answer.lower() == questions[question].lower():
            st.success("Correct! ✅")
        else:
            st.error(f"Wrong! The correct answer is: {questions[question]}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Reading Hub")
