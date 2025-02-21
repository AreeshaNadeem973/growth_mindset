import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import time

# App Title
st.title("📚 StudyFlow: Smart Study Planner")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Dashboard", "📊 Study Tracker", "✅ Task Manager", "⏱️ Focus Timer",
    "📝 Notes Manager", "📈 Progress Analytics", "🎯 Goals", "🏆 Achievements"
])

# Initialize session state
if 'study_sessions' not in st.session_state:
    st.session_state.study_sessions = []
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'notes' not in st.session_state:
    st.session_state.notes = []
if 'goals' not in st.session_state:
    st.session_state.goals = []

# Dashboard
if page == "🏠 Dashboard":
    st.header("Welcome to StudyFlow! 📚")
    st.markdown("""
    ### Your Study Companion
    ✅ **Track Study Time**: Monitor your study sessions  
    ✅ **Manage Tasks**: Stay organized with task lists  
    ✅ **Take Notes**: Keep your study notes organized  
    ✅ **Set Goals**: Track your academic progress  
    ✅ **Stay Focused**: Use our Pomodoro timer  
    """)
    
    # Quick Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Study Sessions", len(st.session_state.study_sessions))
    with col2:
        st.metric("Tasks Completed", len([t for t in st.session_state.tasks if t.get('completed', False)]))
    with col3:
        st.metric("Active Goals", len(st.session_state.goals))

# Study Tracker
elif page == "📊 Study Tracker":
    st.header("📊 Track Your Study Sessions")
    
    # Input form
    with st.form("study_session"):
        subject = st.selectbox("Subject:", ["Mathematics", "Science", "History", "Literature", "Languages"])
        duration = st.number_input("Duration (hours):", min_value=0.5, max_value=12.0, step=0.5)
        productivity = st.slider("Productivity Level (1-10):", 1, 10, 7)
        notes = st.text_area("Session Notes:")
        
        submitted = st.form_submit_button("Log Study Session")
        if submitted:
            st.session_state.study_sessions.append({
                "date": datetime.now(),
                "subject": subject,
                "duration": duration,
                "productivity": productivity,
                "notes": notes
            })
            st.balloons()
            st.success("Study session logged successfully!")

    # Display study statistics
    if st.session_state.study_sessions:
        st.subheader("Study Statistics")
        
        # Create bar chart similar to the provided image
        subjects = ["Mathematics", "Science", "History", "Literature", "Languages"]
        hours = [sum(s['duration'] for s in st.session_state.study_sessions if s['subject'] == sub) for sub in subjects]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = ['red', 'blue', 'green', 'yellow', 'pink']
        bars = ax.bar(subjects, hours, color=colors)
        
        ax.set_ylabel('Hours Studied')
        ax.set_title('Study Hours by Subject')
        plt.xticks(rotation=45)
        plt.grid(True, axis='y')
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom')
        
        st.pyplot(fig)

# Task Manager
elif page == "✅ Task Manager":
    st.header("✅ Manage Your Tasks")
    
    # Add new task
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

    # Display tasks
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
    st.header("⏱️ Pomodoro Focus Timer")
    
    minutes = st.number_input("Study Duration (minutes):", min_value=1, max_value=60, value=25)
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
    st.header("📝 Study Notes Manager")
    
    # Add new note
    with st.form("new_note"):
        subject = st.selectbox("Subject:", ["Mathematics", "Science", "History", "Literature", "Languages"])
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

    # Display notes
    if st.session_state.notes:
        st.subheader("Your Notes")
        for note in reversed(st.session_state.notes):
            with st.expander(f"{note['subject']} - {note['title']}"):
                st.write(note['content'])
                st.caption(f"Created: {note['date'].strftime('%Y-%m-%d %H:%M')}")

# Progress Analytics
elif page == "📈 Progress Analytics":
    st.header("📈 Your Progress Analytics")
    
    if st.session_state.study_sessions:
        # Study time distribution
        st.subheader("Study Time Distribution")
        subjects = ["Mathematics", "Science", "History", "Literature", "Languages"]
        times = [sum(s['duration'] for s in st.session_state.study_sessions if s['subject'] == sub) for sub in subjects]
        
        fig, ax = plt.subplots()
        ax.pie(times, labels=subjects, autopct='%1.1f%%')
        st.pyplot(fig)
        
        # Productivity trend
        st.subheader("Productivity Trend")
        dates = [s['date'] for s in st.session_state.study_sessions]
        productivity = [s['productivity'] for s in st.session_state.study_sessions]
        
        fig, ax = plt.subplots()
        ax.plot(dates, productivity, marker='o')
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Goals
elif page == "🎯 Goals":
    st.header("🎯 Set and Track Goals")
    
    # Add new goal
    with st.form("new_goal"):
        goal_title = st.text_input("Goal:")
        target_date = st.date_input("Target Date:")
        goal_type = st.selectbox("Type:", ["Academic", "Study Habit", "Skill Development"])
        
        if st.form_submit_button("Set Goal"):
            st.session_state.goals.append({
                "title": goal_title,
                "target_date": target_date,
                "type": goal_type,
                "completed": False
            })
            st.balloons()
            st.success("Goal set!")

    # Display goals
    if st.session_state.goals:
        st.subheader("Your Goals")
        for i, goal in enumerate(st.session_state.goals):
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(goal["title"])
            with col2:
                st.write(f"Due: {goal['target_date'].strftime('%Y-%m-%d')}")
            with col3:
                if st.button("Complete", key=f"goal_{i}"):
                    st.session_state.goals[i]["completed"] = True
                    st.balloons()

# Achievements
elif page == "🏆 Achievements":
    st.header("🏆 Your Achievements")
    
    # Calculate achievements
    total_study_hours = sum(s['duration'] for s in st.session_state.study_sessions)
    completed_tasks = len([t for t in st.session_state.tasks if t.get('completed', False)])
    completed_goals = len([g for g in st.session_state.goals if g.get('completed', False)])
    
    # Display achievements
    achievements = [
        {"name": "Study Champion", "desc": "Complete 50+ hours of studying", "achieved": total_study_hours >= 50},
        {"name": "Task Master", "desc": "Complete 20+ tasks", "achieved": completed_tasks >= 20},
        {"name": "Goal Getter", "desc": "Achieve 5+ goals", "achieved": completed_goals >= 5},
        {"name": "Focus Expert", "desc": "Complete 10+ focus sessions", "achieved": len(st.session_state.study_sessions) >= 10}
    ]
    
    for achievement in achievements:
        col1, col2 = st.columns([1, 3])
        with col1:
            if achievement["achieved"]:
                st.markdown("🏆")
            else:
                st.markdown("🔒")
        with col2:
            st.write(f"**{achievement['name']}**")
            st.write(achievement["desc"])

# Footer
st.markdown("---")
st.markdown("📚 *Developed with ❤️ using Streamlit. Study Smart, Achieve More!*")

