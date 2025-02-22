import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Motivational Book Hub", page_icon="📚")
st.title("📚 Welcome to Motivational Book Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
if "current_book" in st.session_state:
    page = "📖 Reading"
else:
    page = st.sidebar.radio("Go to:", [
        "🏡 Home", "📖 Book Collection", "📊 Reading Progress", "📝 Reviews & Thoughts", "📅 Reading Goals"
    ])

# Book Data
books = [
    {"title": "Atomic Habits", "author": "James Clear", "image_url": "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg", "content": "This is the content of Atomic Habits..."},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71zytzrg6lL.jpg", "content": "This is the content of The 5 AM Club..."},
    {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "image_url": "https://bukharibooks.com/wp-content/uploads/2019/07/mindset-2.png", "content": "This is the content of Mindset..."},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71QKQ9mwV7L.jpg", "content": "This is the content of The Subtle Art of Not Giving a F*ck..."},
    {"title": "Awaken the Giant Within", "author": "Tony Robbins", "image_url": "https://images-na.ssl-images-amazon.com/images/I/81tEgsxpNZS.jpg", "content": "This is the content of Awaken the Giant Within..."},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71UypkUjStL.jpg", "content": "This is the content of Think and Grow Rich..."}
]

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
    selected_book = st.selectbox("Select a book to read:", [book["title"] for book in books])
    
    for book in books:
        if book["title"] == selected_book:
            st.image(book["image_url"], width=200)
            st.subheader(book["title"])
            st.write(f"**Author:** {book['author']}")
            if st.button("📖 Read Now"):
                st.session_state["current_book"] = book["title"]
                st.rerun()

# Dynamic Book Reading Page
elif page == "📖 Reading":
    for book in books:
        if book["title"] == st.session_state.get("current_book"):
            st.header(f"📖 Reading: {book['title']}")
            st.image(book["image_url"], width=200)
            st.subheader(f"By {book['author']}")
            st.write(book["content"])
            if st.button("⬅ Back to Collection"):
                del st.session_state["current_book"]
                st.rerun()

# Reading Progress Page
elif page == "📊 Reading Progress":
    st.header("📊 Track Your Reading Progress")
    book_titles = [book["title"] for book in books]
    progress = np.random.randint(0, 100, size=len(book_titles))
    fig, ax = plt.subplots()
    ax.barh(book_titles, progress, color=['#FF5733', '#33FF57', '#3357FF', '#F3FF33'])
    ax.set_title("Reading Progress (%)")
    ax.set_xlabel("Completion %")
    st.pyplot(fig)

# Reviews & Thoughts Page
elif page == "📝 Reviews & Thoughts":
    st.header("📝 Share Your Thoughts on Books")
    book = st.selectbox("Select a Book", book_titles)
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

