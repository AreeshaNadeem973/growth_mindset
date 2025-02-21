import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# Custom Styling
st.markdown("""
    <style>
        .title {color: #ff4500; text-align: center; font-size: 42px; font-weight: bold;}
        .subtitle {color: #2e8b57; text-align: center; font-size: 22px;}
        .box {background: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); text-align: center;}
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.header("📌 Navigate")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📊 AI Progress Tracker", "💬 AI Daily Insights", "📖 AI Success Stories", "🎯 AI Goal Setter",
    "📝 AI Reflection Hub", "📚 Code Learning Hub", "💡 Discussion Forum"
])

# Home Page
if page == "🏡 Home":
    st.markdown("<div class='title'>🤖 Welcome to AI Success Hub</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Harness AI to achieve your goals!</div>", unsafe_allow_html=True)
    st.image("https://media.istockphoto.com/id/1322275371/photo/goal-achievement.webp", use_container_width=True)

# AI Progress Tracker
elif page == "📊 AI Progress Tracker":
    st.markdown("<div class='title'>📊 AI Progress Tracker</div>", unsafe_allow_html=True)
    days = np.arange(1, 11)
    motivation = np.random.randint(50, 100, size=10)
    fig, ax = plt.subplots()
    ax.plot(days, motivation, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Days")
    ax.set_ylabel("Motivation Level")
    ax.set_title("Your AI-Powered Progress")
    st.pyplot(fig)
    if st.button("Celebrate Your Progress! 🎈"):
        for _ in range(3):
            st.balloons()
            time.sleep(0.5)

# AI Daily Insights
elif page == "💬 AI Daily Insights":
    st.markdown("<div class='title'>💬 AI Daily Insights</div>", unsafe_allow_html=True)
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
    st.markdown("<div class='title'>📖 AI Success Stories</div>", unsafe_allow_html=True)
    stories = [
        ("💡 Elon Musk & AI", "Using AI to innovate Tesla & SpaceX."),
        ("🏀 AI in Sports", "AI-driven analytics transforming athletes."),
        ("📚 AI in Media", "How AI is changing entertainment & journalism."),
        ("🚀 AI & Business", "Entrepreneurs using AI to scale success.")
    ]
    for name, story in stories:
        st.markdown(f"<div class='box'><b>{name}</b><br>{story}</div>", unsafe_allow_html=True)

# AI Goal Setter
elif page == "🎯 AI Goal Setter":
    st.markdown("<div class='title'>🎯 AI Goal Setter</div>", unsafe_allow_html=True)
    goal = st.text_input("📝 Your Goal:")
    deadline = st.date_input("📅 Set a Deadline:")
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# AI Reflection Hub
elif page == "📝 AI Reflection Hub":
    st.markdown("<div class='title'>📝 AI Reflection Hub</div>", unsafe_allow_html=True)
    journal_entry = st.text_area("📖 Share your thoughts & insights:")
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep progressing.")

# Code Learning Hub
elif page == "📚 Code Learning Hub":
    st.markdown("<div class='title'>📚 Code Learning Hub</div>", unsafe_allow_html=True)
    st.markdown("Improve your coding skills with these resources:")
    coding_resources = [
        "- [Python for Beginners](https://www.python.org/about/gettingstarted/)",
        "- [JavaScript Basics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)",
        "- [Data Science with Python](https://www.datacamp.com/)",
        "- [Machine Learning with TensorFlow](https://www.tensorflow.org/tutorials)"
    ]
    for res in coding_resources:
        st.markdown(res)

# Discussion Forum
elif page == "💡 Discussion Forum":
    st.markdown("<div class='title'>💡 AI Discussion Forum</div>", unsafe_allow_html=True)
    st.markdown("Connect with fellow AI enthusiasts:")
    discussion = st.text_area("💬 Share your thoughts & questions:")
    if st.button("Post Discussion"):
        st.success("💡 Discussion posted! Engage with the community.")

# Footer
st.markdown("---")
st.markdown("🔥 *Stay Inspired with AI, Stay Focused!* 🚀")
