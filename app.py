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
   ])

# Book Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "image_url": "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg", "category": "Self-Improvement", "description": "A practical guide to building good habits and breaking bad ones."},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71zytzrg6lL.jpg", "category": "Productivity", "description": "Discover the morning routine that can change your life."},
    {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "image_url": "https://bukharibooks.com/wp-content/uploads/2019/07/mindset-2.png", "category": "Psychology", "description": "Understand how a growth mindset leads to success."},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71QKQ9mwV7L.jpg", "category": "Self-Help", "description": "A counterintuitive approach to living a good life."},
    {"title": "Awaken the Giant Within", "author": "Tony Robbins", "image_url": "https://images-na.ssl-images-amazon.com/images/I/81tEgsxpNZS.jpg", "category": "Motivation", "description": "Unleash your full potential with Tony Robbins' strategies."},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71UypkUjStL.jpg", "category": "Wealth", "description": "Timeless principles of success and wealth-building."}
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


