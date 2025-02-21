import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

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

# Success Roadmap Page
elif page == "🎯 Success Roadmap":
    st.header("🎯 Your Roadmap to Success")
    st.markdown("""
    ✅ **Set Clear Goals**: Define your vision & take actionable steps.  
    🚀 **Stay Consistent**: Small efforts every day lead to massive achievements.  
    🏆 **Learn from Failures**: Turn setbacks into stepping stones.  
    """)
    st.success("Your journey to greatness starts NOW!")

# Daily Inspiration Page
elif page == "💡 Daily Inspiration":
    st.header("💡 Stay Inspired Every Day")
    quotes = [
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Great things never come from comfort zones.",
        "Do something today that your future self will thank you for.",
        "Opportunities don’t happen. You create them."
    ]
    st.info(f"🌟 **Today's Inspiration:** {random.choice(quotes)}")
    st.success("Take a step forward today!")

# Legendary Stories Page
elif page == "📚 Legendary Stories":
    st.header("📚 Learn from Legends")
    stories = [
        ("💡 Elon Musk", "Started multiple companies and changed industries."),
        ("📚 J.K. Rowling", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 Michael Jordan", "Was cut from his high school team but became an icon."),
        ("🌍 Nelson Mandela", "Spent 27 years in prison and changed a nation."),
        ("🎶 Ed Sheeran", "Slept on sofas while pursuing music, now a global icon.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
    st.success("Be inspired and create your own success story!")

# Master Your Skills Page
elif page == "📈 Master Your Skills":
    st.header("📈 Elevate Your Skills & Track Progress")
    st.markdown("""
    🔥 **Sharpen Your Expertise**: Learn, practice, and grow.  
    📊 **Measure Your Growth**: Track skill development over time.  
    """)
    
    # Add a graph to visualize skill progress
    skills = ["Leadership", "Creativity", "Discipline", "Networking", "Resilience"]
    progress = np.random.randint(50, 100, size=len(skills))
    
    fig, ax = plt.subplots()
    ax.bar(skills, progress, color=['blue', 'green', 'orange', 'red', 'purple'])
    ax.set_title("Skill Development Progress")
    ax.set_ylabel("Progress (%)")
    ax.set_ylim(0, 100)
    
    st.pyplot(fig)
    
    st.success("Keep building your skills—growth is a continuous journey! 🚀")

# Peak Productivity Page
elif page == "🚀 Peak Productivity":
    st.header("🚀 Unlock Your Peak Productivity")
    st.markdown("""
    📋 **Prioritize Tasks**: Stay organized and efficient.  
    🕒 **Time Management**: Work smarter, not harder.  
    🎯 **Focus & Discipline**: Remove distractions and stay in the zone.  
    """)
    st.success("Maximize your potential every day!")

# Community & Networking Page
elif page == "🤝 Community & Networking":
    st.header("🤝 Connect with Like-Minded Leaders")
    st.markdown("""
    🌍 **Expand Your Network**: Meet inspiring people.  
    💡 **Exchange Ideas**: Learn from different perspectives.  
    🎯 **Collaboration**: Work together towards success.  
    """)
    st.success("Build relationships that fuel your growth!")

# Brain Boosters Page
elif page == "🎮 Brain Boosters":
    st.header("🎮 Train Your Mind")
    puzzles = [
        ("🤔 What has keys but can't open locks?", "A piano"),
        ("🔍 What has to be broken before you can use it?", "An egg"),
        ("🎭 The more you take, the more you leave behind. What is it?", "Footsteps"),
        ("❓ I speak without a mouth and hear without ears. What am I?", "An echo")
    ]
    question, answer = random.choice(puzzles)
    st.write(question)
    user_answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! Well done!")
        else:
            st.error(f"Not quite. The correct answer is: {answer}")
    st.success("Keep challenging your brain every day!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Future Leaders Hub")
