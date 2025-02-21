import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.set_page_config(page_title="Mindset Growth Hub", page_icon="🌱")

# Sidebar for Navigation (Updated Navbar Names)
st.sidebar.header("🌿 Mindset Navigator")
page = st.sidebar.radio("Jump to:", [
    "🏡 Home", "💡 Growth Affirmations", "🧠 Mindset Challenges", "📊 Progress Tracker", "🚀 Power Habits"
])

# Home Page
if page == "🏡 Home":
    st.title("Grow Your Mindset, Change Your Life")
    st.header("Unlock Your Full Potential! 🚀")
    st.markdown("""
    🌿 **Shift Your Thinking**: Develop a resilient, positive mindset.  
    💡 **Learn from Setbacks**: Every failure is a step to success.  
    🔥 **Embrace Challenges**: Growth happens outside your comfort zone.  
    🎯 **Take Action**: Small consistent steps lead to big success.
    """)
    
    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*qfh-TpOCaE_o_4sTAyoVhQ.png", use_container_width=True)
    
    st.success("Every challenge is a new opportunity to grow! Keep evolving! 🌱")

# Growth Affirmations Page
elif page == "💡 Growth Affirmations":
    st.header("💡 Daily Affirmations for a Strong Mindset")
    affirmations = [
        "I am constantly growing and evolving. 🌿",
        "Every challenge strengthens me. 💪",
        "I believe in my ability to succeed. 🚀",
        "Obstacles are just opportunities in disguise. 🎯",
        "I attract positivity and growth in my life. 🌟",
        "Success is built with persistence and belief. 💖"
    ]
    st.info(f"✨ **Today's Affirmation:** {random.choice(affirmations)}")
    st.markdown("**Tip:** Repeat your affirmation 3 times in front of a mirror for maximum impact! 💡")

# Mindset Challenges Page
elif page == "🧠 Mindset Challenges":
    st.header("🧠 Challenge Yourself to Grow")
    challenges = [
        "📖 Read about someone who overcame failure and succeeded.",
        "🚀 Try something new that pushes your limits!",
        "🎯 Reframe a negative thought into a positive one.",
        "💡 Spend 5 minutes visualizing your ideal future.",
        "📝 Write down three things you’re grateful for today.",
        "🤝 Reach out to someone who inspires you and ask for advice."
    ]
    st.info(f"🔥 **Your Challenge Today:** {random.choice(challenges)}")
    st.markdown("**Extra Task:** Keep a journal and track how each challenge impacts your mindset over time. 📓")

# Progress Tracker Page
elif page == "📊 Progress Tracker":
    st.header("📊 Measure Your Mindset Growth")
    categories = ["Resilience", "Optimism", "Problem-Solving", "Self-Discipline", "Confidence"]
    progress = np.random.randint(50, 100, size=len(categories))
    
    fig, ax = plt.subplots()
    ax.bar(categories, progress, color=['blue', 'green', 'red', 'purple', 'orange'])
    ax.set_title("Mindset Growth Progress")
    ax.set_ylabel("Growth (%)")
    ax.set_ylim(0, 100)
    
    st.pyplot(fig)
    st.success("Small improvements every day lead to massive success! 🌟")
    st.markdown("**Tip:** Review your progress weekly and set small, achievable goals! 🚀")

# Power Habits Page
elif page == "🚀 Power Habits":
    st.header("🚀 Build Habits That Strengthen Your Mindset")
    habits = [
        "📌 Start your day with gratitude.",
        "🧘‍♂️ Meditate for 5-10 minutes daily.",
        "📚 Read or listen to personal growth content.",
        "✍️ Journal your thoughts & progress.",
        "🏋️ Exercise to keep both your body and mind healthy.",
        "🎯 Set and track daily goals to build discipline."
    ]
    st.info(f"💪 **Try This Habit Today:** {random.choice(habits)}")
    st.markdown("**Did You Know?** It takes around 21 days to build a habit. Stay consistent! 🔄")
