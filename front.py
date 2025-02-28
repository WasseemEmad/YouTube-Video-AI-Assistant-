import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Store chat messages as a list of tuples (user, bot)

st.title("YouTube Video AI Assistant 🎥🤖")

# Input for YouTube URL
youtube_url = st.text_input("Enter YouTube URL:")

# Buttons for actions
col1, col2 = st.columns(2)
with col1:
    summarize = st.button("Summarize")
with col2:
    ask_question = st.button("Ask a Question")

# User Input for Questions
question = st.text_input("Ask a Question:")

# Handle Summarization
if summarize and youtube_url:
    response = requests.post(f"{FASTAPI_URL}/summary", json={"link": youtube_url})
    if response.status_code == 200:
        summary = response.json().get("summary", "⚠️ Failed to summarize.")
        st.session_state.chat_history.insert(0, ("🧑‍💻 You: (Requested Summary)", f"🤖 Bot: {summary}"))  # Prepend
    else:
        st.session_state.chat_history.insert(0, ("❌ Error", "⚠️ Failed to get summary."))

# Handle Questions
if ask_question and youtube_url and question:
    response = requests.post(f"{FASTAPI_URL}/questions", json={"link": youtube_url, "question": question})
    if response.status_code == 200:
        answer_text = response.json().get("bot_response", "⚠️ Failed to get answer.")
        st.session_state.chat_history.insert(0, (f"🧑‍💻 You: {question}", f"🤖 Bot: {answer_text}"))  # Prepend Q&A
    else:
        st.session_state.chat_history.insert(0, ("❌ Error", "⚠️ Failed to get answer."))

# Display chat messages (Newest at the Top)
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(user_msg)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)
