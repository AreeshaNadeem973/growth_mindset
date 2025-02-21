import streamlit as st
import pandas as pd
import os
import json
import random
from io import BytesIO

# Load or initialize data
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {"challenges": [], "journal": []}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# Streamlit App
st.set_page_config(page_title="Next-Gen Power: Mindset, Innovation & Success", layout="wide")
st.title("🚀 Next-Gen Power: Mindset, Innovation & Success")
st.sidebar.title("Explore")
page = st.sidebar.radio("Navigate to:", ["Home", "Today's Challenge", "Mindset Quiz", "Journal & Reflections", "Youth Innovation Hub"])

# Home Page
if page == "Home":
    st.header("Welcome to Next-Gen Power! ⚡")
    st.write("Empowering the youth with a growth mindset, innovation, and the drive for success!")
    
    st.image("https://source.unsplash.com/800x400/?success,motivation")
    
    st.subheader("🔥 The Power of a Growth Mindset")
    st.write("A growth mindset allows you to face challenges, learn from failures, and persist towards success.")
    
    st.subheader("🌍 Why This Matters for the Youth?")
    st.write("- Build confidence to overcome obstacles")
    st.write("- Learn from failures and turn them into stepping stones")
    st.write("- Think creatively and innovate")
    st.write("- Stay resilient and adaptable in the face of change")
    
    st.subheader("📈 Youth Success Insights")
    data_chart = pd.DataFrame({"Year": [2020, 2021, 2022, 2023, 2024], "Innovation Growth": [50, 65, 80, 90, 120]})
    st.line_chart(data_chart, use_container_width=True)
    
    st.subheader("🚀 Inspirational Quote")
    st.write("""_"The future belongs to those who believe in the beauty of their dreams." - Eleanor Roosevelt_""")

# Today's Challenge
elif page == "Today's Challenge":
    st.header("💡 Your Challenge for the Day")
    challenges = [
        "Try learning a new skill online today and document your progress.",
        "Share a mistake you made and how it helped you grow.",
        "Reach out to a mentor or role model and ask them for advice.",
        "Set a personal goal and write down three steps to achieve it.",
        "Encourage a friend to think positively and embrace challenges."
    ]
    challenge = random.choice(challenges)
    st.subheader("🚀 Challenge:")
    st.write(challenge)

    response = st.text_area("How will you complete this challenge?")
    if st.button("Submit Response"):
        data["challenges"].append({"challenge": challenge, "response": response})
        save_data(data)
        st.success("🎉 Your response has been saved!")

# Mindset Quiz
elif page == "Mindset Quiz":
    st.header("🧠 Test Your Growth Mindset")
    quiz_questions = [
        {"question": "What is a growth mindset?", "options": ["Avoiding failure", "Embracing challenges", "Giving up easily"], "answer": "Embracing challenges"},
        {"question": "How do you view mistakes?", "options": ["As failures", "As learning opportunities", "As things to avoid"], "answer": "As learning opportunities"}
    ]
    
    score = 0
    for q in quiz_questions:
        st.write(q["question"])
        option = st.radio("Choose an answer:", q["options"], key=q["question"])
        if option == q["answer"]:
            score += 1
    
    if st.button("Submit Quiz"):
        st.write(f"Your score: {score}/{len(quiz_questions)}")

# Journal & Reflections
elif page == "Journal & Reflections":
    st.header("📖 Write & Reflect")
    journal_entry = st.text_area("Write about your mindset journey today:")
    if st.button("Save Entry"):
        if journal_entry.strip():
            data["journal"].append(journal_entry)
            save_data(data)
            st.success("Journal entry saved!")
        else:
            st.error("Please write something before saving.")

    if data["journal"]:
        st.subheader("📝 Past Entries")
        for i, entry in enumerate(reversed(data["journal"])):
            st.write(f"*Entry {len(data['journal']) - i}:* {entry}")
    else:
        st.write("No entries yet. Start writing today!")

# Youth Innovation Hub
elif page == "Youth Innovation Hub":
    st.header("🌍 Youth Innovation & Success")
    st.write("This section highlights real-world success stories and innovative ideas from young minds.")
    
    stories = [
        {"name": "Elon Musk's Early Struggles", "summary": "Elon Musk faced multiple failures before achieving success with Tesla and SpaceX."},
        {"name": "Malala Yousafzai's Fight for Education", "summary": "Malala stood against all odds to advocate for girls' education worldwide."},
        {"name": "Nick D'Aloisio's Tech Innovation", "summary": "At 17, he sold his app Summly to Yahoo for millions, proving young minds can innovate!"}
    ]
    
    for story in stories:
        st.subheader(f"📌 {story['name']}")
        st.write(story["summary"])

st.success("🚀 Next-Gen Power Loaded! Keep learning & growing!")
