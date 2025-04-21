# AI Coding Tutor

Welcome to the **AI Coding Tutor** project! This application is a multi-functional Streamlit-based platform designed to assist users in coding, debugging, essay mentoring, and learning computer science concepts. It leverages OpenAI's GPT-4 model to provide intelligent feedback and guidance.

## Features

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

1. Clone the repository:
   ```bash
   git clone https://github.com/nhatnguyen1926-mic/ai-coding-tutor.git
   cd ai-coding-tutor

 2.Create a virtual environment:
 python3 -m venv myenv
 source myenv/bin/activate

 3. Install dependencies:
 pip install -r requirements.txt

 4.Set up environment variables:
  + Create a ".env" file in the root directory
  + Add your OpenAI API key:
  OPENAI_API_KEY = your_openai_api_key
