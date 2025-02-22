import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random

# App Title
st.set_page_config(page_title="Next-Gen Power", page_icon="🚀")
st.title("Next-Gen Power: Mindset, Innovation & Success")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"
if "current_book" not in st.session_state:
    st.session_state.current_book = None
if "completed_books" not in st.session_state:
    st.session_state.completed_books = []
if "insights" not in st.session_state:
    st.session_state.insights = []
if "goals" not in st.session_state:
    st.session_state.goals = []

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
st.session_state.page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights",
    "📅 Set Your Vision", "🎯 Daily Challenge", "🎥 Video Inspirations", "🧠 AI Book Suggestions", "💬 Community Discussion", "🏆 Achievements & Badges"
])

# Book Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Improvement"},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "category": "Productivity"},
    {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "category": "Psychology"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "category": "Self-Help"},
    {"title": "Awaken the Giant Within", "author": "Tony Robbins", "category": "Motivation"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "category": "Wealth"}
]

# Navigation Logic
if st.session_state.page == "🏡 Home":
    st.header("🚀 Welcome to Next-Gen Power")
    st.markdown("Start your journey to success today!")

elif st.session_state.page == "📚 Transform Your Mindset":
    st.header("📚 Transform Your Mindset with Powerful Reads")
    selected_category = st.selectbox("Choose a Category:", ["All"] + list(set(book["category"] for book in books)))
    filtered_books = books if selected_category == "All" else [book for book in books if book["category"] == selected_category]
    for book in filtered_books:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("https://via.placeholder.com/120", width=120)
            with col2:
                st.subheader(book["title"])
                st.write(f"**Author:** {book['author']}")
                st.write(f"**Category:** {book['category']}")
                if st.button(f"📖 Read More", key=book['title']):
                    st.session_state.current_book = book  # Store the selected book
                    st.session_state.page = "📖 Reading"  # Set the new page
                    st.rerun()

elif st.session_state.page == "📊 Your Growth Journey":
    st.header("📊 Your Growth Journey")
    progress = np.random.randint(0, 100, size=len(books))
    fig, ax = plt.subplots()
    ax.pie(progress, labels=[book["title"] for book in books], autopct='%1.1f%%', startangle=140)
    ax.set_title("Your Reading Progress")
    st.pyplot(fig)
    
    # Personal Reflection
    st.subheader("📝 Personal Reflection")
    reflection = st.text_area("Write about your learning journey:")
    if st.button("Save Reflection"):
        st.success("Your reflection has been saved!")

elif st.session_state.page == "📝 Share Your Insights":
    st.header("📝 Share Your Insights & Reflections")
    book = st.selectbox("Select a Book", [book["title"] for book in books])
    review = st.text_area("What did you learn?")
    if st.button("Submit Your Reflection"):
        st.session_state.insights.append({"book": book, "review": review})
        st.success("Your thoughts have been saved!")
    
    # Display Past Insights
    if st.session_state.insights:
        st.subheader("📖 Your Shared Insights")
        for insight in st.session_state.insights:
            st.write(f"**{insight['book']}:** {insight['review']}")

elif st.session_state.page == "📅 Set Your Vision":
    st.header("📅 Set Your Vision for Success")
    goal = st.text_input("What’s your next goal?")
    deadline = st.date_input("Set a deadline:")
    if st.button("Save Your Goal"):
        st.session_state.goals.append({"goal": goal, "deadline": deadline})
        st.success("Your vision is now set! Keep growing!")
    
    # Display Goals
    if st.session_state.goals:
        st.subheader("🎯 Your Goals")
        for g in st.session_state.goals:
            st.write(f"- {g['goal']} (Deadline: {g['deadline']})")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")

