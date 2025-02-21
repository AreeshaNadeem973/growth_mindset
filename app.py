import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="🚀 Peak Performance Hub", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
pages = ["🏡 Home", "🏆 Success Stories", "🎯 Goal Setting", "💡 Productivity Hacks", "🌱 Growth Mindset"]
page = st.sidebar.radio("Go to", pages)

# Home Page
if page == "🏡 Home":
    st.header("🚀 Welcome to Peak Performance Hub! 🌟")
    
    st.markdown("""
    **🌱 Small Steps, Big Success!**  
    *Start your day with the right mindset and unstoppable energy.*  
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1573497491208-6b1acb260507", caption="📚 Learn & Grow", width=100)
        st.image("https://images.unsplash.com/photo-1517694712202-14dd9538aa97", caption="📅 Plan Your Day", width=100)
        
    with col2:
        st.image("https://images.unsplash.com/photo-1516542076529-1ea3854896f4", caption="🎯 Set Goals", width=100)
        st.image("https://images.unsplash.com/photo-1586281380349-632531db7ed5", caption="💡 Stay Inspired", width=100)
    
    with col3:
        st.image("https://images.unsplash.com/photo-1494883759339-0b042055a4ee", caption="🏋️‍♂️ Build Habits", width=100)
        st.image("https://images.unsplash.com/photo-1494390248081-4e521a5940db", caption="📖 Read & Reflect", width=100)
    
    st.success("💪 Every day is a fresh start! Stay focused and keep pushing forward! 🚀")
    
    quotes = [
        "🔥 Your future is created by what you do today, not tomorrow. - Robert Kiyosaki",
        "💡 The only way to do great work is to love what you do. - Steve Jobs",
        "🚀 You miss 100% of the shots you don’t take. - Wayne Gretzky",
        "🎯 Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
    ]
    st.info(f"💬 **Quote of the Day:** {random.choice(quotes)}")
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)  
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("📊 Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Success Stories
elif page == "🏆 Success Stories":
    st.header("🏆 Inspiring Success Stories")
    st.subheader("🚀 Learn from those who achieved greatness")
    st.markdown("""
    - **Elon Musk:** From PayPal to Tesla & SpaceX, relentless innovation drives success.  
    - **Oprah Winfrey:** Overcame hardships to build a media empire.  
    - **J.K. Rowling:** Rejected 12 times before *Harry Potter* became a global phenomenon.  
    - **Michael Jordan:** Cut from his high school basketball team, but went on to become the greatest.  
    """)
    
    st.image("https://images.unsplash.com/photo-1570129477492-45c003edd2be", caption="💪 Never Give Up!", use_column_width=True)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Master the Art of Goal Setting")
    st.markdown("""
    - **SMART Goals:** Make them Specific, Measurable, Achievable, Relevant, and Time-bound.
    - **Break Big Goals into Small Steps:** Achieve milestones consistently.
    - **Track Progress:** Regular self-checks increase success rates.
    """)
    
    st.image("https://images.unsplash.com/photo-1523289333742-be1143f77677", caption="📅 Plan & Execute", use_column_width=True)

# Productivity Hacks
elif page == "💡 Productivity Hacks":
    st.header("💡 Top Productivity Hacks")
    st.markdown("""
    - **The 5 AM Club:** Start your day early for peak performance.
    - **Pomodoro Technique:** Work in focused sprints with short breaks.
    - **Eliminate Distractions:** Use ‘Do Not Disturb’ mode and focus apps.
    - **Prioritize Tasks:** Use Eisenhower Matrix to differentiate urgent vs. important tasks.
    """)
    
    st.image("https://images.unsplash.com/photo-1568992687947-868a62a9f521", caption="🕒 Work Smart!", use_column_width=True)

# Growth Mindset
elif page == "🌱 Growth Mindset":
    st.header("🌱 Cultivate a Growth Mindset")
    st.markdown("""
    - **Embrace Challenges:** Growth happens outside the comfort zone.
    - **Learn from Criticism:** Feedback is the fuel for improvement.
    - **Stay Persistent:** Failures are just stepping stones to success.
    """)
    
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3", caption="🌟 Keep Growing!", use_column_width=True)
