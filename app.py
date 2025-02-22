import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Book Lovers Hub", page_icon="📚")
st.title("📚 Welcome to Book Lovers Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Reading Tracker", "📚 Book Recommendations", "📝 Book Reviews", "📊 Reading Statistics", "🔖 Favorite Quotes"
])

# Home Page
if page == "🏡 Home":

    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", width=250)  # Smaller Image
    st.markdown("""
    ### Discover, Track, and Enjoy Books!
    ✅ **Track Your Reading Progress** 📖  
    ✅ **Get Personalized Book Recommendations** 📚  
    ✅ **Share and Read Reviews** 📝  
    ✅ **Find Inspiring Book Quotes** 🔖  
    """)
    st.success("Start your reading journey today! 📖")

# Reading Tracker
elif page == "📖 Reading Tracker":
    st.header("📖 Track Your Reading")
    books = ["The Alchemist", "Atomic Habits", "1984", "The Power of Now"]
    for book in books:
        st.checkbox(f"Finished reading '{book}'?")
    if st.button("Save Progress"):
        st.success("Great job! Keep reading!")
        st.balloons()

    # Monthly Reading Progress Graph
    progress = np.random.randint(5, 30, size=len(books))
    fig, ax = plt.subplots()
    ax.bar(books, progress, color=['#FF5733', '#33FF57', '#3357FF', '#F3FF33'])
    ax.set_title("Monthly Reading Progress")
    ax.set_ylabel("Days Read")
    ax.set_ylim(0, 30)
    st.pyplot(fig)

# Book Recommendations
elif page == "📚 Book Recommendations":
    st.header("📚 Personalized Book Recommendations")
    genres = ["Fiction", "Self-Help", "Mystery", "Sci-Fi", "Biography"]
    selected_genre = st.selectbox("Choose a genre:", genres)
    
    recommendations = {
        "Fiction": ["The Great Gatsby", "Pride and Prejudice", "To Kill a Mockingbird"],
        "Self-Help": ["Atomic Habits", "The 5 AM Club", "The Power of Habit"],
        "Mystery": ["Gone Girl", "The Girl with the Dragon Tattoo", "Sherlock Holmes"],
        "Sci-Fi": ["Dune", "Neuromancer", "The Martian"],
        "Biography": ["Steve Jobs", "Becoming", "Educated"]
    }
    st.write("📚 Recommended Books:")
    for book in recommendations[selected_genre]:
        st.write(f"- {book}")

# Book Reviews
elif page == "📝 Book Reviews":
    st.header("📝 Share & Read Reviews")
    book = st.text_input("Book Name:")
    review = st.text_area("Your Review:")
    if st.button("Submit Review"):
        st.success("Review submitted successfully!")

# Reading Statistics
elif page == "📊 Reading Statistics":
    st.header("📊 Your Reading Trends")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    books_read = np.random.randint(1, 10, size=12)
    fig, ax = plt.subplots()
    ax.plot(months, books_read, marker='o', linestyle='-', color='blue')
    ax.set_title("Books Read Per Month")
    ax.set_ylabel("Books Read")
    ax.set_ylim(0, 10)
    st.pyplot(fig)

# Favorite Quotes
elif page == "🔖 Favorite Quotes":
    st.header("🔖 Inspiring Book Quotes")
    quotes = [
        "The only thing that you absolutely have to know is the location of the library. - Albert Einstein",
        "A reader lives a thousand lives before he dies. - George R.R. Martin",
        "There is no friend as loyal as a book. - Ernest Hemingway",
        "Reading is essential for those who seek to rise above the ordinary. - Jim Rohn"
    ]
    st.info(f"📖 **Quote of the Day:** {random.choice(quotes)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Book Lovers Hub")
