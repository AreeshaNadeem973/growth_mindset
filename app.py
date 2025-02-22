import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Next-Gen Power", page_icon="🚀")
st.title("Next-Gen Power: Mindset, Innovation & Success")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏡 Home"

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
if "current_book" in st.session_state:
    st.session_state.page = "📖 Reading"
else:
    st.session_state.page = st.sidebar.radio("Go to:", [
        "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights", "📅 Set Your Vision", "🌅 Morning Routine for Success"
    ])

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

# Morning Routine Page
elif st.session_state.page == "🌅 Morning Routine for Success":
    st.header("🌅 Build a Powerful Morning Routine")
    st.markdown("""
    Start your day with energy, clarity, and purpose. Watch this powerful morning routine to boost your success:
    """)
    st.video("https://www.youtube.com/watch?v=8TToLgWcF8s")  # Replace with a working video URL
    st.markdown("""
    ### Key Morning Habits:
    - 🌞 Wake up early and hydrate
    - 📖 Read for 15 minutes
    - 🏋️ Exercise to activate your body
    - 📝 Plan your top 3 goals for the day
    - 🧘 Practice gratitude and mindfulness
    """)
    st.success("Implement these habits and transform your life! 🚀")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")
