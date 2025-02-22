import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Mindset & Success Hub", page_icon="🚀")
st.title("Mindset & Success Hub: Unlock Your Potential")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
st.session_state.page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights", "📅 Set Your Vision"
])

# Book Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Improvement", "description": "Build good habits and break bad ones."},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "category": "Productivity", "description": "Master your morning routine."},
    {"title": "Mindset", "author": "Carol S. Dweck", "category": "Psychology", "description": "Growth mindset for success."},
]
book_titles = [book["title"] for book in books]

# Home Page
if st.session_state.page == "🏡 Home":
    st.header("🚀 Welcome to Mindset & Success Hub")
    st.markdown("""
    ✅ **Learn from the Best** 📖  
    ✅ **Track Your Growth** 📊  
    ✅ **Achieve More Every Day** 💡  
    
    Start your journey today! 🚀
    """)

# Book Collection Page
elif st.session_state.page == "📚 Transform Your Mindset":
    st.header("📚 Transform Your Mindset with Books")
    for book in books:
        st.subheader(book["title"])
        st.write(f"**Author:** {book['author']}")
        st.write(f"📖 {book['description']}")
        st.markdown("---")

# Growth Journey Page
elif st.session_state.page == "📊 Your Growth Journey":
    st.header("📊 Track Your Growth")
    progress = np.random.randint(0, 100, size=len(book_titles))
    fig, ax = plt.subplots()
    ax.pie(progress, labels=book_titles, autopct='%1.1f%%')
    st.pyplot(fig)

# Insights Page
elif st.session_state.page == "📝 Share Your Insights":
    st.header("📝 Share Your Learnings")
    selected_book = st.selectbox("Select a Book", book_titles)
    st.text_area("Your Thoughts")
    if st.button("Submit"):
        st.success("Your insights have been recorded!")

# Vision Page
elif st.session_state.page == "📅 Set Your Vision":
    st.header("📅 Define Your Next Step")
    goal = st.text_input("Your Next Goal")
    if st.button("Save"):
        st.success("Goal saved! Keep growing!")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Mindset & Success Hub")


