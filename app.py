import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
import time

# App Title and Configuration
st.set_page_config(page_title="Life Mastery Hub", page_icon="🌟", layout="wide")
st.title("🌟 Life Mastery Hub: Craft Your Ideal Life")

# Custom CSS for improved design
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f7f7f7, #e0e0e0);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("🧭 Journey Map")
page = st.sidebar.radio("Explore Your Path:", [
    "🏰 Realm of Possibilities", "🎭 Identity Forge", "🧠 Wisdom Workshop",
    "🌈 Harmony Haven", "🚀 Quantum Leap Tracker", "⚡ Power Habits Lab",
    "🌐 Synergy Sphere", "🗺️ Expedition of Knowledge"
])

# Realm of Possibilities (Home)
if page == "🏰 Realm of Possibilities":
    st.header("Welcome to Your Realm of Possibilities")
    
    col1, col2, col3 = st.columns([2,1,1])
    
    with col1:
        st.subheader("Today's Quest")
        quest = st.text_input("What's your main quest for today?")
        if st.button("Embark on Quest"):
            st.success(f"Your quest '{quest}' has begun. May your journey be legendary!")
        
        st.subheader("Realm Stats")
        realms = ['Mind', 'Body', 'Spirit', 'Relationships', 'Career']
        realm_stats = {realm: random.randint(50, 100) for realm in realms}
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(realms, realm_stats.values(), color=plt.cm.viridis(np.linspace(0, 1, len(realms))))
        ax.set_ylim(0, 100)
        ax.set_ylabel("Mastery Level")
        ax.set_title("Your Life Realms")
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}%', ha='center', va='bottom')
        
        st.pyplot(fig)
    
    with col2:
        st.subheader("Daily Power-Ups")
        st.write("Boost your realms:")
        if st.button("🧘 Meditate (Mind +5)"):
            st.info("Inner peace achieved. Mind strengthened!")
        if st.button("🏋️ Quick Workout (Body +5)"):
            st.info("Energy surging. Body invigorated!")
        if st.button("📞 Call a Friend (Relationships +5)"):
            st.info("Connection deepened. Relationship strengthened!")
    
    with col3:
        st.subheader("Wisdom Scroll")
        quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
        ]
        st.info(random.choice(quotes))

# Identity Forge
elif page == "🎭 Identity Forge":
    st.header("🎭 Identity Forge: Sculpt Your Ideal Self")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Craft Your Avatar")
        avatar_name = st.text_input("Your Avatar Name")
        avatar_archetype = st.selectbox("Choose Your Archetype", 
                                        ["The Hero", "The Sage", "The Explorer", "The Creator", "The Caregiver"])
        avatar_mission = st.text_area("Your Life Mission")
        
        if st.button("Forge Identity"):
            st.success(f"Identity forged! {avatar_name} the {avatar_archetype} is ready for the journey!")
    
    with col2:
        st.subheader("Character Stats")
        stats = ["Strength", "Intelligence", "Charisma", "Creativity", "Resilience"]
        values = [random.randint(50, 100) for _ in range(len(stats))]
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        angles = np.linspace(0, 2*np.pi, len(stats), endpoint=False)
        values += values[:1]
        angles = np.concatenate((angles, [angles[0]]))
        
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(stats)
        ax.set_ylim(0, 100)
        plt.title("Character Attributes")
        st.pyplot(fig)
    
    st.subheader("Skill Tree")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Mind Branch")
        st.progress(75)
        st.write("Critical Thinking")
        st.write("Creativity")
    with col2:
        st.write("Body Branch")
        st.progress(60)
        st.write("Strength")
        st.write("Agility")
    with col3:
        st.write("Spirit Branch")
        st.progress(80)
        st.write("Meditation")
        st.write("Empathy")

