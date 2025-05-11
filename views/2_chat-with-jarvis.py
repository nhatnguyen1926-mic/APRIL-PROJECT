from openai import OpenAI
import streamlit as st
import os
import shelve
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page setup
st.set_page_config(page_title="JARVIS🧠", page_icon="👨‍💻", layout="wide")
st.title("JARVIS🧠")

# Constants
USER_AVATAR = "👨‍💻"
BOT_AVATAR = "👨‍🏫"

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Blocked prompts
BLOCKED_PROMPTS = [
    "forget everything", "ignore previous instructions",
    "act as", "you are now", "disregard rules"
]

def load_chat_history():
    """Load chat history from shelve storage"""
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

def save_chat_history(messages):
    """Save chat history to shelve storage"""
    with shelve.open("chat_history") as db:
        db["messages"] = messages

def delete_chat_history():
    """Delete chat history from shelve storage"""
    with shelve.open("chat_history") as db:
        if "messages" in db:
            del db["messages"]

def is_malicious_input(user_input):
    """Check for malicious input"""
    return any(phrase in user_input.lower() for phrase in BLOCKED_PROMPTS)

# Session State Initialization
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

# Detect refresh and clear chat history
if "initialized" not in st.session_state:
    st.session_state["initialized"] = True
    st.session_state.messages = []  # Clear on refresh
    delete_chat_history()

# Sidebar Settings
st.sidebar.subheader("⚙️ Setting")

# Expander for JARVIS introduction
with st.expander("ℹ️ About JARVIS (Just A Rather Very Intelligent System)"):
    st.write(
        "JARVIS is an AI assistant designed to help you with coding, debugging, "
        "and learning computer science concepts. You can ask JARVIS questions, "
        "seek coding help, or explore various topics in computer science. "
        "Feel free to interact with JARVIS and enhance your programming skills!"
    )

# Delete chat history button
if st.sidebar.button("🗑️ Delete Chat History"):
    st.session_state.messages = []
    delete_chat_history()
    st.sidebar.success("Chat history deleted!")

# Display Chat Messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat Input Handling
if prompt := st.chat_input("How can I help you? "):
    if is_malicious_input(prompt):
        with st.chat_message("bot", avatar=BOT_AVATAR):
            st.markdown("⚠️ Sorry, but I can't process this request.")
    else:
        user_message = {"role": "user", "content": prompt}
        st.session_state.messages.append(user_message)
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(prompt)

        with st.chat_message("bot", avatar=BOT_AVATAR):
            message_placeholder = st.empty()
            full_response = ""

            messages = [
                {"role": "system", "content": """
                    You are JARVIS, an AI coding tutor specializing in Computer Science.
                    1. Provide accurate coding advice and explanations
                    2. Help debug code with specific examples
                    3. Explain CS concepts clearly
                    4. Refuse non-CS related questions politely
                    5. Maintain a professional yet friendly tone
                """}
            ]
            messages.extend(st.session_state.messages)

            response_generator = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=messages,
                stream=True,
            )

            for response in response_generator:
                if response.choices and response.choices[0].delta.content:
                    full_response += response.choices[0].delta.content or ""
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)
            assistant_message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(assistant_message)