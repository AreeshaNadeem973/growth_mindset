
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Motivational Book Hub", page_icon="📚")
st.title("📚 Welcome to Motivational Book Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📖 Book Collection", "📊 Reading Progress", "📝 Reviews & Thoughts", "📅 Reading Goals"
])

# Home Page
if page == "🏡 Home":
    st.header("📚 Welcome to Motivational Book Hub")
    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", use_container_width=True)
    st.markdown("""
    ### Explore & Grow with Motivational Books!
    ✅ **Read Life-Changing Books** 📖  
    ✅ **Track Your Reading Progress** 📊  
    ✅ **Share Your Thoughts & Reviews** 📝  
    """)
    st.success("Start your journey to success today! 🚀")

# Book Collection Page
elif page == "📖 Book Collection":
    st.header("📚 Explore Motivational & Life-Changing Books")
    books = [
        {"title": "Atomic Habits", "author": "James Clear", "image_url": "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg"},
        {"title": "The 5 AM Club", "author": "Robin Sharma", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71zytzrg6lL.jpg"},
        {"title": "The Power of Now", "author": "Eckhart Tolle", "image_url": "https://images-na.ssl-images-amazon.com/images/I/81bgwbXcT3L.jpg"},
        {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "image_url": "https://images-na.ssl-images-amazon.com/images/I/81rZ7G0cNxL.jpg"},
        {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71QKQ9mwV7L.jpg"},
        {"title": "Awaken the Giant Within", "author": "Tony Robbins", "image_url": "https://images-na.ssl-images-amazon.com/images/I/81tEgsxpNZS.jpg"}
    ]
    
    cols = st.columns(3)
    for index, book in enumerate(books):
        with cols[index % 3]:
            st.image(book["image_url"], width=150)
            if st.button(f"📖 Read {book['title']}", key=index):
                st.write(f"Opening {book['title']}...")
                st.markdown(f"[Read Now](#)")

# Reading Progress Page
elif page == "📊 Reading Progress":
    st.header("📊 Track Your Reading Progress")
    books = ["Atomic Habits", "The 5 AM Club", "The Power of Now", "Think and Grow Rich"]
    progress = np.random.randint(0, 100, size=len(books))
    fig, ax = plt.subplots()
    ax.barh(books, progress, color=['#FF5733', '#33FF57', '#3357FF', '#F3FF33'])
    ax.set_title("Reading Progress (%)")
    ax.set_xlabel("Completion %")
    st.pyplot(fig)

# Reviews & Thoughts Page
elif page == "📝 Reviews & Thoughts":
    st.header("📝 Share Your Thoughts on Books")
    book = st.selectbox("Select a Book", ["Atomic Habits", "The 5 AM Club", "The Power of Now", "Think and Grow Rich"])
    review = st.text_area("Write your review:")
    if st.button("Submit Review"):
        st.success("Review submitted successfully!")

# Reading Goals Page
elif page == "📅 Reading Goals":
    st.header("📅 Set Your Reading Goals")
    goal = st.text_input("Your Reading Goal:")
    if st.button("Save Goal"):
        st.success("Goal saved successfully! Keep reading!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Motivational Book Hub")

