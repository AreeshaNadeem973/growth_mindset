import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# App Title
st.set_page_config(page_title="Peak Performance Hub", page_icon="🚀")
st.title("🚀 Peak Performance Hub")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", ["🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Success Stories", "🎯 Goal Setting", "📝 Productivity Hacks", "🤔 Self-Reflection", "🧠 Growth Mindset"])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Peak Performance Hub! 🌟")
    st.markdown("""
    ### Why Focus on Growth & Productivity?
    ✅ **Stay Inspired**: Fuel your passion every day.  
    ✅ **Build Smart Habits**: Small steps lead to big wins.  
    ✅ **Set and Smash Goals**: Plan, act, and achieve.  
    ✅ **Develop a Winning Mindset**: Keep learning and growing!  
    """)

    # Displaying 7 small motivational images
    image_urls = [
        "https://source.unsplash.com/150x150/?success",
        "https://source.unsplash.com/150x150/?goal",
        "https://source.unsplash.com/150x150/?motivation",
        "https://source.unsplash.com/150x150/?growth",
        "https://source.unsplash.com/150x150/?learning",
        "https://source.unsplash.com/150x150/?inspiration",
        "https://source.unsplash.com/150x150/?focus"
    ]
    cols = st.columns(7)
    for i, img in enumerate(image_urls):
        with cols[i]:
            st.image(img, use_column_width=True)

    st.success("Today is a new beginning! Make the most of it! 🚀")

    # Motivational Quote of the Day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

    # Weekly Motivation Trend Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)  # Simulated motivation levels
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Peak Performance Hub")