# Wisdom Workshop
elif page == "🧠 Wisdom Workshop":
    st.header("🧠 Wisdom Workshop: Sharpen Your Mind")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Today's Challenge")
        challenges = [
            "Solve a Rubik's Cube",
            "Learn 5 new words in a foreign language",
            "Explain a complex topic to a friend",
            "Write a short story in 15 minutes",
            "Memorize a poem or song lyrics"
        ]
        challenge = random.choice(challenges)
        st.info(f"Your challenge: {challenge}")
        if st.button("Complete Challenge"):
            st.success("Challenge completed! Your mind grows stronger.")
        
        st.subheader("Mind Palace")
        topics = ["Philosophy", "Science", "Arts", "History", "Technology"]
        knowledge = [random.randint(20, 100) for _ in topics]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        wedges, texts, autotexts = ax.pie(knowledge, labels=topics, autopct='%1.1f%%',
                                          textprops=dict(color="w"), colors=plt.cm.Spectral(np.linspace(0, 1, len(topics))))
        ax.set_title("Knowledge Distribution")
        st.pyplot(fig)
    
    with col2:
        st.subheader("Skill Mastery")
        skills = ["Critical Thinking", "Problem Solving", "Creativity", "Memory", "Focus"]
        levels = [random.randint(1, 10) for _ in skills]
        
        for skill, level in zip(skills, levels):
            st.write(f"{skill}: {'🧠' * level}")
        
        st.subheader("Brain Teaser")
        teasers = [
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "What has keys, but no locks; space, but no room; you can enter, but not go in?",
            "The more you take, the more you leave behind. What am I?"
        ]
        selected_teaser = random.choice(teasers)
        st.write(selected_teaser)
        answer = st.text_input("Your answer:")
        if st.button("Check Answer"):
            st.info("Great attempt! Keep exercising that brain.")

# Harmony Haven
elif page == "🌈 Harmony Haven":
    st.header("🌈 Harmony Haven: Balance Your Life Energies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Life Energy Wheel")
        energies = ["Physical", "Emotional", "Mental", "Spiritual", "Social", "Financial"]
        levels = [random.randint(50, 100) for _ in energies]
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        angles = np.linspace(0, 2*np.pi, len(energies), endpoint=False)
        levels += levels[:1]
        angles = np.concatenate((angles, [angles[0]]))
        
        ax.plot(angles, levels)
        ax.fill(angles, levels, alpha=0.3)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(energies)
        ax.set_ylim(0, 100)
        plt.title("Life Energy Balance")
        st.pyplot(fig)
    
    with col2:
        st.subheader("Harmony Rituals")
        rituals = {
            "Morning Meditation": st.checkbox("Morning Meditation"),
            "Gratitude Journaling": st.checkbox("Gratitude Journaling"),
            "Nature Walk": st.checkbox("Nature Walk"),
            "Acts of Kindness": st.checkbox("Acts of Kindness"),
            "Evening Reflection": st.checkbox("Evening Reflection")
        }
        if st.button("Complete Rituals"):
            completed = sum(rituals.values())
            st.success(f"You've completed {completed} harmony rituals. Inner peace intensifies!")
    
    st.subheader("Mood Tracker")
    moods = ["Joyful", "Peaceful", "Neutral", "Stressed", "Melancholic"]
    mood = st.select_slider("How are you feeling today?", options=moods)
    if st.button("Log Mood"):
        st.info(f"Mood logged: {mood}. Remember, every emotion is a valid part of your journey.")

