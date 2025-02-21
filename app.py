import streamlit as st
import random

# Custom Styling
st.markdown("""
    <style>
        .main-container {text-align: center; padding: 50px; background: linear-gradient(to right, #4facfe, #00f2fe); border-radius: 12px; color: white;}
        .main-title {font-size: 42px; font-weight: bold; margin-bottom: 10px;}
        .main-subtext {font-size: 22px; margin-bottom: 20px;}
        .highlight {color: #ffeb3b; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='main-container'>"
            "<div class='main-title'>Welcome to Your Ultimate Productivity Hub 🚀</div>"
            "<div class='main-subtext'>Stay Focused. Stay Motivated. Achieve Greatness.</div>"
            "<div class='main-subtext'>Your journey to success starts here! 💡</div>"
            "</div>", unsafe_allow_html=True)

# Daily Motivation
st.markdown("### 🌟 Today's Motivation")
motivations = [
    "Success is the sum of small efforts, repeated day in and day out.",
    "Your only limit is your mind. Keep pushing forward!",
    "Dream big, work hard, and make it happen!",
    "Every day is a fresh start. Make it count!"
]
st.write(random.choice(motivations))

# Quick Links
st.markdown("### 🚀 Quick Actions")
st.button("📊 Track Your Productivity")
st.button("🎯 Set a New Goal")
st.button("📝 Reflect on Your Day")
st.button("💡 Boost Your Brain")
