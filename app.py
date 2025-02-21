import streamlit as st
import matplotlib.pyplot as plt

# App Title
st.title("🌟 Success Habits Tracker")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Habit Tracker", "📝 Daily Task", "💡 Productivity Tips",
    "📖 Inspirational Stories", "🎯 Goal Setting", "🤔 Self-Reflection", "🧩 Brain Teasers"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Success Habits Tracker! 🚀")
    st.markdown("""
    ### Why Build Success Habits?
    ✅ **Stay Consistent**: Small efforts daily lead to big achievements.  
    ✅ **Learn from Failures**: Mistakes are lessons in disguise.  
    ✅ **Develop Self-Discipline**: Build a mindset for success.  
    ✅ **Track Your Progress**: See how far you’ve come!  
    ✅ **Stay Motivated**: Keep pushing forward every day.  
    """)
    st.image("https://media.istockphoto.com/id/1363797430/photo/success-loading-bar.webp", use_container_width=True)

# Habit Tracker
elif page == "📊 Habit Tracker":
    st.header("📊 Track Your Daily Habits")
    
    days = st.slider("How many days have you been tracking habits?", 1, 30, 5)
    effort = st.slider("How consistent have you been (1-10)?", 1, 10, 7)

    st.session_state["days"] = days  

    fig, ax = plt.subplots()
    ax.bar(["Days Tracked", "Consistency Level"], [days, effort], color=["blue", "green"])
    ax.set_ylabel("Level")
    st.pyplot(fig)

# Daily Task
elif page == "📝 Daily Task":
    st.header("📝 Today's Success Habit Task")
    
    days = st.session_state.get("days", 1)

    tasks = [
        "🔹 Write down 3 things you want to achieve today.",
        "🔹 Start your day with 10 minutes of mindfulness.",
        "🔹 Avoid distractions for 1 hour and focus on deep work.",
        "🔹 Read 10 pages of a book related to personal growth.",
        "🔹 Exercise for at least 30 minutes.",
        "🔹 Reflect on what went well today and what you can improve."
    ]

    st.write("💡 **Task for Today:**", tasks[days % len(tasks)])

# Productivity Tips
elif page == "💡 Productivity Tips":
    st.header("💡 Daily Productivity Tip")
    
    tips = [
        "🔥 **Use the Pomodoro Technique** – Work for 25 minutes, then take a 5-minute break.",
        "🔥 **Eliminate Distractions** – Turn off notifications and focus.",
        "🔥 **Prioritize Tasks** – Focus on the most important tasks first.",
        "🔥 **Stay Hydrated & Eat Well** – Your brain needs energy!",
        "🔥 **Review Your Goals Daily** – Keep yourself accountable.",
        "🔥 **Get Enough Sleep** – A well-rested mind performs better."
    ]

    days = st.session_state.get("days", 1)
    st.markdown(f"💡 **Tip for Today:** {tips[days % len(tips)]}")

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Success Stories of Famous People")
    
    stories = [
        ("💪 **Elon Musk**", "Failed multiple times before Tesla and SpaceX became successful."),
        ("📚 **Stephen King**", "His first novel was rejected 30 times before publication."),
        ("🎤 **Lady Gaga**", "Dropped by her first record label but didn’t give up."),
        ("🏀 **Kobe Bryant**", "Practiced 4 AM workouts every day to be the best."),
        ("💻 **Steve Jobs**", "Was fired from Apple, then returned to make it a global giant.")
    ]
    
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Success Goals")

    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")

    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 Reflect on Your Progress")

    journal = st.text_area("📖 Write about your progress, challenges, and key learnings:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep pushing forward.")

# Brain Teasers
elif page == "🧩 Brain Teasers":
    st.header("🧩 Daily Brain Teaser")

    riddles = [
        ("🤔 **What comes once in a minute, twice in a moment, but never in a thousand years?**", "The letter M"),
        ("🔍 **I am not alive, but I grow. I don’t have lungs, but I need air. What am I?**", "Fire"),
        ("🎭 **The more you remove from me, the bigger I get. What am I?**", "A hole"),
        ("💡 **What can travel around the world while staying in the same spot?**", "A stamp")
    ]
    
    days = st.session_state.get("days", 1)
    question, answer = riddles[days % len(riddles)]

    st.write(question)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🚀 *Built with ❤️ using Streamlit. Keep Growing & Succeeding!*")
