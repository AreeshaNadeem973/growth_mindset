import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import time

# App Title
st.title("🚀 Skill Mastery Tracker")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Dashboard", "📊 Skill Tracker", "✅ Task Manager", "⏱️ Focus Timer",
    "📝 Notes Manager", "📈 Progress Analytics", "🎯 Goals", "🏆 Achievements"
])

# Initialize session state
if 'skill_sessions' not in st.session_state:
    st.session_state.skill_sessions = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'notes' not in st.session_state:
    st.session_state.notes = []
if 'goals' not in st.session_state:
    st.session_state.goals = []

# Dashboard
if page == "🏠 Dashboard":
    st.header("Welcome to Skill Mastery Tracker! 🚀")
    st.markdown("""
    ### Your Learning Companion
    ✅ **Track Learning Time**  
    ✅ **Manage Learning Tasks**  
    ✅ **Take Notes**  
    ✅ **Set Skill Goals**  
    ✅ **Use Focus Timer**  
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Sessions", len(st.session_state.skill_sessions))
    with col2:
        st.metric("Tasks Done", len([t for t in st.session_state.tasks if t.get('completed', False)]))
    with col3:
        st.metric("Active Goals", len(st.session_state.goals))

# Skill Tracker
elif page == "📊 Skill Tracker":
    st.header("📊 Track Your Learning Sessions")

    with st.form("skill_session"):
        skill = st.selectbox("Skill:", ["Coding", "Design", "Marketing", "Finance", "Public Speaking"])
        duration = st.number_input("Duration (hours):", min_value=0.5, max_value=12.0, step=0.5)
        productivity = st.slider("Productivity Level (1-10):", 1, 10, 7)
        notes = st.text_area("Session Notes:")
        
        submitted = st.form_submit_button("Log Learning Session")
        if submitted:
            st.session_state.skill_sessions.append({
                "date": datetime.now(),
                "skill": skill,
                "duration": duration,
                "productivity": productivity,
                "notes": notes
            })
            st.balloons()
            st.success("Learning session logged successfully!")

    if st.session_state.skill_sessions:
        st.subheader("Skill Progress")
        skills = ["Coding", "Design", "Marketing", "Finance", "Public Speaking"]
        hours = [sum(s['duration'] for s in st.session_state.skill_sessions if s['skill'] == sk) for sk in skills]

        fig, ax = plt.subplots(figsize=(6, 4))
        colors = ['red', 'blue', 'green', 'yellow', 'pink']
        bars = ax.bar(skills, hours, color=colors)
        ax.set_ylabel('Hours Learned')
        ax.set_title('Hours per Skill')
        plt.xticks(rotation=45)
        plt.grid(True, axis='y')

        for bar in bars:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{bar.get_height():.1f}', ha='center', va='bottom')

        st.pyplot(fig)

# Task Manager
elif page == "✅ Task Manager":
    st.header("✅ Manage Your Learning Tasks")

    with st.form("new_task"):
        task_name = st.text_input("Task:")
        due_date = st.date_input("Due Date:")
        priority = st.selectbox("Priority:", ["High", "Medium", "Low"])

        if st.form_submit_button("Add Task"):
            st.session_state.tasks.append({
                "name": task_name,
                "due_date": due_date,
                "priority": priority,
                "completed": False
            })
            st.balloons()
            st.success("Task added!")

    if st.session_state.tasks:
        st.subheader("Your Tasks")
        for i, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.checkbox(task["name"], task["completed"], key=f"task_{i}"):
                    st.session_state.tasks[i]["completed"] = True
            with col2:
                st.write(f"Due: {task['due_date'].strftime('%Y-%m-%d')}")

# Focus Timer
elif page == "⏱️ Focus Timer":
    st.header("⏱️ Focus Timer")

    minutes = st.number_input("Duration (minutes):", min_value=1, max_value=60, value=25)
    if st.button("Start Timer"):
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i in range(minutes * 60):
            progress_bar.progress((i + 1) / (minutes * 60))
            mins_remaining = (minutes * 60 - i - 1) // 60
            secs_remaining = (minutes * 60 - i - 1) % 60
            status_text.text(f"Time remaining: {mins_remaining:02d}:{secs_remaining:02d}")
            time.sleep(1)

        st.success("Time's up! Take a break.")
        st.balloons()

# Notes Manager
elif page == "📝 Notes Manager":
    st.header("📝 Notes Manager")

    with st.form("new_note"):
        subject = st.selectbox("Skill:", ["Coding", "Design", "Marketing", "Finance", "Public Speaking"])
        title = st.text_input("Note Title:")
        content = st.text_area("Content:")

        if st.form_submit_button("Save Note"):
            st.session_state.notes.append({
                "subject": subject,
                "title": title,
                "content": content,
                "date": datetime.now()
            })
            st.balloons()
            st.success("Note saved!")

    if st.session_state.notes:
        st.subheader("Your Notes")
        for note in reversed(st.session_state.notes):
            with st.expander(f"{note['subject']} - {note['title']}"):
                st.write(note['content'])
                st.caption(f"Created: {note['date'].strftime('%Y-%m-%d %H:%M')}")

# Achievements
elif page == "🏆 Achievements":
    st.header("🏆 Your Achievements")

    total_hours = sum(s['duration'] for s in st.session_state.skill_sessions)
    completed_tasks = len([t for t in st.session_state.tasks if t.get('completed', False)])
    completed_goals = len([g for g in st.session_state.goals if g.get('completed', False)])

    achievements = [
        {"name": "Skill Pro", "desc": "Learn 50+ hours", "achieved": total_hours >= 50},
        {"name": "Task Finisher", "desc": "Complete 20+ tasks", "achieved": completed_tasks >= 20},
        {"name": "Goal Crusher", "desc": "Complete 5+ goals", "achieved": completed_goals >= 5}
    ]

    for achievement in achievements:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown("🏆" if achievement["achieved"] else "🔒")
        with col2:
            st.write(f"**{achievement['name']}**")
            st.write(achievement["desc"])

st.markdown("---")
st.markdown("🚀 *Developed with ❤️ using Streamlit. Master Your Skills!*")


