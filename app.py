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
st.markdown("<div class='title'>🤖 AI-Powered Success Hub</div>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("📌 Navigate")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📊 AI Progress Tracker", "💬 AI Daily Insights", "📖 AI Success Stories", "🎯 AI Goal Setter",
    "📝 AI Reflection Hub", "🎶 AI Music Generator", "📺 AI Video Recommender"
])

# Home Page
if page == "🏡 Home":
    st.markdown("""
        <div class='home-container'>
            <div class='home-title'>Welcome to AI-Powered Success Hub 🚀</div>
            <div class='home-subtext'>Harness AI to elevate your mindset, overcome hurdles, and thrive in life.</div>
            <div class='home-subtext'>✨ Let AI guide your journey to greatness! ✨</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://media.istockphoto.com/id/1322275371/photo/goal-achievement.webp", use_container_width=True)
    
    st.markdown("""
        <div class='box'>
        ✅ **Enhance Productivity**: AI-driven insights boost efficiency.  
        ✅ **Tackle Challenges Smartly**: Let AI help you navigate hurdles.  
        ✅ **Stay Inspired**: AI-generated motivation keeps you going.  
        ✅ **Achieve Your Goals**: AI optimizes your path to success!  
        </div>
    """, unsafe_allow_html=True)

# AI Progress Tracker with Balloons Effect
elif page == "📊 AI Progress Tracker":
    st.markdown("<div class='subtitle'>📊 Track Your AI-Optimized Progress</div>", unsafe_allow_html=True)
    
    x = np.arange(1, 11)
    y = np.random.randint(10, 100, size=10)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Days")
    ax.set_ylabel("Motivation Level")
    st.pyplot(fig)
    
    if st.button("Celebrate Progress! 🎈"):
        st.balloons()

# AI Daily Insights
elif page == "💬 AI Daily Insights":
    st.markdown("<div class='subtitle'>💬 Get AI-Powered Inspiration</div>", unsafe_allow_html=True)
    
    quotes = [
        "Your potential is limitless!", 
        "Every step forward is progress.",
        "Believe in yourself and take action.",
        "Dream big, work hard, stay focused.",
        "Challenges are opportunities in disguise.",
        "Success comes to those who persist."
    ]
    st.markdown(f"<div class='box'><b>{random.choice(quotes)}</b></div>", unsafe_allow_html=True)

# AI Success Stories
elif page == "📖 AI Success Stories":
    st.markdown("<div class='subtitle'>📖 Learn from AI-Powered Achievements</div>", unsafe_allow_html=True)
    
    stories = [
        ("💡 **Elon Musk & AI**", "Using AI to innovate Tesla & SpaceX."),
        ("🏀 **AI in Sports**", "AI-driven analytics transforming athletes."),
        ("📚 **AI in Media**", "How AI is changing entertainment & journalism."),
        ("🚀 **AI & Business**", "Entrepreneurs using AI to scale success.")
    ]
    
    for name, story in stories:
        st.markdown(f"<div class='box'><b>{name}</b><br>{story}</div>", unsafe_allow_html=True)

# AI Goal Setter
elif page == "🎯 AI Goal Setter":
    st.markdown("<div class='subtitle'>🎯 AI-Assisted Goal Setting</div>", unsafe_allow_html=True)
    
    goal = st.text_input("📝 Your Goal:")
    deadline = st.date_input("📅 Set a Deadline:")
    
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# AI Reflection Hub
elif page == "📝 AI Reflection Hub":
    st.markdown("<div class='subtitle'>📝 AI-Powered Reflection & Growth</div>", unsafe_allow_html=True)
    
    journal_entry = st.text_area("📖 Share your thoughts & insights:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep progressing.")

# Interactive Checkbox Feature
st.markdown("### ✅ Mark Your AI-Driven Achievements")
achievements = ["Completed a daily challenge", "Read an AI success story", "Set a new AI-powered goal", "Reflected on AI-driven progress"]
checkbox_states = {}

for achievement in achievements:
    checkbox_states[achievement] = st.checkbox(achievement)

# Footer
st.markdown("---")
st.markdown("🔥 *Stay Inspired with AI, Stay Focused!* 🚀")

    
