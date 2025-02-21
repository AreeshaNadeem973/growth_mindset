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
st.markdown("<div class='title'>🌱 Growth Mindset Hub</div>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("📌 Navigate")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📊 Progress Tracker", "💡 Daily Motivation", "📖 Success Stories", "🎯 Goal Setter",
    "📝 Reflection Journal", "🎶 Brain Boost Exercises"
])

# Home Page
if page == "🏡 Home":
    st.markdown("""
        <div class='home-container'>
            <div class='home-title'>Welcome to the Growth Mindset Hub 🚀</div>
            <div class='home-subtext'>Develop resilience, embrace challenges, and unlock your full potential.</div>
            <div class='home-subtext'>✨ Your journey to growth starts here! ✨</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://media.istockphoto.com/id/1322275371/photo/goal-achievement.webp", use_container_width=True)
    
    st.markdown("""
        <div class='box'>
        ✅ **Embrace Challenges**: View obstacles as learning opportunities.  
        ✅ **Learn from Mistakes**: Every failure is a stepping stone to success.  
        ✅ **Stay Persistent**: Keep pushing forward no matter what.  
        ✅ **Celebrate Progress**: Every step counts toward growth!  
        </div>
    """, unsafe_allow_html=True)

# Progress Tracker
elif page == "📊 Progress Tracker":
    st.markdown("<div class='subtitle'>📊 Track Your Growth Journey</div>", unsafe_allow_html=True)
    
    x = np.arange(1, 11)
    y = np.random.randint(10, 100, size=10)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Days")
    ax.set_ylabel("Growth Level")
    st.pyplot(fig)
    
    if st.button("Celebrate Progress! 🎈"):
        st.balloons()

# Daily Motivation
elif page == "💡 Daily Motivation":
    st.markdown("<div class='subtitle'>💡 Your Daily Growth Booster</div>", unsafe_allow_html=True)
    
    quotes = [
        "Success is not final, failure is not fatal: it is the courage to continue that counts.", 
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Believe in yourself and all that you are. Know that there is something inside you greater than any obstacle.",
        "Growth and comfort do not coexist.",
        "Difficulties in life are intended to make us better, not bitter."
    ]
    st.markdown(f"<div class='box'><b>{random.choice(quotes)}</b></div>", unsafe_allow_html=True)

# Success Stories
elif page == "📖 Success Stories":
    st.markdown("<div class='subtitle'>📖 Learn from Real-Life Growth Mindsets</div>", unsafe_allow_html=True)
    
    stories = [
        ("💡 **Thomas Edison**", "Failed 1,000 times before inventing the light bulb."),
        ("🌍 **Oprah Winfrey**", "Overcame rejection to build a media empire."),
        ("🎶 **Eminem**", "Was rejected multiple times before becoming a rap legend."),
        ("🏀 **Michael Jordan**", "Was cut from his basketball team but became a legend."),
    ]
    
    for name, story in stories:
        st.markdown(f"<div class='box'><b>{name}</b><br>{story}</div>", unsafe_allow_html=True)

# Goal Setter
elif page == "🎯 Goal Setter":
    st.markdown("<div class='subtitle'>🎯 Set & Achieve Your Growth Goals</div>", unsafe_allow_html=True)
    
    goal = st.text_input("📝 Your Goal:")
    deadline = st.date_input("📅 Set a Deadline:")
    
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# Reflection Journal
elif page == "📝 Reflection Journal":
    st.markdown("<div class='subtitle'>📝 Reflect on Your Growth</div>", unsafe_allow_html=True)
    
    journal_entry = st.text_area("📖 Share your thoughts & experiences:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep growing.")

# Brain Boost Exercises
elif page == "🎶 Brain Boost Exercises":
    st.markdown("<div class='subtitle'>🎶 Fun Brain Exercises for Growth</div>", unsafe_allow_html=True)
    
    puzzles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **The more you take, the more you leave behind. What am I?**", "Footsteps"),
        ("🎭 **I speak without a mouth and hear without ears. Who am I?**", "An echo"),
    ]
    
    question, answer = random.choice(puzzles)
    st.markdown(f"<div class='box'><b>{question}</b></div>", unsafe_allow_html=True)
    if st.button("Show Answer"):
        st.markdown(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🌱 *Stay Curious, Keep Growing!* 🚀")

