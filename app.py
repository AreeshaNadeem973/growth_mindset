import streamlit as st
import random

# App Title
st.set_page_config(page_title="Future Leaders Hub: Unlock Your Potential", page_icon="🔥")
st.title("🔥 Future Leaders Hub: Empower, Innovate & Grow")

# Sidebar for Navigation
st.sidebar.header("🚀 Explore & Elevate")
page = st.sidebar.radio("Jump to:", [
    "🏡 Home", "🎯 Success Roadmap", "💡 Daily Inspiration", "📚 Legendary Stories",
    "📈 Master Your Skills", "🚀 Peak Productivity", "🤝 Community & Networking", "🎮 Brain Boosters"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Future Leaders Hub! 🌍✨")
    st.markdown("""
    ### Why Join the Movement?
    🔥 **Fuel Your Ambition**: Daily wisdom to keep you inspired.  
    🚀 **Develop Winning Habits**: Small actions lead to massive results.  
    🎯 **Achieve & Dominate Goals**: Turn ideas into reality.  
    🧠 **Adopt a Growth Mindset**: Keep evolving & leading!  
    """)
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg", use_container_width=True)
    st.success("Today is YOUR day! Take charge and make an impact! 🌟")
    
    # Add a motivational quote of the day
    quotes = [
        "Your limitation—it’s only your imagination!", 
        "Push yourself, because no one else will do it for you.", 
        "Dream it. Believe it. Build it.", 
        "Success doesn’t just find you. You have to go out and get it!"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Success Roadmap
elif page == "🎯 Success Roadmap":
    st.header("🎯 Your Roadmap to Success")
    st.markdown("""
    - **Set Clear Goals** 🎯
    - **Develop a Powerful Routine** ⏰
    - **Stay Consistent & Adapt** 🔄
    - **Track Your Progress** 📊
    """)

# Daily Inspiration
elif page == "💡 Daily Inspiration":
    st.header("💡 Get Inspired Daily!")
    inspirations = [
        "Believe in yourself and your abilities!", 
        "Every challenge is an opportunity to grow.", 
        "You are stronger than you think.", 
        "Take one step at a time and never stop learning!"
    ]
    st.success(f"🌟 {random.choice(inspirations)}")

# Legendary Stories
elif page == "📚 Legendary Stories":
    st.header("📚 Learn from Legends")
    stories = [
        "💡 **Elon Musk** - Innovating industries with Tesla & SpaceX.",
        "📖 **Oprah Winfrey** - Rising from struggles to global influence.",
        "🚀 **Steve Jobs** - Revolutionizing technology with Apple.",
        "🏆 **Serena Williams** - Dominating tennis with resilience & power."
    ]
    for story in stories:
        st.write(story)

# Master Your Skills
elif page == "📈 Master Your Skills":
    st.header("📈 Sharpen Your Skills")
    skills = ["Public Speaking", "Problem-Solving", "Leadership", "Time Management"]
    for skill in skills:
        st.checkbox(f"Work on {skill} today?")

# Peak Productivity
elif page == "🚀 Peak Productivity":
    st.header("🚀 Maximize Your Productivity")
    st.markdown("""
    - **Use Time Blocks** ⏳
    - **Avoid Multitasking** ❌
    - **Take Regular Breaks** ☕
    - **Prioritize Your Tasks** ✅
    """)

# Community & Networking
elif page == "🤝 Community & Networking":
    st.header("🤝 Connect with Like-Minded People")
    st.write("Network with future leaders and build strong relationships!")
    name = st.text_input("Your Name:")
    if st.button("Join the Community"):
        st.success(f"Welcome to the Future Leaders Network, {name}!")

# Brain Boosters
elif page == "🎮 Brain Boosters":
    st.header("🎮 Train Your Brain")
    questions = [
        "What has to be broken before you can use it? (Hint: Breakfast Item)",
        "The more of me you take, the more you leave behind. What am I?"
    ]
    st.write(random.choice(questions))
