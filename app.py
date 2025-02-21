import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# App Title
st.title("🏋️ Fitness Hub: Your Ultimate Health Companion")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Home", "📊 Workout Tracker", "🍎 Meal Planner", "📈 Health Analytics",
    "🎯 Goal Setter", "🏆 Achievements", "🌍 Community"
])

# Home Page
if page == "🏠 Home":
    st.header("Welcome to Fitness Hub! 🏋️")
    st.markdown("""
    ### Your Personalized Health & Fitness Assistant
    ✅ **Track Workouts**: Log and analyze your exercises  
    ✅ **Plan Meals**: Maintain a balanced diet with meal tracking  
    ✅ **Monitor Health**: Check your BMI and health stats  
    ✅ **Set Goals**: Stay motivated with goal tracking  
    ✅ **Join Community**: Engage with fellow fitness enthusiasts  
    """)
    
    # Quick Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Workouts", "15")
    with col2:
        st.metric("Meals Logged", "30")
    with col3:
        st.metric("Active Goals", "5")
    
    # Motivational Quote
    st.subheader("💪 Stay Strong, Stay Healthy!")
    st.write("*""The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will." - Vince Lombardi*"")








