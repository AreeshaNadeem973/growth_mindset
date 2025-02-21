import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Custom Styling
st.markdown("""
    <style>
        .main {background-color: #f4f4f4; padding: 20px; border-radius: 10px;}
        .title {color: #ff6347; text-align: center; font-size: 40px; font-weight: bold;}
        .subtitle {color: #4682b4; text-align: center; font-size: 20px;}
        .quote-box {background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);}
        .goal-box {background: #dff0d8; padding: 20px; border-radius: 8px;}
        .home-container {text-align: center; padding: 40px; background: linear-gradient(to right, #ff7e5f, #feb47b); border-radius: 12px; color: white;}
        .home-title {font-size: 35px; font-weight: bold; margin-bottom: 10px;}
        .home-subtext {font-size: 18px; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>🌟 Daily Motivation Hub</div>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Progress Graph", "💬 Daily Quote", "📖 Success Stories", "🎯 Goal Planner",
    "📝 Journal", "🎵 Motivational Music", "📺 Inspirational Videos"
])

# Home Page
if page == "🏡 Home":
    st.markdown("""
        <div class='home-container'>
            <div class='home-title'>Welcome to Daily Motivation Hub 🚀</div>
            <div class='home-subtext'>Fuel your passion, overcome obstacles, and stay inspired every day.</div>
            <div class='home-subtext'>✨ Start your journey towards greatness now! ✨</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://media.istockphoto.com/id/1282618663/photo/positivity-and-motivation.webp", use_container_width=True)
    
    st.markdown("""
        <div class='quote-box'>
        ✅ **Boost Productivity**: A positive mindset leads to better performance.  
        ✅ **Overcome Challenges**: Face obstacles with confidence.  
        ✅ **Stay Inspired**: Keep pushing towards your dreams.  
        ✅ **Achieve Your Goals**: Motivation drives success!  
        </div>
    """, unsafe_allow_html=True)

# Progress Graph with Balloons Effect
elif page == "📊 Progress Graph":
    st.markdown("<div class='subtitle'>📊 Your Progress Over Time</div>", unsafe_allow_html=True)
    
    x = np.arange(1, 11)
    y = np.random.randint(5, 100, size=10)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Days")
    ax.set_ylabel("Motivation Level")
    st.pyplot(fig)
    
    if st.button("Click the Graph for Celebration!"):
        st.balloons()

# Daily Quote
elif page == "💬 Daily Quote":
    st.markdown("<div class='subtitle'>💬 Today's Motivational Quote</div>", unsafe_allow_html=True)
    
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn’t just find you. You have to go out and get it."
    ]
    st.markdown(f"<div class='quote-box'><b>{random.choice(quotes)}</b></div>", unsafe_allow_html=True)

# Success Stories
elif page == "📖 Success Stories":
    st.markdown("<div class='subtitle'>📖 Inspirational Success Stories</div>", unsafe_allow_html=True)
    
    stories = [
        ("💪 **Nick Vujicic**", "Born without limbs, became a world-renowned motivational speaker."),
        ("📚 **J.K. Rowling**", "Rejected multiple times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Cut from his high school basketball team, but became an NBA legend."),
        ("🚀 **Elon Musk**", "Faced failures but built Tesla & SpaceX into global giants.")
    ]
    
    for name, story in stories:
        st.markdown(f"<div class='quote-box'><b>{name}</b><br>{story}</div>", unsafe_allow_html=True)

# Goal Planner
elif page == "🎯 Goal Planner":
    st.markdown("<div class='subtitle'>🎯 Set Your Goals</div>", unsafe_allow_html=True)
    
    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# Journal
elif page == "📝 Journal":
    st.markdown("<div class='subtitle'>📝 Daily Reflection Journal</div>", unsafe_allow_html=True)
    
    journal_entry = st.text_area("📖 Write about your thoughts and achievements today:")
    
    if st.button("Save Journal Entry"):
        st.success("📝 Journal entry saved! Keep reflecting and growing.")

# Footer
st.markdown("---")
st.markdown("🚀 *Stay Inspired, Stay Motivated!* 🌟")
