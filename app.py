import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Future Tech Trends: AI, Space, and Innovation", page_icon="🚀")
st.title("🚀 Future Tech Trends: AI, Space, and Innovation")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "🤖 AI Innovations", "🚀 Space Exploration", "📡 Emerging Tech", "📊 Data & Trends"
])

# Home Page
if page == "🏡 Home":
    st.header("🚀 Welcome to Future Tech Trends!")
    st.image("https://images.pexels.com/photos/586528/pexels-photo-586528.jpeg", use_container_width=True)
    st.markdown("""
    ### Explore the Technologies Shaping Our Future
    ✅ **Artificial Intelligence Breakthroughs** 🤖  
    ✅ **Space Missions & Colonization** 🚀  
    ✅ **Emerging Technologies & Future Innovations** 📡  
    """)
    st.success("Stay ahead of the future with cutting-edge insights! 🚀")

# AI Innovations
elif page == "🤖 AI Innovations":
    st.header("🤖 Latest in AI & Machine Learning")
    ai_trends = ["Generative AI", "Quantum Computing", "AI in Healthcare", "Autonomous Vehicles"]
    for trend in ai_trends:
        st.checkbox(f"Interested in {trend}?")
    
    if st.button("Save Preferences"):
        st.success("Your AI interests are saved! 🤖")
    
    # AI Investment Growth Chart
    years = np.arange(2015, 2025)
    investment = np.random.randint(50, 300, size=len(years))
    fig, ax = plt.subplots()
    ax.plot(years, investment, marker='o', linestyle='-', color='blue')
    ax.set_title("AI Investment Growth Over the Years")
    ax.set_ylabel("Investment (Billion $)")
    st.pyplot(fig)

# Space Exploration
elif page == "🚀 Space Exploration":
    st.header("🚀 The Future of Space Travel")
    missions = ["Mars Colonization", "Moon Base", "Space Tourism", "Deep Space Exploration"]
    for mission in missions:
        st.checkbox(f"Excited for {mission}?")
    
    # Space Missions Timeline Graph
    missions_years = [2025, 2030, 2040, 2050]
    milestones = [2, 5, 8, 12]
    fig, ax = plt.subplots()
    ax.bar(missions_years, milestones, color=['red', 'green', 'blue', 'purple'])
    ax.set_title("Upcoming Space Missions Timeline")
    ax.set_ylabel("Mission Count")
    st.pyplot(fig)

# Emerging Tech
elif page == "📡 Emerging Tech":
    st.header("📡 Technologies Reshaping the World")
    tech = ["5G & Beyond", "Blockchain", "AR/VR", "Biotechnology"]
    for t in tech:
        st.checkbox(f"Following {t}?")
    
    # Tech Growth Pie Chart
    labels = ["5G & IoT", "AI & Automation", "Blockchain", "AR/VR"]
    sizes = [30, 25, 20, 25]
    colors = ["blue", "orange", "green", "red"]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title("Tech Adoption Rates")
    ax.axis('equal')
    st.pyplot(fig)

# Data & Trends
elif page == "📊 Data & Trends":
    st.header("📊 Future Tech Market Trends")
    sectors = ["AI", "Space", "Quantum Computing", "Renewable Energy"]
    market_values = np.random.randint(100, 1000, size=len(sectors))
    fig, ax = plt.subplots()
    ax.barh(sectors, market_values, color='cyan')
    ax.set_title("Projected Market Value in 2030 ($B)")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Future Tech Trends")
