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

# Home Page
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
        "Coding": "Coding is an essential skill that helps you build websites, applications, and automate tasks.",
        "Writing": "Writing improves communication skills and is essential for storytelling and professional growth.",
        "Public Speaking": "Public speaking boosts confidence and helps you communicate ideas effectively.",
        "Graphic Design": "Graphic design enables you to create visually appealing content for branding and marketing.",
        "Finance": "Financial literacy is key to managing personal finances and making smart investments."
    }
    
    chosen_category = st.selectbox("Select a skill to explore:", list(categories.keys()))
    st.write(f"**{chosen_category}**: {categories[chosen_category]}")
    st.image(f"https://source.unsplash.com/400x300/?{chosen_category}", caption=chosen_category)

# Learning Goals
elif page == "🎯 Learning Goals":
    st.header("🎯 Set Your Learning Goals")
    goal = st.text_input("📝 Enter your learning goal:")
    deadline = st.date_input("📅 Set a deadline:")
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}!")

# Progress Tracker
elif page == "📊 Progress Tracker":
    st.header("📊 Track Your Learning Progress")
    progress = st.slider("How much progress have you made in your skill (0-100%)?", 0, 100, 50)
    st.write(f"You're {progress}% done! Keep going! 🚀")
    
    if st.button("🎈 Celebrate Progress!"):
        st.balloons()

# Daily Challenges with Interactive Features
elif page == "💡 Daily Challenges":
    st.header("💡 Take a Daily Learning Challenge")
    
    challenge_categories = {
        "Coding": [
            "Write a Python script that prints Fibonacci numbers.",
            "Build a simple calculator using Python.",
            "Create a to-do list app with a GUI framework."
        ],
        "Writing": [
            "Write a 500-word article on AI in daily life.",
            "Summarize a TED talk in 200 words.",
            "Write a short story based on a random prompt."
        ],
        "Public Speaking": [
            "Record a 2-minute speech on an inspiring topic.",
            "Practice storytelling for 5 minutes.",
            "Explain a concept in 60 seconds without filler words."
        ],
        "Graphic Design": [
            "Create a social media post using Canva.",
            "Design a simple logo for a fictional brand.",
            "Make a poster promoting environmental awareness."
        ],
        "Finance": [
            "Make a budget plan for a month.",
            "Read about stock market basics and write a summary.",
            "Track your expenses for the next 3 days."
        ]
    }
    
    category = st.selectbox("Select a challenge category:", list(challenge_categories.keys()))
    
    if st.button("Get Challenge"):
        challenge = random.choice(challenge_categories[category])
        st.write(f"### Your Challenge: {challenge}")
    
    st.write("\n---\n")
    
    st.subheader("📝 Submit Your Challenge Work")
    work_submission = st.text_area("Describe your work or submit code:")
    uploaded_file = st.file_uploader("Upload proof (image, text, or document)")
    
    if st.button("Submit Challenge"):
        if work_submission or uploaded_file:
            st.success("✅ Your challenge submission has been received! Keep learning!")
        else:
            st.warning("⚠️ Please provide a description or upload a file before submitting.")

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
