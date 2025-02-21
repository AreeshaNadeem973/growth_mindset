import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import date

# App Configuration
st.set_page_config(page_title="Limitless Growth Hub 🚀", page_icon="🔥")
st.title("🚀 Limitless Growth Hub - Unlock Your Potential")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "🎯 Goal Setting", "📝 Productivity Hacks", "💡 Growth Mindset",
    "📅 Habit Tracker", "💭 Daily Motivation", "🤔 Self-Reflection", "🎮 Brain Boosters"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Limitless Growth Hub! 🌟")
    st.markdown("""
    ### Why Focus on Growth & Productivity?
    ✅ **Achieve Your Goals Faster** - Smart work over hard work.  
    ✅ **Build Life-Changing Habits** - Small steps lead to big success.  
    ✅ **Master Productivity Hacks** - Work smarter, not harder.  
    ✅ **Adopt a Growth Mindset** - Success is a continuous journey!  
    """)
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    
    # Motivational Quote of the Day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Productivity Hacks
elif page == "📝 Productivity Hacks":
    st.header("📝 Master Productivity Hacks")
    
    # 1. Task Prioritization Techniques
    st.subheader("✅ Task Prioritization Frameworks")
    st.markdown("""
    - **Eisenhower Matrix:** Urgent vs. Important Tasks
    - **Pomodoro Technique:** 25-min Work + 5-min Break
    - **80/20 Rule:** Focus on the 20% that gives 80% results
    """)
    
    # 2. AI-Powered Productivity Tools
    st.subheader("🤖 AI Productivity Tools")
    st.markdown("""
    - **Notion** for organizing tasks & knowledge.
    - **ChatGPT** for brainstorming & automation.
    - **Trello** for task & project management.
    """)
    
    # 3. Productivity Timer
    st.subheader("⏳ Focus Timer (Pomodoro)")
    minutes = st.number_input("Set Focus Timer (Minutes):", min_value=1, max_value=60, value=25)
    if st.button("Start Timer"):
        st.success("Stay focused and productive!")
        st.balloons()
    
    # 4. Daily Routine Optimization
    st.subheader("🌅 Morning & Night Routines")
    st.markdown("""
    - **Morning Routine:** Hydration, Meditation, Goal Setting
    - **Night Routine:** Reflection, Planning, Digital Detox
    """)
    
    # 5. Focus Improvement Tips
    st.subheader("📵 Digital Detox & Focus Strategies")
    st.markdown("""
    - Turn off notifications 🚫
    - Use website blockers (e.g., Freedom, Cold Turkey) ⏳
    - Practice Deep Work (90-minute focus sessions) 📖
    """)
    
    # Productivity Bar Chart (Distraction Analysis)
    categories = ["Focused Work", "Breaks", "Distractions"]
    values = [60, 25, 15]
    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['green', 'yellow', 'red'])
    ax.set_ylabel("Time Spent (%)")
    ax.set_title("How You Spend Your Day")
    st.pyplot(fig)
    
    st.success("🚀 Optimize your productivity and reach new heights!")

# Other Sections Placeholder
elif page == "🎯 Goal Setting":
    st.header("🎯 Set & Achieve Your Goals")
    st.write("Coming soon...")

elif page == "💡 Growth Mindset":
    st.header("💡 Unlock Your Growth Mindset")
    st.write("Coming soon...")

elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Habits Consistently")
    st.write("Coming soon...")

elif page == "💭 Daily Motivation":
    st.header("💭 Stay Inspired Every Day")
    st.write("Coming soon...")

elif page == "🤔 Self-Reflection":
    st.header("🤔 Reflect on Your Daily Progress")
    st.write("Coming soon...")

elif page == "🎮 Brain Boosters":
    st.header("🎮 Sharpen Your Mind with Fun Challenges")
    st.write("Coming soon...")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Limitless Growth Hub")
