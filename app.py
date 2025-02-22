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
st.session_state.page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📚 Transform Your Mindset", "📊 Your Growth Journey", "📝 Share Your Insights",
    "📅 Set Your Vision", "🎙️ Inspirational Podcasts", "📜 Daily Affirmations", "🎯 Success Stories",
    "💡 Innovation Hub"
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

# New Pages

elif st.session_state.page == "📚 Transform Your Mindset":
    st.header("📚 Transform Your Mindset")
    st.write("Discover powerful books and techniques to shift your mindset for success.")
    st.markdown("""
    - **Atomic Habits** by James Clear
    - **Mindset: The New Psychology of Success** by Carol S. Dweck
    - **Think and Grow Rich** by Napoleon Hill
    """)

elif st.session_state.page == "📊 Your Growth Journey":
    st.header("📊 Track Your Growth")
    progress = np.random.randint(0, 100, size=5)
    fig, ax = plt.subplots()
    ax.pie(progress, labels=["Reading", "Learning", "Networking", "Practicing", "Innovating"], autopct='%1.1f%%', startangle=140, colors=['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A8'])
    ax.set_title("Growth Journey Progress")
    st.pyplot(fig)

elif st.session_state.page == "🎙️ Inspirational Podcasts":
    st.header("🎙️ Listen to Powerful Talks")
    st.write("Tune in to life-changing podcasts from world-class thinkers and leaders.")
    podcast_links = {
        "The Tony Robbins Podcast": "https://www.tonyrobbins.com/podcast/",
        "The School of Greatness - Lewis Howes": "https://lewishowes.com/sog-podcast/",
        "The Tim Ferriss Show": "https://tim.blog/podcast/"
    }
    for name, url in podcast_links.items():
        st.markdown(f"🔊 [{name}]({url})")

elif st.session_state.page == "📜 Daily Affirmations":
    st.header("📜 Start Your Day with Motivation")
    affirmations = [
        "I am capable of achieving greatness!",
        "Every challenge is an opportunity to grow.",
        "I am focused, determined, and unstoppable.",
        "Success is within my reach, and I take action towards it today.",
        "I have the power to create my own future."
    ]
    st.write(np.random.choice(affirmations))

elif st.session_state.page == "🎯 Success Stories":
    st.header("🎯 Learn from the Best")
    st.write("Read about inspiring people who have overcome challenges and built success.")
    st.markdown("""
    - 🌟 **Elon Musk:** From sleeping in his office to revolutionizing space travel.
    - 🌟 **Oprah Winfrey:** Overcame hardship to become a media mogul.
    - 🌟 **Jack Ma:** Faced 30+ rejections before creating Alibaba.
    """)

elif st.session_state.page == "💡 Innovation Hub":
    st.header("💡 Share & Discuss Breakthrough Ideas")
    idea = st.text_area("Have an innovative idea? Share it with the community!")
    if st.button("Post Idea"):
        st.success("Your idea has been shared! Keep innovating! 🚀")

# Footer
st.markdown("---")
st.markdown("🚀 Built for Future Leaders | © 2025 Next-Gen Power")

