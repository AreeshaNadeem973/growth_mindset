import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Next-Gen Power", page_icon="🚀")
st.title("Mindset & Success Hub: Unlock Your Potential")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
if "current_book" in st.session_state:
    st.session_state.page = "📖 Reading"
else:
    st.session_state.page = st.sidebar.radio("Go to:", [
        "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights", "📅 Set Your Vision"
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
categories = list(set(book["category"] for book in books))

# Home Page
if st.session_state.page == "🏡 Home":
    st.header("🚀 Welcome to Next-Gen Power")
    st.image("https://images.pexels.com/photos/415071/pexels-photo-415071.jpeg", use_container_width=True)
    st.markdown("""
    ### Unlock Your Full Potential with Knowledge!
    ✅ **Master the Art of Success** 📖  
    ✅ **Track Your Personal Growth** 📊  
    ✅ **Join a Community of Innovators** 💡  
    """)
    st.success("Start your journey to greatness today! 🚀")

# Book Collection Page
elif st.session_state.page == "📚 Transform Your Mindset":
    st.header("📚 Transform Your Mindset with Powerful Reads")
    selected_category = st.selectbox("Choose a Category:", ["All"] + categories)

    filtered_books = books if selected_category == "All" else [book for book in books if book["category"] == selected_category]

    for book in filtered_books:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(book["image_url"], width=120)
            with col2:
                st.subheader(book["title"])
                st.write(f"**Author:** {book['author']}")
                st.write(f"**Category:** {book['category']}")
                st.write(f"📖 {book['description']}")
                if st.button(f"📖 Read More", key=book['title']):
                    st.session_state.current_book = book  # Store the selected book
                    st.session_state.page = "📖 Reading"  # Set the new page
                    st.rerun()  # Rerun the app to switch the page

# Reading Page (Displays the selected book details)
elif st.session_state.page == "📖 Reading" and "current_book" in st.session_state:
    book = st.session_state.current_book
    st.header(f"📖 Dive Deep into Knowledge: {book['title']}")
    st.image(book["image_url"], width=200)
    st.write(f"**Author:** {book['author']}")
    st.write(f"**Category:** {book['category']}")
    st.write(f"📖 {book['description']}")
    if st.button("🔙 Back to Collection"):
        del st.session_state.current_book  # Remove selected book
        st.session_state.page = "📚 Transform Your Mindset"
        st.rerun()

# Reading Progress Page
elif st.session_state.page == "📊 Your Growth Journey":
    st.header("📊 Your Growth Journey")
    progress = np.random.randint(0, 100, size=len(book_titles))
    fig, ax = plt.subplots()
    ax.pie(progress, labels=book_titles, autopct='%1.1f%%', startangle=140, colors=['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A8', '#33FFF5'])
    ax.set_title("Your Reading Progress")
    st.pyplot(fig)

# Reviews & Thoughts Page
elif st.session_state.page == "📝 Share Your Insights":
    st.header("📝 Share Your Insights & Reflections")
    book = st.selectbox("Select a Book", book_titles)
    review = st.text_area("What did you learn?")
    if st.button("Submit Your Reflection"):
        st.success("Your thoughts have been saved!")

# Reading Goals Page
elif st.session_state.page == "📅 Set Your Vision":
    st.header("📅 Set Your Vision for Success")
    goal = st.text_input("What’s your next goal?")
    if st.button("Save Your Goal"):
        st.success("Your vision is now set! Keep growing!")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")



