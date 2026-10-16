import streamlit as st
import random
from datetime import datetime
from streamlit_mic_recorder import speech_to_text
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AI Mini Alexa",
    page_icon=" A",
    layout="centered"
)

st.title(" AI Mini Alexa")
st.caption("Your Virtual AI Assistant")

quotes = [
    "Believe in yourself.",
    "Keep going, you are doing great.",
    "Every day is a new opportunity."
]

facts = [
    "Python is a programming language.",
    "AI stands for Artificial Intelligence.",
    "Machine Learning is a part of AI."
]

if "history" not in st.session_state:
    st.session_state.history = []

def get_reply(command):
    command = command.lower().strip()

    if "hello" in command or command == "hi":
        return "Hello! How can I help you?"
    elif "time" in command:
        return "The current time is " + datetime.now().strftime("%I:%M %p")
    elif "date" in command:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")
    elif "quote" in command:
        return random.choice(quotes)
    elif "fact" in command:
        return random.choice(facts)
    elif "help" in command:
        return "Try hello, time, date, quote, fact, or help."
    else:
        return "I'm still learning that command. Try saying help!"

def add_message(speaker, message):
    st.session_state.history.append((speaker, message))

def process_command(command):
    if command and command.strip():
        add_message("You", command)
        reply = get_reply(command)
        add_message("Alexa", reply)

        # Speak the reply in the browser
        safe_reply = (
            reply.replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace("\n", " ")
        )
        components.html(
            f"""
            <script>
            const text = '{safe_reply}';
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                const msg = new SpeechSynthesisUtterance(text);
                msg.lang = 'en-IN';
                window.speechSynthesis.speak(msg);
            }}
            </script>
            """,
            height=0
        )

with st.sidebar:
    st.header("Available Commands")
    st.write(" Hello — Greeting")
    st.write(" Time — Current time")
    st.write(" Date — Today's date")
    st.write(" Quote — Motivational quote")
    st.write(" Fact — AI fact")
    st.write(" Help — Show commands")

    if st.button(" Clear conversation"):
        st.session_state.history = []
        st.rerun()

st.subheader(" Type to Alexa")

with st.form("chat_form", clear_on_submit=True):
    command = st.text_input("Ask me something:")
    submitted = st.form_submit_button("Ask Alexa")

if submitted:
    process_command(command)

st.subheader("AI Or talk to Alexa")

voice_command = speech_to_text(
    start_prompt="Start speaking",
    stop_prompt="Stop recording",
    language="en",
    just_once=True,
    key="voice_input"
)

if voice_command:
    process_command(voice_command)

st.subheader(" Conversation")

for speaker, message in st.session_state.history:
    with st.chat_message("user" if speaker == "You" else "assistant"):
        st.write(message)

st.caption("Built with Python and Streamlit")

