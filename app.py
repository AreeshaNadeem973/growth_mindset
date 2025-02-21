import streamlit as st
import random

# App Title
st.set_page_config(page_title="🚀 Peak Performance Hub", page_icon="🔥")
st.title("🚀 Peak Performance Hub: Develop a Growth Mindset")

# Sidebar Navigation
st.sidebar.header("📌 Navigate")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "🧠 Mindset Basics", "🎯 Daily Challenges", "📖 Success Stories",
    "✅ Goal Setting & Progress", "💪 Overcoming Setbacks", "📝 Self-Reflection & Journaling",
    "🚀 Motivation & Productivity Hacks"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Peak Performance Hub! 🚀")
    st.markdown("""
    ### Why Growth Mindset Matters?
    ✅ **Embrace Challenges** – Learn and grow from difficulties.  
    ✅ **Persist Through Setbacks** – Failure is just a stepping stone.  
    ✅ **Believe in Progress** – Intelligence & skills can be developed.  
    ✅ **Learn from Others** – Get inspired by success stories!  
    
    """)
    st.success("Your potential is limitless. Keep pushing forward! 💡")
    
    # Random Growth Mindset Quote
    quotes = [
        "Failure is an opportunity to grow!",
        "Effort and attitude determine success.",
        "I can learn anything if I put in the effort.",
        "Challenges make me stronger!",
        "Feedback helps me improve.",
        "Every mistake is a learning opportunity."
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Mindset Basics
elif page == "🧠 Mindset Basics":
    st.header("🧠 Fixed vs. Growth Mindset")
    st.write("""
    - **Fixed Mindset**: Believes abilities are static. Avoids challenges. Gives up easily.
    - **Growth Mindset**: Believes abilities can be developed. Embraces challenges. Keeps going!
    """)
    st.image("https://miro.medium.com/max/1400/1*d7PH_YtJOhHBa-3NiAikbQ.jpeg", use_column_width=True)
    
# Daily Challenges
elif page == "🎯 Daily Challenges":
    st.header("🎯 Today's Growth Challenge")
    challenges = [
        "Try something new today!", "Reframe a failure as a learning experience.",
        "Give constructive feedback to someone.", "Push yourself outside your comfort zone.",
        "Learn a new skill or fact today!"
    ]
    st.success(f"🚀 **Your Challenge:** {random.choice(challenges)}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Inspirational Growth Mindset Stories")
    stories = {
        "🌟 Elon Musk": "Overcame multiple failures to build Tesla & SpaceX.",
        "📚 J.K. Rowling": "Rejected 12 times before publishing Harry Potter.",
        "🏀 Michael Jordan": "Was cut from his high school team but became an icon.",
        "🌍 Nelson Mandela": "Spent 27 years in prison and still changed the world."
    }
    for name, story in stories.items():
        st.subheader(name)
        st.write(story)

# Goal Setting & Progress
elif page == "✅ Goal Setting & Progress":
    st.header("✅ Set & Track Your Goals")
    goal = st.text_input("Your Goal:")
    if goal:
        steps = st.text_area("Steps to Achieve It:")
        if st.button("Save Goal"):
            st.success("Goal Saved! Stay committed.")
            st.balloons()

# Overcoming Setbacks
elif page == "💪 Overcoming Setbacks":
    st.header("💪 Bounce Back from Failure")
    st.write("Failure isn't the end – it's a lesson!")
    st.image("https://i.imgur.com/Y5B30nD.png", use_column_width=True)
    st.info("Think about a recent failure. What did you learn from it?")
    
# Self-Reflection & Journaling
elif page == "📝 Self-Reflection & Journaling":
    st.header("📝 Daily Reflection")
    st.write("Take time to reflect on your growth today.")
    mood = st.select_slider("How was your mood today?", ["😔", "😐", "🙂", "😊", "😃"])
    reflection = st.text_area("What did you learn today?")
    if st.button("Save Reflection"):
        st.success("Reflection saved! Keep growing.")
        st.balloons()

# Motivation & Productivity Hacks
elif page == "🚀 Motivation & Productivity Hacks":
    st.header("🚀 Boost Your Productivity")
    tips = [
        "Use time-blocking to stay focused.",
        "Prioritize tasks using the Eisenhower Matrix.",
        "Get enough sleep for better performance.",
        "Limit distractions like social media.",
        "Stay hydrated and take short breaks."
    ]
    st.write(f"💡 **Tip for Today:** {random.choice(tips)}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Peak Performance Hub")

