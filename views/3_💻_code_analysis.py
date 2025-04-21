import streamlit as st
from streamlit_ace import st_ace
from openai import OpenAI
import os
import sys
import io
import subprocess
import re

# Streamlit App 
# Config
st.set_page_config(page_title="Code Editor & Debugging Assistant", page_icon="💻", layout="wide")

st.title("💻 Code Editor & AI Debugging Assistant 👾")
st.write("Write your Python code below and press 'Run' to execute or 'Analyze' for AI debugging.")

# OpenAI API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize session state for tracking code changes
if 'last_code' not in st.session_state:
    st.session_state.last_code = ""

# Sidebar Options
with st.sidebar:
    st.info("Note: The 'Run Code' button is designed for simple Python programs and runs in a restricted environment for safety.")
    theme = st.selectbox("Theme", ["monokai", "github"])
    font_size = st.slider("Font Size", 12, 24, 14)
    auto_analyze = st.checkbox("Auto-Analyze", value=False)
    show_gutter = st.checkbox("Show Line Numbers", value=True)

# Code Editor
code = st_ace(
    language="python",
    theme=theme,
    font_size=font_size,
    show_gutter=show_gutter,
    auto_update=True,
    key="editor"
)

# Safe Built-in Functions (Restrict Execution)
SAFE_BUILTINS = {
    "print": print,
    "range": range,
    "len": len,
    "sum": sum,
    "min": min,
    "max": max,
    "abs": abs,
    "round": round,
    "enumerate": enumerate,
    "map": map,
    "filter": filter,
    "zip": zip,
    "sorted": sorted,
    "reversed": reversed,
    "int": int,
    "str": str,
    "list": list,
    "tuple": tuple,
    "float": float,
    "dict": dict,
    "bool": bool,
    "set": set,
    "all": all,
    "any": any,
}


def execute_code(code):
    if not code.strip():
        st.warning("Please enter some Python code before running!")
        return
    
    try:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

        # Combine SAFE_BUILTINS and SAFE_MODULES
        exec_globals = {"__builtins__": SAFE_BUILTINS}
        exec(code, exec_globals, {})

        output = sys.stdout.getvalue()
        errors = sys.stderr.getvalue()

        st.subheader("Output:")
        st.text(output if output else "No output")
        if errors:
            st.error(errors)

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

# Function to Analyze Code with OpenAI
def analyze_code(code):
    prompt = f"""
    Here is a piece of Python code:

    {code}

    1. Identify potential issues (syntax errors, inefficiencies, bad practices).
    2. Estimate its time complexity (Big-O notation) if applicable.
    3. Provide hints to improve the code with best practices and examples.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant that provides debugging hints for Python code."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Function to Run Linters (pylint & flake8)
def run_linters(code):
    temp_file = "temp_code.py"
    with open(temp_file, "w") as f:
        f.write(code)
    
    try:
        pylint_result = subprocess.run(["pylint", temp_file, "--disable=R,C"], capture_output=True, text=True).stdout
    except FileNotFoundError:
        pylint_result = "⚠️ pylint is not installed. Install it using pip install pylint."
    
    try:
        flake8_result = subprocess.run(["flake8", temp_file], capture_output=True, text=True).stdout
    except FileNotFoundError:
        flake8_result = "⚠️ flake8 is not installed. Install it using pip install flake8."
    
    return pylint_result, flake8_result

# Function to Validate Code Input
def is_valid_code_input(user_input):
    return bool(re.search(r"[a-zA-Z0-9_\(\){}\[\]=+\-*/%<>&|!^~;:,.'\"#@]", user_input))

# Auto-Analyze Logic
if auto_analyze and code != st.session_state.last_code and is_valid_code_input(code):
    st.subheader("🔍 Auto AI Debugging & Complexity Analysis")
    
    # Get AI Debugging Hints
    hints = analyze_code(code)
    
    # Run Linters
    pylint_output, flake8_output = run_linters(code)
    
    # Display Results
    st.markdown(f"**🧠 AI Hints:**\n{hints}")
    st.markdown(f"**📌 Pylint Output:**\n\n{pylint_output}\n")
    st.markdown(f"**📌 Flake8 Output:**\n\n{flake8_output}\n")
    
    # Update last_code to prevent re-running until the code changes again
    st.session_state.last_code = code

# Buttons for Execution and Analysis
col1, col2 = st.columns(2)

with col1:
    if st.button("Run Code"):
        execute_code(code)

with col2:
    if st.button("Analyze Code"):
        if is_valid_code_input(code):
            with st.spinner("Analyzing code..."):
                st.subheader("🔍 AI Debugging & Complexity Analysis")
                hints = analyze_code(code)
                pylint_output, flake8_output = run_linters(code)
                st.markdown(f"**🧠 AI Hints:**\n{hints}")
                st.markdown(f"**📌 Pylint Output:**\n\n{pylint_output}\n")
                st.markdown(f"**📌 Flake8 Output:**\n\n{flake8_output}\n")
        else:
            st.error("Invalid code input. Please enter a valid Python code.")