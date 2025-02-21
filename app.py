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
        "Coding": ("Learn programming languages like Python, Java, and more to build applications and software.", "https://upload.wikimedia.org/wikipedia/commons/3/3a/Neural_Network.svg"),
        "Writing": ("Enhance your writing skills for blogging, content creation, and storytelling.", "https://upload.wikimedia.org/wikipedia/commons/6/69/Writing.svg"),
        "Public Speaking": ("Improve your speaking skills to communicate effectively and confidently.", "https://upload.wikimedia.org/wikipedia/commons/a/a3/Public_speaking.svg"),
        "Graphic Design": ("Master tools like Photoshop and Canva to create visually stunning designs.", "https://upload.wikimedia.org/wikipedia/commons/4/4e/Graphic_design.svg"),
        "Photography": ("Learn the art of capturing beautiful moments and editing photos.", "https://upload.wikimedia.org/wikipedia/commons/3/3f/Photography.svg"),
        "Marketing": ("Understand digital marketing, branding, and social media strategies.", "https://upload.wikimedia.org/wikipedia/commons/e/e6/Marketing.svg"),
        "Finance": ("Gain knowledge in financial management, investment, and wealth building.", "https://upload.wikimedia.org/wikipedia/commons/8/88/Finance.svg")
    }
    chosen_category = st.selectbox("Select a skill to explore:", list(categories.keys()))
    
    if chosen_category:
        st.subheader(chosen_category)
        st.write(categories[chosen_category][0])
        st.image(categories[chosen_category][1], use_column_width=True)

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



   
