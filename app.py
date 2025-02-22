import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="The Success Blueprint", page_icon="🚀")
st.title("🚀 The Success Blueprint: Mindset, Habits & Innovation")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Power Habits", "💡 Success Mindset", "📖 Innovation Stories",
    "🎯 Goal Mastery", "📝 Productivity Hacks", "🤔 Self-Reflection", "🧠 Brain Fuel"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to The Success Blueprint! 🚀")
    
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg", use_container_width=True)

    st.markdown("""
    ### Why Focus on Mindset, Habits & Innovation?
    ✅ **Cultivate a Growth Mindset**: Success starts in the mind.  
    ✅ **Master High-Performance Habits**: Small daily actions lead to great results.  
    ✅ **Innovate for a Competitive Edge**: Creativity fuels success.  
    ✅ **Achieve Your Goals**: Make dreams a reality with smart strategies!  
    """)
    st.success("Your journey to success begins today! Keep pushing forward! 🚀")
    
    # Success Quote of the Day
    quotes = [
        "Your mindset is the key to your success. - Unknown",
        "Discipline is the bridge between goals and accomplishment. - Jim Rohn",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Opportunities don’t happen. You create them. - Chris Grosser"
    ]
    st.info(f"💡 **Success Quote of the Day:** {random.choice(quotes)}")

# Power Habits
elif page == "📅 Power Habits":
    st.header("📅 Power Habits for Success")
    habits = ["Morning Exercise", "Deep Work", "Reading", "Networking", "Learning Something New"]

    for habit in habits:
        st.checkbox(f"Did you practice {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Consistency is key!")
        st.balloons()

    # Weekly Habit Progress Graph
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='blue')
    ax.set_title("Weekly Power Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Success Mindset
elif page == "💡 Success Mindset":
    st.header("💡 Build a Success Mindset")
    mindset_tips = [
        "🌟 *Your thoughts shape your reality.*", 
        "🚀 *Failure is feedback. Learn and grow!*", 
        "🔥 *Surround yourself with positive, driven people.*", 
        "💡 *Take massive action toward your goals!*",
        "🌱 *Challenge yourself daily to grow.*"
    ]
    st.success(f"💡 **Mindset Tip:** {random.choice(mindset_tips)}")

    # Weekly Mindset Strength Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    mindset_levels = np.random.randint(50, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, mindset_levels, marker='o', linestyle='--', color='orange')
    ax.set_title("Weekly Mindset Growth")
    ax.set_ylabel("Mindset Strength (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Innovation Stories
elif page == "📖 Innovation Stories":
    st.header("📖 Stories of Game-Changing Innovation")
    stories = [
        ("🚀 **Elon Musk**", "Revolutionized space travel and electric vehicles."),
        ("📱 **Steve Jobs**", "Redefined technology with the iPhone."),
        ("🧬 **Marie Curie**", "Pioneered research in radioactivity."),
        ("🌍 **Nikola Tesla**", "Invented AC electricity, changing the world.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Mastery
elif page == "🎯 Goal Mastery":
    st.header("🎯 Set & Master Your Goals")
    goal = st.text_input("Define your biggest goal:")
    steps = st.text_area("Steps to achieve it:")
    if st.button("Save Goal"):
        st.success("Goal saved! Take action today!")

# Productivity Hacks
elif page == "📝 Productivity Hacks":
    st.header("📝 High-Performance Productivity Hacks")
    hacks = [
        "⏳ **Time Blocking** – Allocate time for deep work.",
        "🚀 **Eat the Frog** – Do the hardest task first.",
        "📋 **Plan Tomorrow Today** – End each day with a plan.",
        "📖 **Continuous Learning** – Always sharpen your skills."
    ]
    st.write(f"💡 **Today's Hack:** {random.choice(hacks)}")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Success Reflection")
    mood = st.select_slider("How productive was your day?", options=["Low", "Average", "Great", "Excellent"])
    st.write(f"Your day was: {mood}")
    if st.button("Save Reflection"):
        st.success("Reflection saved! Keep evolving!")

# Brain Fuel
elif page == "🧠 Brain Fuel":
    st.header("🧠 Brain-Boosting Challenges")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg")
    ]
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    user_answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! Keep that brain sharp!")
            st.balloons()
        else:
            st.error(f"Not quite. The answer is: {answer}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 The Success Blueprint")

