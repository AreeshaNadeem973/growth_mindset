import streamlit as st
import random
from datetime import date

# App Title
st.set_page_config(page_title="📚 Reading Hub", page_icon="📖")
st.title("📚 Welcome to Your Reading Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Book Recommendations", "📚 My Library", "📊 Reading Progress",
    "✍️ Book Reviews", "🧠 Reading Challenges", "📅 Reading Planner", "🔎 Fun Trivia", "📚 Life & Motivation Books"
])

# Home Page
if page == "🏡 Home":
    st.header("📖 Explore the World of Books!")
    st.markdown("""
    ### Why Reading Matters?
    ✅ **Expand Your Knowledge** – Learn something new every day.  
    ✅ **Boost Imagination** – Enter different worlds through stories.  
    ✅ **Improve Focus & Memory** – Strengthen your cognitive skills.  
    ✅ **Reduce Stress** – Relax with a good book.  
    """)
    st.image("https://images.pexels.com/photos/46274/books-education-school-literature-46274.jpeg", use_container_width=True)
    st.success("A book a day keeps boredom away! Start your reading journey today! 📖")

# Book Recommendations
elif page == "📖 Book Recommendations":
    st.header("📚 Personalized Book Recommendations")
    genres = ["Fiction", "Mystery", "Fantasy", "Science Fiction", "Self-Help", "Biography", "History"]
    selected_genre = st.selectbox("Choose a Genre:", genres)
    books = {
        "Fiction": ["To Kill a Mockingbird", "1984", "The Great Gatsby"],
        "Mystery": ["Gone Girl", "The Girl with the Dragon Tattoo", "Big Little Lies"],
        "Fantasy": ["Harry Potter Series", "The Hobbit", "Percy Jackson"],
        "Science Fiction": ["Dune", "The Martian", "Ender's Game"],
        "Self-Help": ["Atomic Habits", "The Power of Now", "The Subtle Art of Not Giving a F*ck"],
        "Biography": ["Steve Jobs", "Becoming", "Long Walk to Freedom"],
        "History": ["Sapiens", "Guns, Germs, and Steel", "The Silk Roads"]
    }
    st.write(f"📖 Recommended Books in {selected_genre}:")
    for book in books[selected_genre]:
        st.write(f"- {book}")

# My Library
elif page == "📚 My Library":
    st.header("📚 Track Your Library")
    book_name = st.text_input("Enter Book Name:")
    if st.button("Add to Library"):
        st.success(f"{book_name} added to your library!")

# Reading Progress
elif page == "📊 Reading Progress":
    st.header("📊 Track Your Reading Progress")
    pages_read = st.number_input("Pages Read Today:", min_value=0, step=1)
    total_pages = st.number_input("Total Pages in the Book:", min_value=1, step=1)
    if st.button("Update Progress"):
        progress = (pages_read / total_pages) * 100
        st.progress(progress / 100)
        st.write(f"You've completed {progress:.2f}% of your book!")

# Book Reviews
elif page == "✍️ Book Reviews":
    st.header("✍️ Share Your Book Reviews")
    book_title = st.text_input("Book Title:")
    review = st.text_area("Write Your Review:")
    rating = st.slider("Rate the Book:", 1, 5, 3)
    if st.button("Submit Review"):
        st.success(f"Your review for {book_title} has been submitted! ⭐ {rating}/5")

# Reading Challenges
elif page == "🧠 Reading Challenges":
    st.header("🧠 Join a Reading Challenge!")
    challenges = [
        "Read 10 Books This Year",
        "Try a New Genre",
        "Read a Classic Novel",
        "Complete a 30-Day Reading Streak"
    ]
    challenge = random.choice(challenges)
    st.write(f"📌 Your Challenge: {challenge}")
    if st.button("Accept Challenge"):
        st.success("Great! Start reading today!")

# Reading Planner
elif page == "📅 Reading Planner":
    st.header("📅 Plan Your Reading Schedule")
    st.date_input("Select Your Reading Start Date:")
    st.date_input("Select Your Target Completion Date:")
    if st.button("Save Plan"):
        st.success("Your reading plan has been saved!")

# Fun Trivia
elif page == "🔎 Fun Trivia":
    st.header("🔎 Test Your Book Knowledge")
    trivia_questions = [
        ("Who wrote 'Pride and Prejudice'?", "Jane Austen"),
        ("What is the first book in the Harry Potter series?", "Harry Potter and the Sorcerer's Stone"),
        ("Which novel features the character Jay Gatsby?", "The Great Gatsby")
    ]
    question, answer = random.choice(trivia_questions)
    st.write(question)
    user_answer = st.text_input("Your Answer:")
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer is: {answer}")

# Life & Motivation Books
elif page == "📚 Life & Motivation Books":
    st.header("📚 Life & Motivation Books")
    motivation_books = [
        ("The 7 Habits of Highly Effective People", "https://m.media-amazon.com/images/I/81Rc+3O8g4L._SL1500_.jpg", "https://www.pdfdrive.com/the-7-habits-of-highly-effective-people-e15874302.html"),
        ("Think and Grow Rich", "https://m.media-amazon.com/images/I/91VS9xmr5UL._SL1500_.jpg", "https://www.pdfdrive.com/think-and-grow-rich-e15879348.html"),
        ("The Power of Now", "https://m.media-amazon.com/images/I/71t4GuxLCuL._SL1500_.jpg", "https://www.pdfdrive.com/the-power-of-now-e15874234.html")
    ]
    for title, img, link in motivation_books:
        st.subheader(title)
        st.image(img, width=200)
        st.markdown(f"[📖 Read Now]({link})", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Reading Hub")

