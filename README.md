# APRIL: AI-Powered Learning Platform

## Overview

**APRIL** is a multi-functional Streamlit-based platform designed to assist users in coding, debugging, essay mentoring, and learning computer science concepts. It leverages OpenAI's GPT-4 model to provide intelligent feedback and guidance. This project was inspired by the CS50 Duck Debugger and aims to help users enhance their programming and writing skills interactively.

## Video Demo

[![Watch the Demo](https://img.youtube.com/vi/BG2TIJh1r70/0.jpg)](https://youtu.be/BG2TIJh1r70)  

## Description

APRIL consists of four main features:

### 1. About Me
- A personal introduction page showcasing the developer's background, achievements, and interests.
- Includes a profile picture and contact information.
- Explains the motivation behind pursuing computer science and the inspiration for this project.

### 2. Chat with JARVIS
- **JARVIS** (Just A Rather Very Intelligent System) is an AI-powered coding tutor.
- Provides:
  - Accurate coding advice and explanations.
  - Debugging assistance with specific examples.
  - Clear explanations of computer science concepts.
- Maintains a professional yet friendly tone and politely refuses non-CS-related questions.

### 3. Code Analysis
- A code editor and debugging assistant.
- Features:
  - Syntax highlighting and customizable themes.
  - AI-powered debugging and complexity analysis.
  - Integration with `pylint` and `flake8` for linting.
  - Safe execution of Python code in a restricted environment.

### 4. Essay Mentor
- **FRIDAY** (a thoughtful writing mentor) helps users improve their essays.
- Provides:
  - Feedback on structure, grammar, and vocabulary.
  - Reflective questions to guide improvement.
  - Estimated scores based on IELTS-style criteria.
- Encourages self-reflection and revision without writing essays for users.

## Installation


1. **Set up a virtual environment**:
```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Add the following line to your `.env` file:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the application**:
   ```bash
   streamlit run main.py
   ```

###  Tech Stack

###  Frontend
- **Streamlit** – For building an intuitive, interactive web interface.
- **Streamlit Ace** – Code editor with syntax highlighting and customizable themes.

###  Backend & AI
- **OpenAI GPT-4** – Powers the AI features for coding, debugging, and essay mentoring.
- **Python** – Core language used to build the entire application.

###  Environment & Configuration
- **Python Dotenv** – Manages environment variables securely via a `.env` file.

###  Code Quality Tools
- **Pylint** – Enforces coding standards and detects code issues.
- **Flake8** – Ensures adherence to Python style guides.