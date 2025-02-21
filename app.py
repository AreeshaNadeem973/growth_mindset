import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Mindset Growth Lab: Unlock Your Potential", page_icon="🧠")

# Sidebar for Navigation
st.sidebar.header("🚀 Explore & Elevate")
page = st.sidebar.radio("Jump to:", [
    "🏡 Home", "🎯 Success Roadmap", "💡 Daily Inspiration", "📚 Legendary Stories",
    "📈 Master Your Skills", "🧠 Mindset Growth Lab", "🤝 Community & Networking", "🎮 Brain Boosters"
])

# Home Page
if page == "🏡 Home":
    st.title("🔥 Future Leaders Hub: Empower, Innovate & Grow")
    st.header("Welcome to Future Leaders Hub! 🌍✨")
    st.markdown("""
    ### Why Join the Movement?
    🔥 **Fuel Your Ambition**: Daily wisdom to keep you inspired.  
    🚀 **Develop Winning Habits**: Small actions lead to massive results.  
    🎯 **Achieve & Dominate Goals**: Turn ideas into reality.  
    🧠 **Adopt a Growth Mindset**: Keep evolving & leading!  
    """)
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg", use_container_width=True)
    st.success("Today is YOUR day! Take charge and make an impact! 🌟")
    
    # Add a motivational quote of the day
    quotes = [
        "Your limitation—it’s only your imagination!", 
        "Push yourself, because no one else will do it for you.", 
        "Dream it. Believe it. Build it.", 
        "Success doesn’t just find you. You have to go out and get it!"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Mindset Growth Lab Page
elif page == "🧠 Mindset Growth Lab":
    st.header("🧠 Mindset Growth Lab: Unlock Your Full Potential")
    st.markdown("""
    ✅ **Daily Mindset Challenge** – Improve your thinking with small daily exercises.  
    ✅ **Mindset Reflection Journal** – Track your thoughts & personal growth.  
    ✅ **Reframe Negative Thoughts** – Convert negative thoughts into positive affirmations.  
    ✅ **Growth Tracker Graph** – Visualize your mindset progress over time.  
    """)
    
    # Reframe Negative Thoughts
    st.subheader("🔄 Reframe Your Negative Thoughts")
    negative_thought = st.text_input("Write a negative thought you're struggling with:")
    if negative_thought:
        positive_reframes = [
            "Every challenge is an opportunity to grow!", 
            "I am learning and improving every day!", 
            "Mistakes help me become better!", 
            "I am capable and strong!"
        ]
        st.success(f"💡 **Reframed Thought:** {random.choice(positive_reframes)}")
    
    # Growth Tracker Graph
    st.subheader("📊 Mindset Strength Growth Tracker")
    mindset_areas = ["Self-Belief", "Resilience", "Optimism", "Discipline", "Focus"]
    growth_scores = np.random.randint(50, 100, size=len(mindset_areas))
    
    fig, ax = plt.subplots()
    ax.bar(mindset_areas, growth_scores, color=['blue', 'green', 'orange', 'red', 'purple'])
    ax.set_title("Mindset Growth Progress")
    ax.set_ylabel("Growth Score (%)")
    ax.set_ylim(0, 100)
    
    st.pyplot(fig)
    
    st.success("Keep strengthening your mindset—progress is key to success! 🚀")

# Master Your Skills Page
elif page == "📈 Master Your Skills":
    st.header("📈 Elevate Your Skills & Track Progress")
    st.markdown("""
    🔥 **Sharpen Your Expertise**: Learn, practice, and grow.  
    📊 **Measure Your Growth**: Track skill development over time.  
    """)
    
    # Add a graph to visualize skill progress
    skills = ["Leadership", "Creativity", "Discipline", "Networking", "Resilience"]
    progress = np.random.randint(50, 100, size=len(skills))
    
    fig, ax = plt.subplots()
    ax.bar(skills, progress, color=['blue', 'green', 'orange', 'red', 'purple'])
    ax.set_title("Skill Development Progress")
    ax.set_ylabel("Progress (%)")
    ax.set_ylim(0, 100)
    
    st.pyplot(fig)
    
    st.success("Keep building your skills—growth is a continuous journey! 🚀")

 
