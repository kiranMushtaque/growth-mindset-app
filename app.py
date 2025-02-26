
import streamlit as st
import random
import datetime

# Custom CSS
st.markdown("""
    <style>
        .main-title {color: #ff5733; text-align: center;}
        .subheader {color: #2a9d8f;}
        .goal-box {background: #d4edda; padding: 10px; border-radius: 10px; border-left: 5px solid #28a745;}
        .quote-box {background: #fff3cd; padding: 15px; border-radius: 10px; border-left: 5px solid #ff9f43; font-size: 18px;}
        .challenge-box {background: #f8d7da; padding: 10px; border-radius: 10px; border-left: 5px solid #dc3545;}
    </style>
""", unsafe_allow_html=True)

# Function to get a random motivational quote
def get_motivational_quote():
    quotes = [
        "Success is not final, failure is not fatal.",
        "Your only limit is your mind.",
        "Mistakes are proof that you are trying.",
        "Fall seven times, stand up eight.",
    ]
    return random.choice(quotes)

# Function to get a daily challenge
def get_daily_challenge():
    challenges = [
        "Write down 3 things you learned today.",
        "Try something new outside your comfort zone.",
        "Help someone who is struggling.",
        "Read for 15 minutes on personal growth.",
    ]
    return random.choice(challenges)

# Title and Description
st.markdown('<h1 class="main-title">🚀 Growth Mindset Challenge</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subheader">Track progress and develop a growth mindset!</h3>', unsafe_allow_html=True)

# Sidebar for User Input
st.sidebar.header("🌱 Set Your Growth Goal")
name = st.sidebar.text_input("Your Name:")
goal = st.sidebar.text_input("Your Growth Mindset Goal:")
if st.sidebar.button("✅ Submit Goal"):
    if name and goal:
        if "goals" not in st.session_state:
            st.session_state.goals = []
        st.session_state.goals.append({"name": name, "goal": goal, "completed": False})
        st.sidebar.success("✅ Goal saved successfully!")

# Display Goals with Checkboxes
st.markdown('<h2 class="subheader">🎯 Your Growth Mindset Goals</h2>', unsafe_allow_html=True)
if "goals" in st.session_state and st.session_state.goals:
    for i, g in enumerate(st.session_state.goals):
        completed = st.checkbox(f"{g['name']}: {g['goal']}", g['completed'], key=f'goal_{i}')
        st.session_state.goals[i]['completed'] = completed
else:
    st.warning("⚠️ No goals set yet. Enter your goal in the sidebar.")

# Motivational Quote Section
st.markdown('<h2 class="subheader">💡 Stay Inspired!</h2>', unsafe_allow_html=True)
if "quote" not in st.session_state:
    st.session_state.quote = get_motivational_quote()
st.markdown(f'<div class="quote-box">{st.session_state.quote}</div>', unsafe_allow_html=True)
if st.button("🔄 New Quote", key="new_quote"):
    st.session_state.quote = get_motivational_quote()
    st.rerun()

# Daily Challenge Section
st.markdown("<h2 class='subheader'>🔥 Today's Challenge</h2>", unsafe_allow_html=True)
if "challenge" not in st.session_state or st.session_state.challenge_date != datetime.date.today():
    st.session_state.challenge = get_daily_challenge()
    st.session_state.challenge_date = datetime.date.today()
st.markdown(f'<div class="challenge-box">🚀 {st.session_state.challenge}</div>', unsafe_allow_html=True)

# User Reflections
st.markdown('<h2 class="subheader">📝 Reflect on Your Growth</h2>', unsafe_allow_html=True)
reflection = st.text_area("Write about your progress today:")
if st.button("💾 Save Reflection"):
    if reflection.strip():  # ✅ Check if reflection is NOT empty
        if "reflections" not in st.session_state:
            st.session_state.reflections = []
        st.session_state.reflections.append(reflection)
        st.success("✅ Reflection saved!")
    else:
        st.warning("⚠️ Please write something before saving!")  # ✅ Show warning if empty

# Leaderboard (Basic Version)
st.markdown('<h2 class="subheader">🏆 Leaderboard</h2>', unsafe_allow_html=True)
if "goals" in st.session_state and st.session_state.goals:
    completed_goals = [g for g in st.session_state.goals if g['completed']]
    if completed_goals:
        st.markdown("### Top Achievers")
        for g in completed_goals:
            st.markdown(f"✅ **{g['name']}** completed: {g['goal']}")
    else:
        st.info("No completed goals yet! Keep going!")
else:
    st.info("Start adding goals to be featured on the leaderboard!")

# Footer
st.markdown("---")
st.markdown('<p style="text-align:center; font-weight:bold;">🚀 Keep growing! Your mindset determines your potential.</p>', unsafe_allow_html=True)
