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

# Skill Categories with Detailed Information
elif page == "📖 Skill Categories":
    st.header("📖 Explore Different Skills")
    categories = {
        "Coding": ("Learn programming from scratch and build real-world applications.", "https://upload.wikimedia.org/wikipedia/commons/3/39/Programming_languages.jpeg"),
        "Writing": ("Enhance your writing skills to communicate effectively and creatively.", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Writing_1.jpg/800px-Writing_1.jpg"),
        "Public Speaking": ("Master the art of speaking confidently in front of an audience.", "https://upload.wikimedia.org/wikipedia/commons/1/13/Public_Speaking.jpg"),
        "Graphic Design": ("Learn to create visually appealing content using design tools.", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Graphic_Design.jpg/800px-Graphic_Design.jpg"),
        "Finance": ("Understand financial concepts to manage money wisely.", "https://upload.wikimedia.org/wikipedia/commons/1/19/Financial_Charts.jpg")
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

# Progress Tracker with Animated Balloons
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
    
    completed = st.checkbox("Mark as Completed")
    
    if completed:
        st.success("🎉 Well done! You've completed the challenge!")
        uploaded_file = st.file_uploader("Upload proof (image, text, or document)")
        if uploaded_file:
            st.write("✅ Proof uploaded successfully!")

# Resource Library with Valid URLs
elif page == "📚 Resource Library":
    st.header("📚 Explore Learning Resources")
    resources = {
        "Coding": "https://www.freecodecamp.org/",
        "Writing": "https://www.grammarly.com/blog/",
        "Public Speaking": "https://www.toastmasters.org/",
        "Graphic Design": "https://www.canva.com/",
        "Finance": "https://www.investopedia.com/"
    }
    
    for skill, link in resources.items():
        st.markdown(f"✅ [{skill}]({link})", unsafe_allow_html=True)

# Discussion Forum
elif page == "💬 Discussion Forum":
    st.header("💬 Share Your Learning Journey")
    discussion = st.text_area("📝 What's something new you've learned recently?")
    if st.button("Post"):
        st.success("✅ Your response has been shared!")
