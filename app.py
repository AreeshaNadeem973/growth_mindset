import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Custom Styling
st.markdown("""
    <style>
        .main-container {text-align: center; padding: 50px; background: linear-gradient(to right, #ff758c, #ff7eb3); border-radius: 12px; color: white;}
        .main-title {font-size: 42px; font-weight: bold; margin-bottom: 10px;}
        .main-subtext {font-size: 22px; margin-bottom: 20px;}
        .highlight {color: #ffeb3b; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("📚 Explore Sections")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📖 Skill Categories", "🎯 Learning Goals", "📊 Progress Tracker", "💡 Daily Challenges",
    "📚 Resource Library", "💬 Discussion Forum"
])

# Home Page (Welcome Message Only Here)
if page == "🏡 Home":
    st.markdown("""
        <div class='main-container'>
        <div class='main-title'>Welcome to Skill Learning Hub 🎓</div>
        <div class='main-subtext'>Boost your knowledge, one skill at a time!</div>
        <div class='main-subtext'>🚀 Learn, track, and master new skills efficiently.</div>
        </div>
    """, unsafe_allow_html=True)

# Skill Categories
elif page == "📖 Skill Categories":
    st.header("📖 Explore Different Skills")
    categories = {
        "Coding": ("Master programming languages and build projects.", "https://www.python.org/static/community_logos/python-logo.png"),
        "Writing": ("Enhance your writing skills for blogs, books, and more.", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Pencil_icon.svg/1024px-Pencil_icon.svg.png"),
        "Public Speaking": ("Improve your confidence in speaking to audiences.", "https://upload.wikimedia.org/wikipedia/commons/8/8e/PublicSpeaking.jpg"),
        "Graphic Design": ("Create stunning visuals and designs.", "https://upload.wikimedia.org/wikipedia/commons/6/6a/Graphic_Design_Tools.jpg"),
        "Finance": ("Learn about managing money and investments.", "https://upload.wikimedia.org/wikipedia/commons/1/1a/Finance.png")
    }
    chosen_category = st.selectbox("Select a skill to explore:", list(categories.keys()))
    st.write(f"### {chosen_category}")
    st.write(categories[chosen_category][0])
    st.image(categories[chosen_category][1], use_column_width=True)

# Learning Goals
elif page == "🎯 Learning Goals":
    st.header("🎯 Set Your Learning Goals")
    goal = st.text_input("📝 Enter your learning goal:")
    deadline = st.date_input("📅 Set a deadline:")
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}!")

# Progress Tracker with Balloons
elif page == "📊 Progress Tracker":
    st.header("📊 Track Your Learning Progress")
    progress = st.slider("How much progress have you made? (0-100%)", 0, 100, 50)
    st.write(f"You're {progress}% done! Keep going! 🚀")
    if st.button("🎈 Celebrate Progress!"):
        st.balloons()

# Daily Challenges with Quiz
elif page == "💡 Daily Challenges":
    st.header("💡 Take a Daily Learning Challenge")
    challenge_categories = {
        "Coding": [
            ("What does 'print' do in Python?", ["Displays output", "Reads input", "Runs a loop"], "Displays output"),
            ("Which symbol is used for comments in Python?", ["//", "#", "/* */"], "#")
        ],
        "Writing": [
            ("What is the main purpose of an essay?", ["To entertain", "To inform", "To confuse"], "To inform")
        ]
    }
    category = st.selectbox("Select a challenge category:", list(challenge_categories.keys()))
    challenge = random.choice(challenge_categories[category])
    st.write(f"### {challenge[0]}")
    answer = st.radio("Choose an answer:", challenge[1])
    if st.button("Submit Answer"):
        if answer == challenge[2]:
            st.success("🎉 Correct!")
        else:
            st.error("❌ Incorrect. Try again!")

# Resource Library
elif page == "📚 Resource Library":
    st.header("📚 Explore Learning Resources")
    resources = {
        "Coding": "https://www.freecodecamp.org/",
        "Writing": "https://www.grammarly.com/blog/",
        "Public Speaking": "https://www.ted.com/talks",
        "Graphic Design": "https://www.canva.com/",
        "Finance": "https://www.investopedia.com/"
    }
    for skill, link in resources.items():
        st.markdown(f"✅ [{skill}]({link})")

# Discussion Forum
elif page == "💬 Discussion Forum":
    st.header("💬 Share Your Learning Journey")
    discussion = st.text_area("📝 What's something new you've learned recently?")
    if st.button("Post"):
        st.success("✅ Your response has been shared!")
