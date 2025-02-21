import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Custom Styling
st.markdown("""
    <style>
        .main {background-color: #f4f4f4; padding: 20px; border-radius: 10px;}
        .title {color: #ff4500; text-align: center; font-size: 42px; font-weight: bold;}
        .subtitle {color: #2e8b57; text-align: center; font-size: 22px;}
        .box {background: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); text-align: center;}
        .home-container {text-align: center; padding: 40px; background: linear-gradient(to right, #ff9a9e, #fad0c4); border-radius: 12px; color: white;}
        .home-title {font-size: 40px; font-weight: bold; margin-bottom: 10px;}
        .home-subtext {font-size: 20px; margin-bottom: 20px;}
        .highlight {color: #ff4500; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>🚀 AI-Powered Growth Hub</div>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("🌍 Explore")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📊 AI Growth Tracker", "💬 AI-Powered Insights", "📖 Inspiring AI Stories", "🎯 Smart Goal Setter",
    "📝 Reflection Journal", "🧠 AI Brain Boost"
])

# Home Page
if page == "🏡 Home":
    st.markdown("""
        <div class='home-container'>
            <div class='home-title'>Welcome to the AI-Powered Growth Hub 🤖</div>
            <div class='home-subtext'>Supercharge your mindset with AI-driven insights and motivation.</div>
            <div class='home-subtext'>🚀 Let AI help you grow and achieve more every day!</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg", use_container_width=True)
    
    st.markdown("""
        <div class='box'>
        ✅ **AI-Powered Insights**: Use AI to track and boost your growth.  
        ✅ **Smart Learning**: Get personalized recommendations based on your progress.  
        ✅ **Stay Motivated**: AI-generated daily tips to keep you going.  
        ✅ **Achieve More**: Set smarter goals with AI-driven analytics.  
        </div>
    """, unsafe_allow_html=True)

# AI Growth Tracker
elif page == "📊 AI Growth Tracker":
    st.header("📊 Track Your AI Growth")
    days = st.slider("How many days have you been improving with AI?", 1, 30, 5)
    effort = st.slider("How much effort do you put in (1-10)?", 1, 10, 7)
    
    fig, ax = plt.subplots()
    ax.bar(["Days", "Effort"], [days, effort], color=["blue", "green"])
    ax.set_ylabel("Progress Level")
    st.pyplot(fig)

# AI-Powered Insights
elif page == "💬 AI-Powered Insights":
    st.header("💡 AI-Generated Daily Motivation")
    tips = [
        "🚀 Keep pushing forward! AI believes in your potential.",
        "🎯 Every step matters. Stay consistent and grow.",
        "💡 Learning from failures is the key to AI-driven success.",
        "🔥 Challenge yourself today, and let AI assist your journey."
    ]
    st.write(random.choice(tips))

# Inspiring AI Stories
elif page == "📖 Inspiring AI Stories":
    st.header("📖 Real-Life AI Success Stories")
    stories = [
        ("🔬 **AlphaGo**", "An AI that beat human champions in the complex game of Go."),
        ("🚗 **Self-Driving Cars**", "AI is transforming transportation worldwide."),
        ("🎶 **AI in Music**", "AI is composing music and revolutionizing creativity.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Smart Goal Setter
elif page == "🎯 Smart Goal Setter":
    st.header("🎯 AI-Powered Goal Setting")
    goal = st.text_input("📝 Enter your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}!")

# Reflection Journal
elif page == "📝 Reflection Journal":
    st.header("📝 Daily AI-Assisted Reflection")
    journal = st.text_area("📖 Share your thoughts and progress:")
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep growing with AI.")

# AI Brain Boost
elif page == "🧠 AI Brain Boost":
    st.header("🧠 AI-Generated Brain Challenge")
    riddles = [
        ("🤖 **I speak without a mouth and hear without ears. What am I?**", "An AI model"),
        ("💡 **The more data I get, the smarter I become. What am I?**", "Machine Learning"),
        ("🔍 **I can predict the future but have no mind. What am I?**", "Artificial Intelligence")
    ]
    question, answer = random.choice(riddles)
    st.write(question)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🌱 *Built with ❤️ using Streamlit. AI is here to help you grow!*")