# Quantum Leap Tracker
elif page == "🚀 Quantum Leap Tracker":
    st.header("🚀 Quantum Leap Tracker: Accelerate Your Growth")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Set a Quantum Goal")
        goal = st.text_input("What's your next big leap?")
        deadline = st.date_input("Target Date")
        importance = st.slider("Importance", 1, 10, 5)
        
        if st.button("Initiate Quantum Leap"):
            st.success(f"Quantum Goal '{goal}' set! The universe conspires in your favor.")
    
    with col2:
        st.subheader("Growth Accelerator")
        milestones = [
            "Learn a New Skill",
            "Overcome a Fear",
            "Achieve a Personal Best",
            "Help Someone Succeed",
            "Explore a New Place"
        ]
        completed_milestones = st.multiselect("Select completed milestones:", milestones)
        if st.button("Calculate Growth"):
            growth = len(completed_milestones) * 20
            st.metric("Personal Growth", f"{growth}%", f"+{growth}%")
    
    st.subheader("Leap Log")
    leaps = [
        {"date": "2023-01-15", "leap": "Ran first marathon"},
        {"date": "2023-03-01", "leap": "Started a business"},
        {"date": "2023-05-20", "leap": "Learned to code"},
        {"date": "2023-07-10", "leap": "Traveled solo internationally"}
    ]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for i, leap in enumerate(leaps):
        date = datetime.strptime(leap["date"], "%Y-%m-%d")
        ax.scatter(date, i, s=100, color='gold')
        ax.annotate(leap["leap"], (date, i), xytext=(10, 0), 
                    textcoords="offset points", ha='left', va='center')
    
    ax.set_yticks([])
    ax.set_title("Quantum Leap Timeline")
    plt.xticks(rotation=45)
    fig.tight_layout()
    st.pyplot(fig)

# Power Habits Lab
elif page == "⚡ Power Habits Lab":
    st.header("⚡ Power Habits Lab: Forge Your Destiny")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Habit Forge")
        new_habit = st.text_input("Enter a new power habit:")
        habit_type = st.selectbox("Habit Type", ["Keystone", "Supporting", "Breaking Bad Habit"])
        frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
        
        if st.button("Forge Habit"):
            st.success(f"Power habit '{new_habit}' forged! Your destiny awaits.")
    
    with col2:
        st.subheader("Habit Strength")
        habits = ["Morning Ritual", "Exercise", "Reading", "Meditation", "Gratitude"]
        strengths = [random.randint(1, 100) for _ in habits]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(habits, strengths, color=plt.cm.viridis(np.linspace(0, 1, len(habits))))
        ax.set_xlim(0, 100)
        ax.set_xlabel("Habit Strength")
        ax.set_title("Power Habits Mastery")
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2, f'{width}%', 
                    ha='left', va='center')
        
        st.pyplot(fig)
    
    st.subheader("21-Day Habit Challenge")
    habit_challenge = st.selectbox("Select a habit for the 21-day challenge:", 
                                   ["Waking up at 5 AM", "Cold Showers", "No Complaining", "Daily Exercise", "Mindful Eating"])
    
    progress = random.randint(1, 21)
    st.progress(progress / 21)
    st.write(f"Day {progress} of 21")
    
    if st.button("Complete Today's Challenge"):
        st.balloons()
        st.success("Another day conquered! Your willpower grows stronger.")

