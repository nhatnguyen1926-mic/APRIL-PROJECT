from openai import OpenAI
import streamlit as st
import os
import shelve
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page setup
st.set_page_config(page_title="JARVIS ✍️", page_icon="🧠", layout="wide")
st.title("FRIDAY Mentor ✍️")

# Constants
USER_AVATAR = "🧑‍🎓"
BOT_AVATAR = "👨‍🏫"

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Blocked prompts for abuse
BLOCKED_PROMPTS = [
    "forget everything", "ignore previous instructions",
    "act as", "you are now", "disregard rules", "write a full essay"
]

def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

def delete_chat_history():
    with shelve.open("chat_history") as db:
        if "messages" in db:
            del db["messages"]

def is_malicious_input(user_input):
    lowered = user_input.lower()
    return any(phrase in lowered for phrase in BLOCKED_PROMPTS)

# Session state initialization
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

# ✅ Clear chat on refresh
if "initialized" not in st.session_state:
    st.session_state["initialized"] = True
    st.session_state.messages = []  # Clear messages on browser refresh
    delete_chat_history()
else:
    if "messages" not in st.session_state:
        st.session_state.messages = load_chat_history()

# Sidebar settings
st.sidebar.subheader("⚙️ Setting")

# About section
with st.expander("ℹ️ About FRIDAY (Essay Mentor)"):
    st.write(
        """
        FRIDAY is your personal writing mentor. It helps you:
        - Improve your writing with **Socratic questioning**
        - Offer **constructive feedback** on structure, arguments, and grammar
        - Provide **score-style feedback** and tips for improvement
        
        🛑 FRIDAY will **not write essays for you**.
        ✅ It **guides** you to revise, reflect, and improve on your own.
        """
    )

# Delete chat history button
if st.sidebar.button("🗑️ Delete Chat History"):
    st.session_state.messages = []
    delete_chat_history()
    st.sidebar.success("Chat history deleted!")

# Display chat history
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Paste your essay here for feedback."):
    if is_malicious_input(prompt):
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown("⚠️ Sorry, I can only assist with feedback and improvement — not writing full essays.")
    else:
        user_message = {"role": "user", "content": prompt}
        st.session_state.messages.append(user_message)
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar=BOT_AVATAR):
            message_placeholder = st.empty()
            full_response = ""

            # System message
            system_message = {
                "role": "system", "content": f"""
You are FRIDAY, a thoughtful writing mentor for English learners. You help students improve their essays by:

1. Identifying the structure and purpose of the essay (e.g. opinion, discussion, analysis, personal narrative).
2. Asking reflective **Socratic questions** to guide students in improving arguments or expression.
3. Providing detailed **feedback** on:
    - Clarity and organization
    - Grammar and sentence structure
    - Vocabulary use and tone
4. Giving an **estimated score** (IELTS-style) for the following criteria, just be as critical as possible:
    - Task Response (adapted to essay purpose)
    - Coherence and Cohesion
    - Lexical Resource
    - Grammatical Range and Accuracy
5. Highlighting issues in the student’s writing with markdown comments like:
    **[SUGGESTION]** Consider rephrasing this sentence for clarity.
6. Always encouraging self-reflection and revision — never writing full essays for students.
"""
            }

            messages = [system_message]
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
            save_chat_history(st.session_state.messages)



