import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import webbrowser

# App Title
st.set_page_config(page_title="Motivational Book Hub", page_icon="📚")
st.title(" Growth Mindset")

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
    {"title": "Atomic Habits", "author": "James Clear", "image_url": "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg", "read_url": "https://jamesclear.com/atomic-habits"},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71zytzrg6lL.jpg", "read_url": "https://www.robinsharma.com/book/the-5am-club"},
    {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "image_url": "https://bukharibooks.com/wp-content/uploads/2019/07/mindset-2.png", "read_url": "https://www.amazon.com/Mindset-Psychology-Carol-S-Dweck/dp/0345472322"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71QKQ9mwV7L.jpg", "read_url": "https://markmanson.net/books/subtle-art"},
    {"title": "Awaken the Giant Within", "author": "Tony Robbins", "image_url": "https://images-na.ssl-images-amazon.com/images/I/81tEgsxpNZS.jpg", "read_url": "https://www.tonyrobbins.com/podcast/awaken-the-giant-within/"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "image_url": "https://images-na.ssl-images-amazon.com/images/I/71UypkUjStL.jpg", "read_url": "https://www.naphill.org/think-and-grow-rich/"}
]

book_titles = [book["title"] for book in books]  # Ensure book_titles is always defined

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
    cols = st.columns(3)
    for index, book in enumerate(books):
        with cols[index % 3]:
            st.image(book["image_url"], width=150)
            st.subheader(book["title"])
            st.write(f"**Author:** {book['author']}")
            if st.button(f"📖 Read Now {book['title']}", key=book['title']):
                webbrowser.open_new_tab(book["read_url"])  # Open book link in new browser tab

# Reading Progress Page
elif page == "📊 Reading Progress":
    st.header("📊 Track Your Reading Progress")
    progress = np.random.randint(0, 100, size=len(book_titles))
    fig, ax = plt.subplots()
    ax.pie(progress, labels=book_titles, autopct='%1.1f%%', startangle=140, colors=['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A8', '#33FFF5'])
    ax.set_title("Reading Progress Distribution")
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
