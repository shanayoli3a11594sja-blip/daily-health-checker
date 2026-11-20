import streamlit as st

# -------------------------------------------------
# Daily Health Checker
# A simple rule-based wellness tracker for students
# -------------------------------------------------

st.set_page_config(
    page_title="Daily Health Checker",
    page_icon="🌿",
    layout="centered"
)

def reset_inputs():
    """Clear all input values when the Reset button is clicked."""
    for key in [
        "name", "age", "sleep", "water",
        "exercise", "screen_time", "mood"
    ]:
        if key in st.session_state:
            del st.session_state[key]


st.title("🌿 Daily Health Checker")
st.write(
    "Welcome! Record your daily habits and get simple feedback "
    "about your lifestyle."
)
st.info(
    "This app gives general wellness suggestions only. "
    "It does not diagnose health conditions or replace advice from a doctor."
)

st.header("📝 Enter Your Daily Details")

name = st.text_input("Name", key="name")
age = st.number_input(
    "Age", min_value=5, max_value=100, value=14, step=1, key="age"
)
sleep = st.number_input(
    "Hours of sleep", min_value=0.0, max_value=24.0,
    value=8.0, step=0.5, key="sleep"
)
water = st.number_input(
    "Glasses of water consumed", min_value=0, max_value=30,
    value=6, step=1, key="water"
)
exercise = st.number_input(
    "Daily exercise duration (in minutes)", min_value=0,
    max_value=600, value=30, step=5, key="exercise"
)
screen_time = st.number_input(
    "Daily screen time (in hours)", min_value=0.0,
    max_value=24.0, value=3.0, step=0.5, key="screen_time"
)
mood = st.selectbox(
    "How is your mood today?",
    ["Happy", "Sad", "Stressed", "Energetic"],
    key="mood"
)

st.caption("Tip: Enter your details and click Check My Health.")

if st.button("🔍 Check My Health", type="primary"):
    if not name.strip():
        st.warning("Please enter your name first.")
    else:
        st.header("📊 Your Daily Health Summary")
        st.subheader(f"Hello, {name.strip()}!")

        # Sleep feedback
        if sleep < 7:
            st.warning("Sleep: You entered less than 7 hours. Try to follow a "
                       "regular, relaxing bedtime routine.")
        elif sleep <= 9:
            st.success("Sleep: Your sleep duration is in a generally helpful range.")
        else:
            st.info("Sleep: You entered more than 9 hours. Notice how rested "
                    "you feel and try to keep a regular sleep routine.")

        # Water feedback (simple tracking target, not a medical requirement)
        if water < 5:
            st.warning("Water: You recorded a few glasses. Keep water available "
                       "and drink regularly throughout the day.")
        elif water <= 8:
            st.success("Water: Good job keeping track of your water intake!")
        else:
            st.info("Water: You recorded plenty of glasses. Drink according "
                    "to your thirst and your day's activity.")

        # Exercise feedback
        if exercise < 20:
            st.warning("Exercise: Try adding a little enjoyable movement, "
                       "such as walking, cycling or playing a game.")
        elif exercise <= 60:
            st.success("Exercise: Nice work making time for movement!")
        else:
            st.info("Exercise: You had a long activity session. Remember to "
                    "take breaks and allow time for rest.")

        # Screen-time feedback
        if screen_time > 6:
            st.warning("Screen time: Consider taking regular screen breaks "
                       "and making time for offline activities.")
        elif screen_time >= 3:
            st.info("Screen time: Try balancing screen use with hobbies, "
                    "outdoor time and face-to-face activities.")
        else:
            st.success("Screen time: Your recorded screen time is relatively low. "
                       "Keep a healthy balance.")

        # Mood feedback
        if mood == "Happy":
            st.success("Mood: Great to hear you are feeling happy! Keep doing "
                       "activities that support your well-being.")
        elif mood == "Energetic":
            st.success("Mood: You are feeling energetic. Use that energy for "
                       "something enjoyable and take breaks when needed.")
        elif mood == "Sad":
            st.info("Mood: Everyone has difficult days. Consider talking to "
                    "someone you trust or doing a comforting activity.")
        else:
            st.info("Mood: If you feel stressed, try a short break, slow "
                    "breathing, or talking with someone you trust.")

        # Daily Wellness Score out of 100.
        # These are simple project scoring rules, not a medical measurement.
        score = 0

        if 7 <= sleep <= 9:
            score += 25
        elif sleep > 9:
            score += 20
        elif sleep >= 6:
            score += 15
        else:
            score += 5

        if water >= 8:
            score += 20
        elif water >= 5:
            score += 15
        elif water >= 3:
            score += 10
        else:
            score += 5

        if 20 <= exercise <= 60:
            score += 25
        elif exercise > 60:
            score += 20
        elif exercise >= 10:
            score += 15
        else:
            score += 5

        if screen_time < 3:
            score += 20
        elif screen_time <= 5:
            score += 15
        elif screen_time <= 7:
            score += 10
        else:
            score += 5

        if mood in ["Happy", "Energetic"]:
            score += 10
        else:
            score += 5

        st.header("⭐ Daily Wellness Score")
        st.metric("Your score", f"{score}/100")
        st.progress(score / 100)
        st.caption(
            "The score is based on the app's own simple points system. "
            "It is for this school project, not a clinical health score."
        )

        # Personalised recommendations
        st.header("💡 Recommendations")
        recommendations = []

        if sleep < 7:
            recommendations.append("Try to keep a consistent sleep and wake-up time.")
        if water < 5:
            recommendations.append("Keep a water bottle nearby and take regular water breaks.")
        if exercise < 20:
            recommendations.append("Try a short walk, stretching or a fun outdoor activity.")
        if screen_time > 5:
            recommendations.append("Take regular screen breaks and spend some time offline.")
        if mood in ["Sad", "Stressed"]:
            recommendations.append("Talk with a trusted adult, family member or friend about how you feel.")

        if recommendations:
            for item in recommendations:
                st.write("• " + item)
        else:
            st.success("You have a balanced set of habits in this check-in. Keep it up!")

        st.success("Your daily health check is complete!")


st.divider()
st.button("🔄 Reset / Clear Inputs", on_click=reset_inputs)
st.caption("Made with Python and Streamlit | Daily Health Checker")
