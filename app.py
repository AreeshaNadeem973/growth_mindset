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
    "🏡 Home", "📖 Reading Tracker", "📚 Book Recommendations", "📝 Book Reviews", "📊 Reading Statistics"
])

# Home Page
if page == "🏡 Home":
    st.header("📚 Welcome to Book Lovers Hub")
    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", width=300)  # Smaller Image
    st.markdown("""
    ### Discover, Track, and Enjoy Books!
    ✅ **Track Your Reading Progress** 📖  
    ✅ **Get Personalized Book Recommendations** 📚  
    ✅ **Share and Read Reviews** 📝  
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

    # New Progress Graph with different colors
    progress = np.random.randint(0, 7, size=len(books))
    fig, ax = plt.subplots()
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
    ax.bar(books, progress, color=colors)
    ax.set_title("Weekly Reading Progress")
    ax.set_ylabel("Days Read")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Book Recommendations
elif page == "📚 Book Recommendations":
    st.header("📚 Personalized Book Recommendations")
    genres = ["Fiction", "Self-Help", "Mystery", "Sci-Fi", "Biography"]
    selected_genre = st.selectbox("Choose a genre:", genres)
    
    recommendations = {
        "Fiction": ["The Great Gatsby", "Pride and Prejudice"],
        "Self-Help": ["Atomic Habits", "The 5 AM Club"],
        "Mystery": ["Gone Girl", "The Girl with the Dragon Tattoo"],
        "Sci-Fi": ["Dune", "Neuromancer"],
        "Biography": ["Steve Jobs", "Becoming"]
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

    # Sentiment Analysis Graph
    sentiments = ["Positive", "Neutral", "Negative"]
    sentiment_counts = np.random.randint(5, 20, size=3)
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiments, autopct='%1.1f%%', colors=['#2ECC71', '#F1C40F', '#E74C3C'])
    ax.set_title("Book Review Sentiments")
    st.pyplot(fig)

# Reading Statistics
elif page == "📊 Reading Statistics":
    st.header("📊 Your Reading Trends")
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    reading_hours = np.random.randint(0, 3, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, reading_hours, marker='o', linestyle='-', color='purple', linewidth=2, markersize=8)
    ax.fill_between(days, reading_hours, color='purple', alpha=0.2)
    ax.set_title("Weekly Reading Hours")
    ax.set_ylabel("Hours Read")
    ax.set_ylim(0, 3)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Book Lovers Hub")
