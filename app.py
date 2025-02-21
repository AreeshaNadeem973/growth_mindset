import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Custom Styling
st.markdown("""
    <style>
        .main {background-color: #f4f4f4; padding: 20px; border-radius: 10px;}
        .title {color: #ff4500; text-align: center; font-size: 42px; font-weight: bold;}
        .subtitle {color: #2e8b57; text-align: center; font-size: 22px;}
        .box {background: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);}
        .home-container {text-align: center; padding: 40px; background: linear-gradient(to right, #36d1dc, #5b86e5); border-radius: 12px; color: white;}
        .home-title {font-size: 36px; font-weight: bold; margin-bottom: 10px;}
        .home-subtext {font-size: 18px; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>🌟 Ultimate Motivation Hub</div>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("📌 Navigate")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📊 Progress Tracker", "💬 Daily Inspiration", "📖 Iconic Success Stories", "🎯 Personal Goals",
    "📝 Reflect & Grow", "🎶 Uplifting Music", "📺 Must-Watch Videos"
])

# Home Page
if page == "🏡 Home":
    st.markdown("""
        <div class='home-container'>
            <div class='home-title'>Welcome to Ultimate Motivation Hub 🚀</div>
            <div class='home-subtext'>Elevate your mindset, overcome hurdles, and thrive in life.</div>
            <div class='home-subtext'>✨ Embark on your path to greatness today! ✨</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://media.istockphoto.com/id/1322275371/photo/goal-achievement.webp", use_container_width=True)
    
    st.markdown("""
        <div class='box'>
        ✅ **Enhance Productivity**: A strong mindset boosts efficiency.  
        ✅ **Tackle Challenges Head-On**: Face every hurdle with confidence.  
        ✅ **Stay Encouraged**: Daily motivation keeps you going.  
        ✅ **Crush Your Goals**: Consistency leads to success!  
        </div>
    """, unsafe_allow_html=True)

# Progress Tracker with Balloons Effect
elif page == "📊 Progress Tracker":
    st.markdown("<div class='subtitle'>📊 Track Your Progress</div>", unsafe_allow_html=True)
    
    x = np.arange(1, 11)
    y = np.random.randint(10, 100, size=10)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Days")
    ax.set_ylabel("Motivation Level")
    st.pyplot(fig)
    
    if st.button("Celebrate Progress! 🎈"):
        st.balloons()

# Daily Inspiration
elif page == "💬 Daily Inspiration":
    st.markdown("<div class='subtitle'>💬 Get Inspired Today</div>", unsafe_allow_html=True)
    
    quotes = [
        "Your potential is limitless!", 
        "Every step forward is progress.",
        "Believe in yourself and take action.",
        "Dream big, work hard, stay focused.",
        "Challenges are opportunities in disguise.",
        "Success comes to those who persist."
    ]
    st.markdown(f"<div class='box'><b>{random.choice(quotes)}</b></div>", unsafe_allow_html=True)

# Iconic Success Stories
elif page == "📖 Iconic Success Stories":
    st.markdown("<div class='subtitle'>📖 Learn from the Best</div>", unsafe_allow_html=True)
    
    stories = [
        ("💡 **Elon Musk**", "From failures to leading Tesla & SpaceX."),
        ("🏀 **Michael Jordan**", "Overcame rejection to become an NBA legend."),
        ("📚 **Oprah Winfrey**", "From adversity to media empire."),
        ("🚀 **Jeff Bezos**", "Built Amazon from a garage startup to a giant.")
    ]
    
    for name, story in stories:
        st.markdown(f"<div class='box'><b>{name}</b><br>{story}</div>", unsafe_allow_html=True)

# Personal Goals
elif page == "🎯 Personal Goals":
    st.markdown("<div class='subtitle'>🎯 Define Your Goals</div>", unsafe_allow_html=True)
    
    goal = st.text_input("📝 Your Goal:")
    deadline = st.date_input("📅 Set a Deadline:")
    
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# Reflect & Grow
elif page == "📝 Reflect & Grow":
    st.markdown("<div class='subtitle'>📝 Your Daily Reflection</div>", unsafe_allow_html=True)
    
    journal_entry = st.text_area("📖 Share your thoughts & insights:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep progressing.")

# Interactive Checkbox Feature
st.markdown("### ✅ Mark Your Achievements")
achievements = ["Completed a daily challenge", "Read a success story", "Set a new goal", "Reflected on progress"]
checkbox_states = {}

for achievement in achievements:
    checkbox_states[achievement] = st.checkbox(achievement)

# Footer
st.markdown("---")
st.markdown("🔥 *Stay Motivated, Stay Focused!* 🚀")
