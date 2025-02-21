import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="Rise & Thrive: Unlock Your Potential", page_icon="🌟")
st.title("🌟 Rise & Thrive: Unlock Your Potential")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
age_group = st.sidebar.selectbox("Select Your Age Group:", ["Kids", "Teens", "Adults", "Seniors"])
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Inspirational Stories",
    "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Self-Reflection", "🧠 Brain Teasers", "🧠 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.header(f"Welcome to Rise & Thrive, {age_group}! 🚀")
    st.markdown("""
    ### Why Focus on Productivity & Motivation?
    ✅ **Stay Inspired**: Start each day with positive energy.  
    ✅ **Build Consistent Habits**: Small steps lead to big success.  
    ✅ **Set and Achieve Goals**: Turn your dreams into reality.  
    ✅ **Develop a Growth Mindset**: Keep learning and improving!  
    """)
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg", use_container_width=True)
    st.success("Today is a new beginning! Make the most of it! 🚀")
    
    # Add a motivational quote of the day based on age group
    quotes = {
        "Kids": [
            "You are braver than you believe, stronger than you seem, and smarter than you think. - A.A. Milne",
            "Mistakes are proof that you are trying!",
            "Believe in yourself and magic will happen!"
        ],
        "Teens": [
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
            "Dream big, work hard, stay focused!"
        ],
        "Adults": [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
        ],
        "Seniors": [
            "It’s never too late to be what you might have been. - George Eliot",
            "Do not regret growing older. It is a privilege denied to many.",
            "Keep your mind young, and your heart will follow!"
        ]
    }
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes[age_group])}")
