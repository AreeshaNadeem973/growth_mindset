import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# App Title
st.set_page_config(page_title="Life Optimizer", page_icon="⚡", layout="wide")
st.title("⚡ Life Optimizer: Unleash Your Potential")

# Sidebar for Navigation
st.sidebar.header("🧭 Navigation")
page = st.sidebar.radio("Explore:", [
    "🏠 Command Center", "🎯 Mission Control", "🧠 Mind Gym",
    "⚖️ Life Harmony", "🚀 Progress Pulse", "🔄 Habit Forge",
    "🌐 Connection Hub", "🗺️ Learning Odyssey"
])

# Command Center
if page == "🏠 Command Center":
    st.header("Welcome to Your Command Center")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Daily Focus")
        focus_area = st.selectbox("What's your main focus today?", 
                                  ["Personal Growth", "Career Development", "Health & Fitness", "Relationships", "Learning"])
        st.write(f"Great choice! Let's make progress on {focus_area} today.")
        
        st.subheader("Quick Wins")
        tasks = [
            st.checkbox("Complete 1 chapter of current book"),
            st.checkbox("15-minute workout"),
            st.checkbox("Meditate for 10 minutes"),
            st.checkbox("Connect with a friend or family member")
        ]
        if st.button("Log Quick Wins"):
            completed = sum(tasks)
            st.success(f"You've completed {completed} quick wins today! Keep up the momentum!")
    
    with col2:
        st.subheader("Productivity Pulse")
        dates = pd.date_range(end=datetime.now(), periods=7).strftime("%Y-%m-%d").tolist()
        productivity = [random.randint(50, 100) for _ in range(7)]
        df = pd.DataFrame({"Date": dates, "Productivity": productivity})
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Date'], df['Productivity'], marker='o')
        ax.set_title("7-Day Productivity Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("Productivity Score")
        ax.set_ylim(0, 100)
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        avg_productivity = np.mean(productivity)
        st.metric("Average Productivity", f"{avg_productivity:.1f}%", f"{avg_productivity - 75:.1f}%")

# Mission Control
elif page == "🎯 Mission Control":
    st.header("🎯 Mission Control: Goal Tracking & Project Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Set New Goal")
        goal_title = st.text_input("Goal Title")
        goal_description = st.text_area("Goal Description")
        goal_deadline = st.date_input("Deadline")
        goal_category = st.selectbox("Category", ["Career", "Personal", "Health", "Finance", "Relationships"])
        
        if st.button("Add Goal"):
            st.success(f"New goal added: {goal_title}")
    
    with col2:
        st.subheader("Active Goals")
        goals = [
            {"title": "Run a Marathon", "progress": 60, "category": "Health"},
            {"title": "Learn Python", "progress": 75, "category": "Career"},
            {"title": "Save $10,000", "progress": 45, "category": "Finance"},
            {"title": "Write a Book", "progress": 30, "category": "Personal"}
        ]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        categories = [goal['category'] for goal in goals]
        titles = [goal['title'] for goal in goals]
        progress = [goal['progress'] for goal in goals]
        
        colors = plt.cm.Spectral(np.linspace(0, 1, len(categories)))
        ax.barh(titles, progress, color=colors)
        ax.set_xlim(0, 100)
        ax.set_xlabel("Progress (%)")
        ax.set_title("Goal Progress Tracker")
        
        for i, v in enumerate(progress):
            ax.text(v + 1, i, f"{v}%", va='center')
        
        st.pyplot(fig)
    
    st.subheader("Project Kanban Board")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("### To Do")
        st.info("- Research new project ideas\n- Update resume\n- Plan weekend trip")
    
    with col2:
        st.markdown("### In Progress")
        st.warning("- Develop new app feature\n- Write blog post")
    
    with col3:
        st.markdown("### Review")
        st.success("- Code review for PR #123\n- Proofread report")
    
    with col4:
        st.markdown("### Done")
        st.error("- Team meeting\n- Gym session\n- Grocery shopping")

# Mind Gym
elif page == "🧠 Mind Gym":
    st.header("🧠 Mind Gym: Skill Development & Mental Fitness")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Skill Proficiency Tracker")
        skills = ["Critical Thinking", "Creativity", "Communication", "Leadership", "Problem Solving"]
        skill_levels = {skill: st.slider(f"{skill} proficiency:", 0, 100, 50) for skill in skills}
        
        if st.button("Update Skills"):
            st.success("Skills updated successfully!")
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        angles = np.linspace(0, 2*np.pi, len(skills), endpoint=False)
        values = list(skill_levels.values())
        values += values[:1]
        angles = np.concatenate((angles, [angles[0]]))
        
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(skills)
        ax.set_ylim(0, 100)
        plt.title("Skill Proficiency Web")
        st.pyplot(fig)
    
    with col2:
        st.subheader("Daily Brain Teaser")
        brain_teasers = [
            {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "answer": "An echo"},
            {"question": "You measure my life in hours and I serve you by expiring. I'm quick when I'm thin and slow when I'm fat. The wind is my enemy. What am I?", "answer": "A candle"},
            {"question": "What has keys, but no locks; space, but no room; you can enter, but not go in?", "answer": "A keyboard"}
        ]
        
        selected_teaser = random.choice(brain_teasers)
        st.write(selected_teaser["question"])
        user_answer = st.text_input("Your answer:")
        if st.button("Check Answer"):
            if user_answer.lower() == selected_teaser["answer"].lower():
                st.success("Correct! Great job!")
            else:
                st.error(f"Not quite. The answer is: {selected_teaser['answer']}")
        
        st.subheader("Mindfulness Minute")
        if st.button("Start 1-Minute Meditation"):
            st.info("Close your eyes, take deep breaths, and focus on the present moment.")
            latest_iteration = st.empty()
            bar = st.progress(0)
            for i in range(60):
                latest_iteration.text(f"{60 - i} seconds remaining")
                bar.progress((i + 1) * 100 // 60)
                time.sleep(1)
            st.success("Meditation complete. How do you feel?")

# Life Harmony
elif page == "⚖️ Life Harmony":
    st.header("⚖️ Life Harmony: Balancing Your Life Dimensions")
    
    life_dimensions = ["Career", "Finance", "Health", "Relationships", "Personal Growth", "Fun & Recreation"]
    satisfaction_levels = {dim: st.slider(f"Rate your satisfaction with {dim}:", 0, 10, 5) for dim in life_dimensions}
    
    if st.button("Update Life Harmony"):
        st.success("Life satisfaction levels updated!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        angles = np.linspace(0, 2*np.pi, len(life_dimensions), endpoint=False)
        values = list(satisfaction_levels.values())
        values += values[:1]
        angles = np.concatenate((angles, [angles[0]]))
        
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(life_dimensions)
        ax.set_ylim(0, 10)
        plt.title("Life Harmony Wheel")
        st.pyplot(fig)
    
    with col2:
        st.subheader("Life Harmony Insights")
        total_satisfaction = sum(satisfaction_levels.values())
        avg_satisfaction = total_satisfaction / len(life_dimensions)
        st.metric("Overall Life Satisfaction", f"{avg_satisfaction:.1f} / 10", f"{avg_satisfaction - 7:.1f}")
        
        max_dimension = max(satisfaction_levels, key=satisfaction_levels.get)
        min_dimension = min(satisfaction_levels, key=satisfaction_levels.get)
        
        st.write(f"💪 Strongest dimension: **{max_dimension}** ({satisfaction_levels[max_dimension]}/10)")
        st.write(f"🎯 Area for improvement: **{min_dimension}** ({satisfaction_levels[min_dimension]}/10)")
        
        st.subheader("Suggested Actions")
        if satisfaction_levels[min_dimension] < 5:
            st.warning(f"Consider focusing on improving your {min_dimension.lower()} dimension.")
            if min_dimension == "Health":
                st.write("- Schedule a health check-up")
                st.write("- Start a new exercise routine")
                st.write("- Plan healthier meals")
            elif min_dimension == "Relationships":
                st.write("- Plan quality time with loved ones")
                st.write("- Practice active listening")
                st.write("- Express gratitude to someone important")

# Progress Pulse
elif page == "🚀 Progress Pulse":
    st.header("🚀 Progress Pulse: Tracking Your Journey")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Log Daily Progress")
        progress_date = st.date_input("Date")
        progress_category = st.selectbox("Category", ["Career", "Health", "Learning", "Personal"])
        progress_description = st.text_area("What progress did you make today?")
        
        if st.button("Log Progress"):
            st.success("Progress logged successfully!")
    
    with col2:
        st.subheader("Progress Heatmap")
        dates = pd.date_range(end=datetime.now(), periods=30)
        categories = ["Career", "Health", "Learning", "Personal"]
        data = np.random.randint(0, 5, size=(len(categories), len(dates)))
        
        fig, ax = plt.subplots(figsize=(12, 6))
        im = ax.imshow(data, cmap="YlGn")
        
        ax.set_xticks(np.arange(len(dates)))
        ax.set_yticks(np.arange(len(categories)))
        ax.set_xticklabels([date.strftime("%d") for date in dates])
        ax.set_yticklabels(categories)
        
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        
        for i in range(len(categories)):
            for j in range(len(dates)):
                text = ax.text(j, i, data[i, j], ha="center", va="center", color="black")
        
        ax.set_title("30-Day Progress Heatmap")
        fig.tight_layout()
        st.pyplot(fig)
    
    st.subheader("Milestone Timeline")
    milestones = [
        {"date": "2023-01-15", "description": "Ran first 5K"},
        {"date": "2023-03-01", "description": "Completed online course"},
        {"date": "2023-04-20", "description": "Started new job"},
        {"date": "2023-06-10", "description": "Launched personal blog"}
    ]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for i, milestone in enumerate(milestones):
        date = datetime.strptime(milestone["date"], "%Y-%m-%d")
        ax.scatter(date, i, s=100, color='gold')
        ax.annotate(milestone["description"], (date, i), xytext=(10, 0), 
                    textcoords="offset points", ha='left', va='center')
    
    ax.set_yticks([])
    ax.set_title("Milestone Timeline")
    plt.xticks(rotation=45)
    fig.tight_layout()
    st.pyplot(fig)

# Habit Forge
elif page == "🔄 Habit Forge":
    st.header("🔄 Habit Forge: Building Lasting Habits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Create New Habit")
        habit_name = st.text_input("Habit Name")
        habit_category = st.selectbox("Category", ["Health", "Productivity", "Learning", "Relationships", "Personal Growth"])
        habit_frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
        habit_reminder = st.time_input("Set reminder time")
        
        if st.button("Add Habit"):
            st.success(f"New habit '{habit_name}' added successfully!")
    
    with col2:
        st.subheader("Habit Tracker")
        habits = ["Morning Meditation", "Read 30 minutes", "Exercise", "Drink 8 glasses of water", "Practice gratitude"]
        today = datetime.now().date()
        dates = [(today - timedelta(days=i)).strftime("%a") for i in range(7)][::-1]
        
        data = np.random.choice([0, 1], size=(len(habits), 7), p=[0.3, 0.7])
        
        fig, ax = plt.subplots(figsize=(12, 6))
        im = ax.imshow(data, cmap="YlGn")
        
        ax.set_xticks(np.arange(len(dates)))
        ax.set_yticks(np.arange(len(habits)))
        ax.set_xticklabels(dates)
        ax.set_yticklabels(habits)
        
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        
        for i in range(len(habits)):
            for j in range(len(dates)):
                text = ax.text(j, i, "✓" if data[i, j] else "", ha="center", va="center", color="black")
        
        ax.set_title("7-Day Habit Tracker")
        fig.tight_layout()
        st.pyplot(fig)
    
    st.subheader("Habit Streaks")
    habit_streaks = {
        "Morning Meditation": 15,
        "Read 30 minutes": 7,
        "Exercise": 21,
        "Drink 8 glasses of water": 30,
        "Practice gratitude": 10
    }
    
    fig, ax = plt.subplots(figsize=(10, 6))
    habits = list(habit_streaks.keys())
    streaks = list(habit_streaks.values())
    
    bars = ax.barh(habits, streaks)
    ax.set_xlabel("Current Streak (days)")
    ax.set_title("Habit Streaks")
    
    for i, v in enumerate(streaks):
        ax.text(v + 0.5, i, str(v), va='center')
    
    st.pyplot(fig)

# Connection Hub
elif page == "🌐 Connection Hub":
    st.header("🌐 Connection Hub: Nurturing Relationships")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add New Connection")
        connection_name = st.text_input("Name")
        connection_type = st.selectbox("Relationship Type", ["Family", "Friend", "Professional", "Mentor", "Mentee"])
        connection_notes = st.text_area("Notes")
        
        if st.button("Add Connection"):
            st.success(f"New connection '{connection_name}' added successfully!")
    
    with col2:
        st.subheader("Connection Strength")
        connections = {
            "Family": 9,
            "Close Friends": 8,
            "Colleagues": 6,
            "Professional Network": 7,
            "Community": 5
        }
        
        fig, ax = plt.subplots(figsize=(10, 6))
        categories = list(connections.keys())
        strengths = list(connections.values())
        
        bars = ax.bar(categories, strengths, color=plt.cm.viridis(np.linspace(0, 1, len(categories))))
        ax.set_ylim(0, 10)
        ax.set_ylabel("Connection Strength (0-10)")
        ax.set_title("Relationship Strength by Category")
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}',
                    ha='center', va='bottom')
        
        plt.xticks(rotation=45, ha='right')
        fig.tight_layout()
        st.pyplot(fig)
    
    st.subheader("Interaction Planner")
    st.write("Plan your next meaningful interaction:")
    interaction_person = st.selectbox("Choose a person", ["Alice (Family)", "Bob (Friend)", "Charlie (Mentor)", "Diana (Colleague)"])
    interaction_type = st.selectbox("Type of interaction", ["Call", "Meet for coffee", "Send a message", "Plan an activity"])
    interaction_date = st.date_input("When?")
    
    if st.button("Schedule Interaction"):
        st.success(f"Interaction with {interaction_person} scheduled for {interaction_date}!")

# Learning Odyssey
elif page == "🗺️ Learning Odyssey":
    st.header("🗺️ Learning Odyssey: Your Knowledge Adventure")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Log Learning Activity")
        learning_topic = st.text_input("What did you learn?")
        learning_category = st.selectbox("Category", ["Technology", "Science", "Arts", "History", "Language", "Other"])
        learning_method = st.selectbox("Learning Method", ["Book", "Online Course", "Podcast", "Video", "Practice", "Other"])
        learning_duration = st.number_input("Time spent (minutes)", min_value=5, max_value=480, value=30, step=5)
        
        if st.button("Log Learning"):
            st.success(f"Learning activity '{learning_topic}' logged successfully!")
    
    with col2:
        st.subheader("Knowledge Map")
        knowledge_areas = {
            "Technology": 75,
            "Science": 60,
            "Arts": 45,
            "History": 55,
            "Language": 70,
            "Philosophy": 40
        }
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        categories = list(knowledge_areas.keys())
        values = list(knowledge_areas.values())
        
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
        values += values[:1]
        angles = np.concatenate((angles, [angles[0]]))
        
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_ylim(0, 100)
        plt.title("Knowledge Area Proficiency")
        st.pyplot(fig)
    
    st.subheader("Learning Streak")
    learning_days = [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]  # 1 for learning day, 0 for no learning
    current_streak = sum(takewhile(lambda x: x == 1, reversed(learning_days)))
    
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.imshow([learning_days], cmap="YlGn", aspect="auto")
    ax.set_xticks(range(len(learning_days)))
    ax.set_xticklabels([f"Day {i+1}" for i in range(len(learning_days))])
    ax.set_yticks([])
    
    for i, day in enumerate(learning_days):
        ax.text(i, 0, "✓" if day else "✗", ha="center", va="center", color="black")
    
    ax.set_title(f"Learning Streak: {current_streak} days")
    st.pyplot(fig)
    
    st.metric("Current Learning Streak", f"{current_streak} days", f"+{current_streak}")

# Footer
st.markdown("---")
st.markdown("Empowering your journey to excellence | © 2025 Life Optimizer")


