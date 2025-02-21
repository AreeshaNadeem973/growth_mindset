import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Mindset Growth Lab", page_icon="🧠")

# Sidebar for Navigation
st.sidebar.header("🚀 Mindset Boost")
page = st.sidebar.radio("Jump to:", [
    "🏡 Home", "💡 Daily Affirmations", "🧠 Mindset Quiz", "📊 Growth Tracker", "🔥 Challenge Yourself"
])

# Home Page
if page == "🏡 Home":
    st.title("🧠 Mindset Growth Lab")
    st.header("Unlock the Power of a Growth Mindset! 🚀")
    st.markdown("""
    🔥 **Shift Your Thinking**: Rewire your brain for success.  
    💡 **Embrace Challenges**: Learn from failures & keep pushing forward.  
    🚀 **Develop Grit & Resilience**: Small steps lead to massive success.  
    """)

    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qfh-TpOCaE_o_4sTAyoVhQ.png", use_container_width=True)

    st.success("Every day is a chance to grow! Keep going! 🌱")

# Daily Affirmations Page
elif page == "💡 Daily Affirmations":
    st.header("💡 Positive Mindset Affirmations")
    
    affirmations = [
        "I am capable of achieving greatness! 🚀",
        "Challenges help me grow stronger. 💪",
        "Every failure is a lesson towards success. 🎯",
        "I embrace learning and improvement daily. 🌱"
    ]
    
    st.info(f"✨ **Your Affirmation for Today:** {random.choice(affirmations)}")

# Mindset Quiz Page
elif page == "🧠 Mindset Quiz":
    st.header("🧠 Growth vs. Fixed Mindset Quiz")
    st.markdown("**Answer the following questions to check your mindset!**")

    questions = [
        "1️⃣ When I fail, I... (A) Give up | (B) Learn from it",
        "2️⃣ Challenges are... (A) Frustrating | (B) Opportunities",
        "3️⃣ Effort is... (A) Pointless | (B) Key to success",
        "4️⃣ Criticism is... (A) An attack | (B) Helpful feedback"
    ]

    for q in questions:
        st.markdown(q)
    
    st.success("If most of your answers are (B), you're developing a **Growth Mindset!** 🌟")

# Growth Tracker Page
elif page == "📊 Growth Tracker":
    st.header("📊 Track Your Mindset Growth")

    categories = ["Resilience", "Confidence", "Problem-Solving", "Adaptability"]
    progress = np.random.randint(50, 100, size=len(categories))

    fig, ax = plt.subplots()
    ax.bar(categories, progress, color=['blue', 'green', 'red', 'purple'])
    ax.set_title("Mindset Growth Progress")
    ax.set_ylabel("Growth (%)")
    ax.set_ylim(0, 100)

    st.pyplot(fig)
    st.success("Keep growing! Every step counts! 🌱")

# Challenge Yourself Page
elif page == "🔥 Challenge Yourself":
    st.header("🔥 Growth Mindset Challenges")
    
    challenges = [
        "📖 Read about someone who overcame adversity.",
        "🚀 Try something new that scares you!",
        "🎯 Reframe a negative thought into a positive one.",
        "💡 Spend 10 minutes reflecting on a past success."
    ]
    
    st.info(f"💪 **Today's Challenge:** {random.choice(challenges)}")

st.sidebar.success("Embrace the Growth Mindset! 🚀")

