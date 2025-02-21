import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random
from datetime import date

# App Title
st.set_page_config(page_title="Success & Mindset Hub", page_icon="🚀")
st.title("🚀 Success & Mindset Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Progress Tracker", "💡 Daily Wisdom", "📖 Success Stories",
    "🎯 Vision & Goals", "📈 Productivity Insights", "🧠 Mindset Growth"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Success & Mindset Hub! 🌟")
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg", use_container_width=True)
    
    st.markdown("""
    ### Why Success & Mindset Matter?
    ✅ **Build Confidence** – Believe in yourself every day.  
    ✅ **Master Productivity** – Optimize your workflow.  
    ✅ **Set Big Goals** – Transform vision into action.  
    ✅ **Develop a Winning Mindset** – Stay resilient and adaptable.  
    """)
    
    # Motivational Quote of the Day
    quotes = [
        "Success is not just about making money. It’s about making a difference.",
        "Your mindset shapes your reality. Think big!",
        "Opportunities don't happen. You create them!",
        "Don't wait for the perfect moment. Take the moment and make it perfect!"
    ]
    st.success(f"💡 **Quote of the Day:** {random.choice(quotes)}")
    
    # Weekly Motivation Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(50, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Progress Tracker
elif page == "📊 Progress Tracker":
    st.header("📊 Track Your Progress")
    habits = ["Exercise", "Read", "Learn Something New", "Meditate", "Plan Goals"]
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Progress saved! Keep pushing forward! 💪")
        st.balloons()
    
    # Weekly Progress Chart
    weekly_data = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_data.keys(), weekly_data.values(), color='green')
    ax.set_title("Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Daily Wisdom
elif page == "💡 Daily Wisdom":
    st.header("💡 Insights to Elevate Your Day")
    wisdoms = [
        "Hardships often prepare ordinary people for an extraordinary destiny.",
        "The mind is everything. What you think, you become.",
        "Take risks in life. If you win, you can lead. If you lose, you can guide.",
        "The only limit to our realization of tomorrow is our doubts of today."
    ]
    st.success(f"🌟 **Today's Wisdom:** {random.choice(wisdoms)}")
    
    # Daily Focus Chart
    focus_levels = np.random.randint(40, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, focus_levels, marker='o', linestyle='--', color='purple')
    ax.set_title("Daily Focus Levels")
    ax.set_ylabel("Focus (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Inspiring Success Stories")
    stories = [
        ("🌍 **Oprah Winfrey**", "Overcame poverty and built a media empire."),
        ("📱 **Steve Jobs**", "Revolutionized technology with Apple."),
        ("⚡ **Nikola Tesla**", "Pioneered innovations in electricity and energy."),
        ("🚀 **Elon Musk**", "Shaped the future of space travel and electric cars.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
    
    # Add Your Own Success Story
    st.subheader("Share Your Story")
    user_story = st.text_area("Your success journey:")
    if st.button("Submit Story"):
        st.success("Thanks for sharing! Your journey will inspire others! 🌟")
        st.balloons()

# Vision & Goals
elif page == "🎯 Vision & Goals":
    st.header("🎯 Define Your Vision & Goals")
    goal_types = ["Short-term", "Medium-term", "Long-term"]
    for goal in goal_types:
        goal_input = st.text_input(f"Enter a {goal.lower()} goal:")
        if goal_input:
            st.write(f"Your {goal.lower()} goal: {goal_input}")
    
    if st.button("Save Goals"):
        st.success("Goals saved successfully! Stay committed! 🚀")
        st.balloons()

# Productivity Insights
elif page == "📈 Productivity Insights":
    st.header("📈 Productivity Strategies")
    tips = [
        "🕒 Prioritize high-impact tasks.",
        "🚀 Use the Pomodoro technique to stay focused.",
        "📋 Plan your day the night before.",
        "🛑 Minimize distractions and maximize deep work time.",
        "📊 Track progress and adjust strategies accordingly."
    ]
    st.write(f"💡 **Productivity Tip of the Day:** {random.choice(tips)}")
    
    # Productivity Pie Chart
    fig, ax = plt.subplots()
    labels = ["Deep Work", "Meetings", "Breaks", "Distractions"]
    sizes = [50, 20, 20, 10]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=["green", "blue", "yellow", "red"])
    st.pyplot(fig)

# Mindset Growth
elif page == "🧠 Mindset Growth":
    st.header("🧠 Cultivating a Strong Mindset")
    challenges = [
        "Face a fear today and take action!",
        "Reframe a negative thought into a positive one.",
        "Push beyond your comfort zone for growth.",
        "Learn from a mistake and apply the lesson."
    ]
    st.write(f"🌱 **Today's Growth Challenge:** {random.choice(challenges)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Success & Mindset Hub")
