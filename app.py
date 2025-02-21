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
        .box {background: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); text-align: center;}
        .home-container {text-align: center; padding: 40px; background: linear-gradient(to right, #ff9a9e, #fad0c4); border-radius: 12px; color: white;}
        .home-title {font-size: 40px; font-weight: bold; margin-bottom: 10px;}
        .home-subtext {font-size: 20px; margin-bottom: 20px;}
        .highlight {color: #ff4500; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>🚀 Personal Growth & Productivity Hub</div>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("🌍 Explore")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📊 Productivity Tracker", "💡 Daily Motivation", "📖 Success Stories", "🎯 Goal Setter",
    "📝 Reflection Journal", "🧠 Brain Boost"
])

# Home Page
if page == "🏡 Home":
    st.markdown("""
        <div class='home-container'>
            <div class='home-title'>Welcome to Your Productivity Hub 💪</div>
            <div class='home-subtext'>Boost your focus, stay consistent, and achieve your dreams.</div>
            <div class='home-subtext'>🚀 Let's grow and improve every day!</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://www.success.com/wp-content/uploads/legacy/sites/default/files/new3.jpg", use_container_width=True)
    
    st.markdown("""
        <div class='box'>
        ✅ **Track Your Progress**: Stay consistent with daily habits.  
        ✅ **Stay Motivated**: Get fresh daily motivation and success tips.  
        ✅ **Set Goals**: Define and achieve smart personal goals.  
        ✅ **Challenge Your Mind**: Engage in brain-boosting activities.  
        </div>
    """, unsafe_allow_html=True)

# Productivity Tracker
elif page == "📊 Productivity Tracker":
    st.header("📊 Track Your Productivity")
    days = st.slider("How many days have you been consistent?", 1, 30, 5)
    effort = st.slider("How much effort do you put in (1-10)?", 1, 10, 7)
    
    fig, ax = plt.subplots()
    ax.bar(["Days", "Effort"], [days, effort], color=["blue", "green"])
    ax.set_ylabel("Progress Level")
    st.pyplot(fig)

# Daily Motivation
elif page == "💡 Daily Motivation":
    st.header("💡 Get Your Daily Dose of Motivation")
    tips = [
        "🚀 Keep pushing forward! Your efforts matter.",
        "🎯 Every small step brings you closer to success.",
        "💡 Learning from mistakes makes you stronger.",
        "🔥 Challenge yourself today to become better tomorrow."
    ]
    st.write(random.choice(tips))

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Real-Life Success Stories")
    stories = [
        ("📚 **J.K. Rowling**", "From struggling single mother to one of the world's best-selling authors."),
        ("💼 **Elon Musk**", "From failed startups to revolutionizing multiple industries."),
        ("🏃 **David Goggins**", "Overcame incredible odds to become an ultra-endurance athlete.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setter
elif page == "🎯 Goal Setter":
    st.header("🎯 Set Your Goals & Achieve More")
    goal = st.text_input("📝 Enter your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}!")

# Reflection Journal
elif page == "📝 Reflection Journal":
    st.header("📝 Daily Reflection Journal")
    journal = st.text_area("📖 Share your thoughts and progress:")
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep growing.")

# Brain Boost
elif page == "🧠 Brain Boost":
    st.header("🧠 Daily Brain Challenge")
    riddles = [
        ("🤔 **The more you use me, the sharper I get. What am I?**", "Your brain"),
        ("📖 **I can fill a room but take up no space. What am I?**", "Knowledge"),
        ("💡 **I grow the more you share me. What am I?**", "Happiness")
    ]
    question, answer = random.choice(riddles)
    st.write(question)
