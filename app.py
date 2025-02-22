import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import random

# App Title and Configuration
st.set_page_config(page_title="Personal Growth Tracker", page_icon="📈", layout="wide")
st.title("📈 Personal Growth Tracker")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Goal Setter", "Habit Tracker", "Mood Logger"])

# Home Page
if page == "Home":
    st.header("Welcome to Your Personal Growth Journey")
    
    st.subheader("Quick Actions")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Set a New Goal"):
            st.session_state.page = "Goal Setter"
            st.experimental_rerun()
    with col2:
        if st.button("Log a Habit"):
            st.session_state.page = "Habit Tracker"
            st.experimental_rerun()
    with col3:
        if st.button("Record Your Mood"):
            st.session_state.page = "Mood Logger"
            st.experimental_rerun()
    
    st.subheader("Your Progress Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Goals Set", "5", "+1 this week")
        st.metric("Habits Tracked", "3", "+2 this month")
    with col2:
        st.metric("Mood Score (Avg)", "7.5", "+0.5 from last week")
    
    st.subheader("Motivational Quote")
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(random.choice(quotes))

# Goal Setter Page
elif page == "Goal Setter":
    st.header("Set and Track Your Goals")
    
    # Input for new goal
    st.subheader("Create a New Goal")
    goal_title = st.text_input("Goal Title")
    goal_description = st.text_area("Goal Description")
    goal_deadline = st.date_input("Goal Deadline")
    goal_category = st.selectbox("Goal Category", ["Personal", "Professional", "Health", "Financial", "Other"])
    
    if st.button("Add Goal"):
        st.success(f"New goal added: {goal_title}")
    
    # Display existing goals
    st.subheader("Your Current Goals")
    goals = [
        {"title": "Learn Python", "progress": 60, "category": "Professional"},
        {"title": "Run a 5K", "progress": 40, "category": "Health"},
        {"title": "Save $1000", "progress": 75, "category": "Financial"}
    ]
    
    for goal in goals:
        col1, col2, col3 = st.columns([3, 1, 1])
        col1.write(f"**{goal['title']}** ({goal['category']})")
        col2.progress(goal['progress'])
        col3.write(f"{goal['progress']}%")

# Habit Tracker Page
elif page == "Habit Tracker":
    st.header("Build and Monitor Your Habits")
    
    # Input for new habit
    st.subheader("Start a New Habit")
    habit_name = st.text_input("Habit Name")
    habit_frequency = st.selectbox("Frequency", ["Daily", "Weekly"])
    
    if st.button("Add Habit"):
        st.success(f"New habit added: {habit_name}")
    
    # Display habit tracking
    st.subheader("Your Habit Tracker")
    habits = ["Read for 30 minutes", "Exercise", "Meditate", "Drink 8 glasses of water"]
    today = datetime.now().date()
    dates = [(today - timedelta(days=i)).strftime("%a") for i in range(7)][::-1]
    
    df = pd.DataFrame(index=habits, columns=dates)
    for habit in habits:
        for date in dates:
            df.loc[habit, date] = random.choice([True, False])
    
    st.table(df.style.applymap(lambda x: 'background-color: #90EE90' if x else 'background-color: #FFB3BA'))

# Mood Logger Page
elif page == "Mood Logger":
    st.header("Track Your Daily Mood")
    
    # Input for mood logging
    st.subheader("How are you feeling today?")
    mood_date = st.date_input("Date", datetime.now())
    mood_score = st.slider("Mood Score", 1, 10, 5)
    mood_notes = st.text_area("Any notes about your day?")
    
    if st.button("Log Mood"):
        st.success(f"Mood logged for {mood_date}")
    
    # Display mood trend
    st.subheader("Your Mood Trend")
    dates = pd.date_range(end=datetime.now(), periods=14).strftime("%Y-%m-%d").tolist()
    moods = [random.randint(1, 10) for _ in range(14)]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, moods, marker='o')
    ax.set_title("14-Day Mood Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Mood Score")
    ax.set_ylim(0, 10)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Track your growth, one day at a time. © 2023 Personal Growth Tracker")



