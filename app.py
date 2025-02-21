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
    st.markdown("### 🌟 Why Learn a New Skill?")
    benefits = [
        "🚀 Expand your career opportunities",
        "📚 Enhance creativity & problem-solving",
        "💡 Boost confidence & personal growth",
        "🎯 Stay ahead in a competitive world"
    ]
    for benefit in benefits:
        st.write(f"✅ {benefit}")
    
    st.markdown("### 🔥 Today's Learning Tip")
    tips = [
        "Break your learning into small chunks for better retention!",
        "Practice makes perfect – keep experimenting!",
        "Teach someone what you learn – it strengthens your knowledge!",
        "Stay consistent, even if you learn for just 10 minutes a day."
    ]
    st.write(random.choice(tips))

# Skill Categories
elif page == "📖 Skill Categories":
    st.header("📖 Explore Different Skills")
    categories = ["Coding", "Writing", "Public Speaking", "Graphic Design", "Photography", "Marketing", "Finance"]
    chosen_category = st.selectbox("Select a skill to explore:", categories)
    st.write(f"You selected: **{chosen_category}**")

# Learning Goals
elif page == "🎯 Learning Goals":
    st.header("🎯 Set Your Learning Goals")
    goal = st.text_input("📝 Enter your learning goal:")
    deadline = st.date_input("📅 Set a deadline:")
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}!")

# Progress Tracker with Animated Balloons and Enhanced Graph
elif page == "📊 Progress Tracker":
    st.header("📊 Track Your Learning Progress")
    progress = st.slider("How much progress have you made in your skill (0-100%)?", 0, 100, 50)
    st.write(f"You're {progress}% done! Keep going! 🚀")
    
    # Enhanced Graph with Animation Effect
    x = np.arange(1, 11)
    y = np.random.randint(10, 100, size=10)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', linestyle='-', color='blue', label='Learning Progress')
    ax.set_xlabel("Days")
    ax.set_ylabel("Skill Mastery (%)")
    ax.set_title("Learning Progress Over Time")
    ax.legend()
    st.pyplot(fig)
    
    # Create a button to trigger balloon animation
    if st.button("🎈 Celebrate Progress!"):
        st.write("🎉 Balloons are rising to celebrate your progress!")
        st.balloons()

# Daily Challenges
elif page == "💡 Daily Challenges":
    st.header("💡 Take a Daily Learning Challenge")
    challenges = [
        "Write a 500-word article on a topic of your choice.",
        "Code a simple calculator in Python.",
        "Give a 2-minute speech on an interesting fact.",
        "Design a creative social media post in Canva.",
        "Read a book summary and take notes."
    ]
    st.write(random.choice(challenges))

# Resource Library
elif page == "📚 Resource Library":
    st.header("📚 Explore Learning Resources")
    resources = {
        "Coding": "[FreeCodeCamp](https://www.freecodecamp.org/)",
        "Writing": "[Grammarly Blog](https://www.grammarly.com/blog/)",
        "Public Speaking": "[TED Talks](https://www.ted.com/talks)",
        "Graphic Design": "[Canva](https://www.canva.com/)",
        "Finance": "[Investopedia](https://www.investopedia.com/)"
    }
    for skill, link in resources.items():
        st.markdown(f"✅ [{skill}]({link})")

# Discussion Forum
elif page == "💬 Discussion Forum":
    st.header("💬 Share Your Learning Journey")
    discussion = st.text_area("📝 What's something new you've learned recently?")
    if st.button("Post"):
        st.success("✅ Your response has been shared!")

   
