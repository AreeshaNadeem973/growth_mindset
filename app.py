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
        .box {background: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);}
        .home-container {text-align: center; padding: 40px; background: linear-gradient(to right, #36d1dc, #5b86e5); border-radius: 12px; color: white;}
        .home-title {font-size: 36px; font-weight: bold; margin-bottom: 10px;}
        .home-subtext {font-size: 18px; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>🌱 Growth Mindset Hub</div>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("🌟 Growth Journey")
page = st.sidebar.radio("Choose a section:", [
    "🏡 Home", "📊 Growth Progress Tracker", "💬 Daily Motivation", "📖 Success Stories", "🎯 Goal Setter",
    "📝 Reflection Journal", "🧠 Brain Boost"
])

# Home Page
if page == "🏡 Home":
    st.markdown("""
        <div class='home-container'>
            <div class='home-title'>Welcome to the Growth Mindset Hub 🚀</div>
            <div class='home-subtext'>Unlock your potential, embrace challenges, and grow every day.</div>
            <div class='home-subtext'>✨ Start your journey to success now! ✨</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.image("https://media.istockphoto.com/id/1282270343/photo/growth-mindset-concept-showing-a-brain-growing-like-a-tree.webp", use_container_width=True)
    
    st.markdown("""
        <div class='box'>
        ✅ **Embrace Challenges**: View obstacles as opportunities to learn.  
        ✅ **Learn from Mistakes**: Mistakes help you grow and improve.  
        ✅ **Stay Persistent**: Keep going even when things get tough.  
        ✅ **Celebrate Progress**: Every step forward is a victory!  
        </div>
    """, unsafe_allow_html=True)

# Other sections remain unchanged...
