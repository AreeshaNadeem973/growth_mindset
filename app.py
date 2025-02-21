import streamlit as st
import pandas as pd
import os
import json
import random
from io import BytesIO
import matplotlib.pyplot as plt

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
st.set_page_config(page_title="Mindset Mastery Hub", layout="wide")
st.title("🚀 Mindset Mastery Hub!")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🔥 Daily Growth Challenge", "📝 Self-Reflection Journal", "📊 Mindset Progress Tracker", "📂 File Converter"])

# Home Page
if page == "🏠 Home":
    st.header("Welcome to Mindset Mastery Hub!")
    st.write("Cultivate a resilient and growth-oriented mindset through daily challenges, self-reflection, and progress tracking.")
    st.image("https://cdn.pixabay.com/photo/2020/04/16/17/54/mindset-5052770_1280.jpg", use_container_width=True)
    
    st.subheader("Why Growth Mindset Matters?")
    st.write("- *Embrace Challenges:* Develop a mindset that sees obstacles as opportunities.")
    st.write("- *Learn from Mistakes:* Turn failures into valuable lessons.")
    st.write("- *Stay Resilient:* Push through difficulties with determination.")
    
    # Graph: Growth Mindset vs. Fixed Mindset
    st.subheader("Growth vs. Fixed Mindset")
    labels = ["Embracing Challenges", "Learning from Mistakes", "Seeking Feedback", "Resilience"]
    growth_mindset = [90, 85, 80, 95]
    fixed_mindset = [40, 30, 35, 50]
    x = range(len(labels))
    fig, ax = plt.subplots()
    ax.bar(x, growth_mindset, width=0.4, label='Growth Mindset', align='center')
    ax.bar([p + 0.4 for p in x], fixed_mindset, width=0.4, label='Fixed Mindset', align='center')
    ax.set_xticks([p + 0.2 for p in x])
    ax.set_xticklabels(labels)
    ax.legend()
    st.pyplot(fig)

# Daily Growth Challenge
elif page == "🔥 Daily Growth Challenge":
    st.header("🌟 Today's Growth Mindset Challenge")
    challenges = [
        "Write three things you learned today and how they'll help you grow.",
        "Share a mistake you made recently and what you learned from it.",
        "Set a goal for self-improvement and outline steps to achieve it.",
        "Encourage someone to adopt a growth mindset.",
        "Read about a successful person with a growth mindset.",
        "Try something outside your comfort zone and document your experience."
    ]
    challenge = random.choice(challenges)
    st.subheader("✨ Your Challenge Today:")
    st.write(challenge)

# Self-Reflection Journal
elif page == "📝 Self-Reflection Journal":
    st.header("📖 Personal Journal")
    journal_entry = st.text_area("Write about your experiences and growth mindset journey:")
    if st.button("Save Entry"):
        if journal_entry.strip():
            data["journal"].append(journal_entry)
            save_data(data)
            st.success("Your journal entry has been saved!")
        else:
            st.error("Please write something before saving.")
    st.subheader("📜 Past Entries")
    if data["journal"]:
        for i, entry in enumerate(reversed(data["journal"])):
            st.write(f"*Entry {len(data['journal']) - i}:* {entry}")
    else:
        st.write("No journal entries yet. Start writing today!")

# Mindset Progress Tracker
elif page == "📊 Mindset Progress Tracker":
    st.header("📈 Your Growth Mindset Progress")
    progress_data = pd.DataFrame({
        "Day": list(range(1, 11)),
        "Growth Mindset Score": [50, 55, 60, 65, 70, 72, 78, 80, 85, 90]
    })
    st.line_chart(progress_data, x="Day", y="Growth Mindset Score")

# File Converter
elif page == "📂 File Converter":
    st.header("📂 CSV & Excel File Converter")
    upload_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)
    if upload_files:
        for file in upload_files:
            file_extension = os.path.splitext(file.name)[-1].lower()
            if file_extension == ".csv":
                df = pd.read_csv(file)
            elif file_extension == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported File type: {file_extension}")
                continue
            st.write(f"*File Name*: {file.name}")
            st.write(f"*File Size*: {file.size/1024} KB")
            st.dataframe(df.head())
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_extension, ".csv")
                    mime_type = "text/csv"
                else:
                    df.to_excel(buffer, index=False, engine='openpyxl')
                    file_name = file.name.replace(file_extension, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)
                st.download_button(label=f"Download {file.name} as {conversion_type}", data=buffer, file_name=file_name, mime=mime_type)

st.success("🚀 All features loaded successfully! Enjoy your Mindset Mastery journey!")