# Synergy Sphere
elif page == "🌐 Synergy Sphere":
    st.header("🌐 Synergy Sphere: Amplify Your Connections")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Forge New Connection")
        name = st.text_input("Name of new connection:")
        relationship = st.selectbox("Relationship Type", ["Friend", "Mentor", "Colleague", "Family", "Community Member"])
        synergy_level = st.slider("Initial Synergy Level", 1, 10, 5)
        
        if st.button("Create Connection"):
            st.success(f"New connection with {name} established! Your network grows stronger.")
    
    with col2:
        st.subheader("Connection Web")
        connections = ["Family", "Close Friends", "Colleagues", "Mentors", "Community"]
        strengths = [random.randint(50, 100) for _ in connections]
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        angles = np.linspace(0, 2*np.pi, len(connections), endpoint=False)
        strengths += strengths[:1]
        angles = np.concatenate((angles, [angles[0]]))
        
        ax.plot(angles, strengths)
        ax.fill(angles, strengths, alpha=0.3)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(connections)
        ax.set_ylim(0, 100)
        plt.title("Connection Strength Web")
        st.pyplot(fig)
    
    st.subheader("Synergy Booster")
    boost_connection = st.selectbox("Choose a connection to boost:", ["Alice (Friend)", "Bob (Mentor)", "Carol (Colleague)", "David (Family)"])
    boost_action = st.selectbox("Choose a synergy-boosting action:", ["Quality Time", "Deep Conversation", "Collaborative Project", "Acts of Kindness", "Shared Experience"])
    
    if st.button("Boost Synergy"):
        st.success(f"Synergy boosted with {boost_connection} through {boost_action}! Your connection grows stronger.")
    
    st.subheader("Network Influence Map")
    network_data = {
        'You': ['Family', 'Friends', 'Work'],
        'Family': ['Extended Family', 'Family Friends'],
        'Friends': ['School Friends', 'Hobby Groups'],
        'Work': ['Colleagues', 'Industry Contacts']
    }
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    def draw_network(center, radius, start_angle, end_angle, level=0):
        x = radius * np.cos(np.pi/2 - start_angle)
        y = radius * np.sin(np.pi/2 - start_angle)
        ax.scatter(x, y, s=100, color=plt.cm.viridis(level / 3))
        ax.annotate(center, (x, y), ha='center', va='center')
        
        if center in network_data:
            n = len(network_data[center])
            for i, subcenter in enumerate(network_data[center]):
                subangle = start_angle + (end_angle - start_angle) * (i + 0.5) / n
                subradius = radius + 1
                draw_network(subcenter, subradius, subangle - 0.2, subangle + 0.2, level+1)
                ax.plot([x, subradius * np.cos(np.pi/2 - subangle)],
                        [y, subradius * np.sin(np.pi/2 - subangle)], 'k-', alpha=0.2)
    
    draw_network("You", 0, 0, 2*np.pi)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis('off')
    plt.title("Your Network Influence Map")
    st.pyplot(fig)

# Expedition of Knowledge
elif page == "🗺️ Expedition of Knowledge":
    st.header("🗺️ Expedition of Knowledge: Chart Your Learning Adventure")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("New Knowledge Expedition")
        topic = st.text_input("What do you want to learn?")
        learning_method = st.selectbox("Choose your learning method:", ["Book", "Online Course", "Podcast", "Documentary", "Hands-on Project"])
        commitment = st.slider("Commitment Level (hours/week)", 1, 20, 5)
        
        if st.button("Embark on Learning Journey"):
            st.success(f"Your expedition to master {topic} has begun! Knowledge awaits!")
    
    with col2:
        st.subheader("Knowledge Archipelago")
        subjects = ["Science", "Philosophy", "Arts", "Technology", "History"]
        mastery = [random.randint(20, 100) for _ in subjects]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(subjects, mastery, color=plt.cm.Spectral(np.linspace(0, 1, len(subjects))))
        ax.set_ylabel("Mastery Level")
        ax.set_title("Your Knowledge Domains")
        
        for i, v in enumerate(mastery):
            ax.text(i, v + 1, f"{v}%", ha='center')
        
        st.pyplot(fig)
    
    st.subheader("Learning Log")
    log_date = st.date_input("Date of learning:")
    log_topic = st.text_input("What did you learn?")
    log_insights = st.text_area("Key insights:")
    
    if st.button("Record in Learning Log"):
        st.success("Your knowledge has been etched into the annals of your personal history!")
    
    st.subheader("Wisdom Path")
    learning_milestones = [
        {"date": "2023-01-15", "milestone": "Started learning Python"},
        {"date": "2023-03-01", "milestone": "Completed philosophy course"},
        {"date": "2023-05-20", "milestone": "Read 'Sapiens' by Yuval Noah Harari"},
        {"date": "2023-07-10", "milestone": "Attended AI conference"}
    ]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for i, milestone in enumerate(learning_milestones):
        date = datetime.strptime(milestone["date"], "%Y-%m-%d")
        ax.scatter(date, i, s=100, color='purple')
        ax.annotate(milestone["milestone"], (date, i), xytext=(10, 0), 
                    textcoords="offset points", ha='left', va='center')
    
    ax.set_yticks([])
    ax.set_title("Your Wisdom Path")
    plt.xticks(rotation=45)
    fig.tight_layout()
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Empowering your journey to mastery | © 2025 Life Mastery Hub")


