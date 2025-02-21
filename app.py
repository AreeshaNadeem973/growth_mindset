import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from datetime import date

# App Title
st.set_page_config(page_title="Rise & Thrive: Unlock Your Potential", page_icon="🔥")
st.title("🔥 Rise & Thrive: Unlock Your Potential")

# Sidebar for Navigation
st.sidebar.header("🚀 Explore")
page = st.sidebar.radio("Choose a Section:", [
    "🏠 Home", "📅 Habit Builder", "🌟 Daily Boost", "📚 Inspiring Journeys",
    "🎯 Goal Mastery", "⚡ Productivity Hacks", "💡 Mind Expansion", "🔎 Brain Boost", "🚀 Limitless Growth"
])

# Home Page
if page == "🏠 Home":
    st.header("Welcome to Rise & Thrive! 🌟")
    st.markdown("""
    **Why This Matters?**  
    ✅ **Fuel Your Ambition** – Start each day with energy.  
    ✅ **Create Powerful Habits** – Small actions, massive impact.  
    ✅ **Crush Your Goals** – Turn vision into success.  
    ✅ **Adopt a Limitless Mindset** – Keep evolving & winning!  
    """)
    
    st.image("https://source.unsplash.com/800x400/?success,motivation", use_column_width=True)
    
    st.success("Every day is a chance to level up. Let’s make it count! 🚀")
    
    # Motivational Quote of the Day
    quotes = [
        "Dream big, work hard, stay focused, and surround yourself with good people.",
        "Your potential is endless. Keep going!", 
        "Success isn’t about luck; it’s about consistency and effort.",
        "Make today so awesome that yesterday gets jealous.",
        "The harder you work for something, the greater you’ll feel when you achieve it."
    ]
    st.info(f"💡 **Today's Quote:** {random.choice(quotes)}")

# Habit Builder
elif page == "📅 Habit Builder":
    st.header("📅 Build Winning Habits")
    habits = ["Workout", "Read 10 Pages", "Meditate", "Drink Water", "Journal Thoughts"]
    
    for habit in habits:
        st.checkbox(f"Completed: {habit}")
    
    if st.button("Save Progress ✅"):
        st.success("Great job! Keep pushing forward!")
        st.balloons()

    # Habit Progress Graph
    progress = np.random.randint(2, 7, size=len(habits))
    fig, ax = plt.subplots()
    ax.bar(habits, progress, color='skyblue')
    ax.set_title("Your Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)

# Daily Boost
elif page == "🌟 Daily Boost":
    st.header("🌟 Elevate Your Energy")
    
    energy_levels = st.slider("How energized do you feel today?", 0, 100, 50)
    fig, ax = plt.subplots()
    ax.bar(["Energy Level"], [energy_levels], color='gold')
    ax.set_ylim(0, 100)
    st.pyplot(fig)
    
    st.markdown("🔥 Tip: Move your body, get some fresh air, and hydrate!")

# Inspiring Journeys
elif page == "📚 Inspiring Journeys":
    st.header("📚 Real Success Stories")
    
    people = [
        ("⚡ **Oprah Winfrey**", "From rejection to global media icon."),
        ("🚀 **Jeff Bezos**", "Started Amazon in a garage, changed the world."),
        ("🏀 **Kobe Bryant**", "Relentless work ethic turned him into a legend."),
        ("🎶 **Eminem**", "Overcame struggle to become a music icon."),
    ]
    
    for name, story in people:
        st.subheader(name)
        st.write(story)

# Goal Mastery
elif page == "🎯 Goal Mastery":
    st.header("🎯 Define & Crush Your Goals")
    
    goal = st.text_input("What's a major goal you're working on?")
    steps = st.text_area("Steps to achieve this goal:")
    
    if st.button("Save Goal 🎯"):
        st.success("Your goal is set! Time to execute.")
        st.balloons()

# Productivity Hacks
elif page == "⚡ Productivity Hacks":
    st.header("⚡ Work Smarter, Not Harder")
    
    tips = [
        "Time block your day for efficiency.",
        "Avoid distractions by setting app limits.",
        "Use the 2-minute rule—if it takes less than 2 minutes, do it now!",
        "Take strategic breaks to refresh your mind.",
    ]
    st.write(f"💡 **Hack of the Day:** {random.choice(tips)}")

# Mind Expansion
elif page == "💡 Mind Expansion":
    st.header("💡 Expand Your Knowledge")
    
    challenge = random.choice([
        "Try a new skill today.",
        "Write down one big idea you have.",
        "Watch a TED Talk on something unfamiliar.",
        "Read about an inspiring leader.",
        "Teach something new to someone today."
    ])
    st.write(f"🌟 **Today's Challenge:** {challenge}")
    
    if st.button("Accept Challenge ✅"):
        st.success("You're on your way to leveling up!")
        st.balloons()

# Brain Boost
elif page == "🔎 Brain Boost":
    st.header("🔎 Sharpen Your Thinking")
    
    puzzles = [
        ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "A candle"),
        ("What has hands but can’t clap?", "A clock"),
        ("What has a head, a tail, but no body?", "A coin"),
    ]
    
    q, a = random.choice(puzzles)
    st.write(f"🤔 **Riddle:** {q}")
    ans = st.text_input("Your answer:")
    
    if st.button("Check Answer"):
        if ans.lower() == a.lower():
            st.success("Correct! 🎉")
            st.balloons()
        else:
            st.error(f"Not quite. The correct answer is: {a}")

# Limitless Growth
elif page == "🚀 Limitless Growth":
    st.header("🚀 The Power of a Growth Mindset")
    
    mindset = st.radio("Do you believe you can always improve?", ["Yes", "No"])
    if mindset == "Yes":
        st.success("That’s the spirit! Keep growing! 🌱")
    else:
        st.warning("Challenge your limits, don’t limit your challenges.")
    
    if st.button("Start Growth Challenge 🚀"):
        st.success("You’ve taken the first step towards limitless potential!")
        st.balloons()

# Footer
st.markdown("---")
st.markdown("Made with ❤️ to empower the next-gen achievers. 🚀")
