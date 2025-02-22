import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="Personal Growth Journey", page_icon="🌱")
st.title("🌱 Personal Growth Journey: Evolve, Learn & Thrive")

# Sidebar for Navigation
st.sidebar.header("📌 Journey Map")
page = st.sidebar.radio("Explore:", [
    "🏡 Dashboard", "🌟 Daily Reflections", "📚 Learning Log", "🎭 Skill Development",
    "🧘 Mindfulness Corner", "🌍 Personal Projects", "🤝 Relationship Building", "🧠 Knowledge Hub"
])

# Dashboard
if page == "🏡 Dashboard":
    st.header("Welcome to Your Personal Growth Journey! 🌱")
    
    st.image("https://images.unsplash.com/photo-1552581234-26160f608093?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80", use_column_width=True)

    st.markdown("""
    ### Why Focus on Personal Growth?
    ✅ **Continuous Self-Improvement**: Evolve into your best self.  
    ✅ **Expand Your Horizons**: Learn new skills and perspectives.  
    ✅ **Enhance Relationships**: Grow alongside others.  
    ✅ **Achieve Personal Goals**: Turn aspirations into reality!  
    """)
    st.success("Your journey of personal growth starts now! Keep evolving! 🌱")
    
    # Inspirational Quote
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis"
    ]
    st.info(f"💡 **Today's Inspiration:** {random.choice(quotes)}")

# Daily Reflections
elif page == "🌟 Daily Reflections":
    st.header("🌟 Daily Reflections")
    reflection_areas = ["Gratitude", "Personal Wins", "Areas for Improvement", "Acts of Kindness", "New Insights"]

    for area in reflection_areas:
        st.text_area(f"Reflect on your {area.lower()}:")
    
    if st.button("Save Reflection"):
        st.success("Reflection saved! Great job on self-awareness!")
        st.balloons()

    # Mood Tracker
    st.subheader("Mood Tracker")
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    mood_levels = np.random.randint(1, 10, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, mood_levels, marker='o', linewidth=2, color='purple')
    ax.set_title("Weekly Mood Tracker")
    ax.set_ylabel("Mood (1-10)")
    ax.set_ylim(0, 10)
    st.pyplot(fig)

