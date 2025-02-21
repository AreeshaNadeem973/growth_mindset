import streamlit as st
import random
from datetime import date

# Set Page Configuration
st.set_page_config(page_title="🚀 Peak Performance Hub", page_icon="🔥", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💡 Daily Motivation", "📖 Success Stories",
    "🎯 Goal Setting", "📝 Productivity Hacks", "🤔 Self-Reflection", "🧠 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.markdown("# 🚀 Welcome to Peak Performance Hub!")
    st.image("https://source.unsplash.com/800x400/?motivation,success", use_container_width=True)
    st.markdown(
        """
        ### Why Focus on Peak Performance?
        ✅ **Unlock Your Potential**: Stay motivated every day.
        ✅ **Build Powerful Habits**: Small steps lead to success.
        ✅ **Set & Achieve Goals**: Make your dreams a reality.
        ✅ **Develop a Growth Mindset**: Keep evolving and improving!
        """
    )
    
    # Quote of the Day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Do what you can, with what you have, where you are. - Theodore Roosevelt",
        "Opportunities don't happen, you create them. - Chris Grosser"
    ]
    st.success(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.markdown("# 📅 Track Your Habits")
    habits = ["Exercise", "Read", "Meditate", "Hydration", "Healthy Eating"]
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    if st.button("Save Progress"):
        st.success("Progress Saved! Keep going! 💪")

# Daily Motivation
elif page == "💡 Daily Motivation":
    st.markdown("# 💡 Daily Motivation")
    st.image("https://source.unsplash.com/800x400/?success,inspiration", use_container_width=True)
    st.write("### Stay Inspired Every Day!")
    st.info(f"💬 **Today's Motivation:** {random.choice(quotes)}")
    
# Success Stories
elif page == "📖 Success Stories":
    st.markdown("# 📖 Inspiring Success Stories")
    st.image("https://source.unsplash.com/800x400/?achievement,goal", use_container_width=True)
    stories = [
        ("💡 **Elon Musk**", "Revolutionized industries with Tesla, SpaceX, and Neuralink."),
        ("📚 **J.K. Rowling**", "Overcame rejection to publish Harry Potter, inspiring millions."),
        ("🏀 **Michael Jordan**", "Cut from his high school basketball team but became a legend."),
        ("🌍 **Nelson Mandela**", "Fought for justice and changed a nation."),
        ("🎶 **Ed Sheeran**", "From busking in streets to global music icon.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
        st.markdown("---")

# Goal Setting
elif page == "🎯 Goal Setting":
    st.markdown("# 🎯 Set Your Goals")
    st.image("https://source.unsplash.com/800x400/?goal,success", use_container_width=True)
    goal = st.text_input("Enter your goal:")
    steps = st.text_area("Steps to achieve your goal:")
    if st.button("Save Goal"):
        st.success("Goal saved successfully! 🚀")

# Productivity Hacks
elif page == "📝 Productivity Hacks":
    st.markdown("# 📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule focused time for tasks.",
        "📋 **Prioritize** – Use the Eisenhower Matrix to manage tasks.",
        "📵 **Limit Distractions** – Reduce social media usage.",
        "💤 **Get Enough Sleep** – A well-rested mind is productive.",
        "📖 **Continuous Learning** – Keep growing and adapting."
    ]
    st.info(f"💡 **Productivity Tip:** {random.choice(tips)}")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.markdown("# 🤔 Daily Self-Reflection")
    st.write("Reflect on your day to gain insights and improve tomorrow.")
    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    accomplishments = st.text_area("What did you accomplish today?")
    challenges = st.text_area("What challenges did you face?")
    lessons = st.text_area("What did you learn today?")
    if st.button("Save Reflection"):
        st.success("Reflection saved! Keep growing! 🌱")

# Growth Mindset
elif page == "🧠 Growth Mindset":
    st.markdown("# 🧠 Develop a Growth Mindset")
    st.image("https://source.unsplash.com/800x400/?learning,mindset", use_container_width=True)
    st.markdown(
        """
        ### Key Growth Mindset Principles:
        1️⃣ **Embrace Challenges** – See obstacles as opportunities.
        2️⃣ **Learn from Setbacks** – Mistakes help you grow.
        3️⃣ **Effort Leads to Mastery** – Keep improving daily.
        4️⃣ **Seek Feedback** – Use criticism to improve.
        5️⃣ **Stay Inspired** – Learn from the success of others.
        """
    )
    
    if st.button("Accept the Growth Mindset Challenge"):
        st.success("Great! Keep learning and growing! 🌱")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | 🚀 Peak Performance Hub")