# Learning Log
elif page == "📚 Learning Log":
    st.header("📚 Learning Log")
    
    new_skill = st.text_input("What new skill or knowledge did you gain today?")
    learning_source = st.selectbox("How did you learn it?", ["Book", "Online Course", "Podcast", "YouTube", "Conversation", "Other"])
    
    if st.button("Log Learning"):
        st.success(f"Great job learning about {new_skill}!")

    # Learning Progress Chart
    st.subheader("Monthly Learning Progress")
    topics = ['Technology', 'Arts', 'Science', 'Language', 'Soft Skills']
    progress = np.random.randint(0, 100, size=len(topics))
    fig, ax = plt.subplots()
    ax.bar(topics, progress)
    ax.set_title("Learning Progress by Topic")
    ax.set_ylabel("Progress (%)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Skill Development
elif page == "🎭 Skill Development":
    st.header("🎭 Skill Development Tracker")
    skills = ["Public Speaking", "Writing", "Coding", "Design", "Time Management"]

    for skill in skills:
        st.slider(f"Rate your progress in {skill}:", 0, 100, 50)
    
    if st.button("Update Skills"):
        st.success("Skills updated! Keep practicing!")

    # Skill Web Chart
    st.subheader("Skill Web")
    angles = np.linspace(0, 2*np.pi, len(skills), endpoint=False)
    values = np.random.randint(50, 100, size=len(skills))
    values = np.concatenate((values, [values[0]]))  # repeat the first value to close the polygon
    angles = np.concatenate((angles, [angles[0]]))  # repeat the first angle to close the polygon
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(skills)
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Mindfulness Corner
elif page == "🧘 Mindfulness Corner":
    st.header("🧘 Mindfulness Corner")
    mindfulness_activities = ["Meditation", "Deep Breathing", "Gratitude Practice", "Nature Walk", "Journaling"]
    
    activity = st.selectbox("Choose a mindfulness activity:", mindfulness_activities)
    duration = st.number_input("Duration (minutes):", min_value=1, max_value=60, value=5)
    
    if st.button("Start Activity"):
        st.info(f"Enjoy your {duration} minutes of {activity}!")
        # Simulating the activity with a progress bar
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(duration/100)  # Adjust for real-time experience
            progress_bar.progress(i + 1)
        st.success("Activity completed! How do you feel?")

# Personal Projects
elif page == "🌍 Personal Projects":
    st.header("🌍 Personal Projects Hub")
    
    project_name = st.text_input("Project Name:")
    project_description = st.text_area("Project Description:")
    project_deadline = st.date_input("Project Deadline:")
    
    if st.button("Add Project"):
        st.success(f"Project '{project_name}' added! Let's make it happen!")

    # Project Timeline
    st.subheader("Project Timeline")
    projects = ["Learn Spanish", "Write a Book", "Run a Marathon", "Start a Blog"]
    start_dates = [date(2023, 1, 1), date(2023, 3, 15), date(2023, 6, 1), date(2023, 9, 1)]
    end_dates = [date(2023, 6, 30), date(2023, 12, 31), date(2023, 11, 30), date(2024, 2, 29)]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(projects, [(end - start).days for start, end in zip(start_dates, end_dates)], left=start_dates)
    ax.set_xlabel("Timeline")
    ax.set_ylabel("Projects")
    plt.tight_layout()
    st.pyplot(fig)

# Relationship Building
elif page == "🤝 Relationship Building":
    st.header("🤝 Relationship Building")
    
    relationship_goals = st.text_area("Set a relationship goal for today:")
    person = st.text_input("Person you want to connect with:")
    action = st.text_input("Action to strengthen the relationship:")
    
    if st.button("Log Interaction"):
        st.success(f"Great job reaching out to {person}!")

    # Relationship Strength Heatmap
    st.subheader("Relationship Strength Map")
    relationships = ["Family", "Friends", "Colleagues", "Community"]
    strength = np.random.randint(1, 10, size=(len(relationships), len(relationships)))
    fig, ax = plt.subplots()
    im = ax.imshow(strength, cmap="YlGnBu")
    ax.set_xticks(np.arange(len(relationships)))
    ax.set_yticks(np.arange(len(relationships)))
    ax.set_xticklabels(relationships)
    ax.set_yticklabels(relationships)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    for i in range(len(relationships)):
        for j in range(len(relationships)):
            text = ax.text(j, i, strength[i, j], ha="center", va="center", color="black")
    ax.set_title("Relationship Strength Heatmap")
    fig.tight_layout()
    st.pyplot(fig)

# Knowledge Hub
elif page == "🧠 Knowledge Hub":
    st.header("🧠 Knowledge Hub")
    
    topics = ["Science", "Technology", "Arts", "Philosophy", "History"]
    selected_topic = st.selectbox("Choose a topic to explore:", topics)
    
    st.write(f"Exploring {selected_topic}...")
    
    # Simulated knowledge quiz
    questions = [
        "What is the capital of France?",
        "Who painted the Mona Lisa?",
        "What is the chemical symbol for gold?"
    ]
    
    score = 0
    for question in questions:
        user_answer = st.text_input(question)
        if st.button(f"Submit Answer for '{question}'"):
            # Simple check (in real app, you'd have proper answer validation)
            if user_answer.lower() in ["paris", "leonardo da vinci", "au"]:
                st.success("Correct!")
                score += 1
            else:
                st.error("Not quite. Keep learning!")
    
    st.write(f"Your current score: {score}/{len(questions)}")

# Footer
st.markdown("---")
st.markdown("Crafted with 💖 for your personal growth | © 2025 Personal Growth Journey")

