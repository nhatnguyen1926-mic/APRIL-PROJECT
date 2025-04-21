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

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nhatnguyen1926-mic/ai-coding-tutor.git
   cd ai-coding-tutor
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Add the following line to your `.env` file:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the application**:
   ```bash
   streamlit run main.py
   ```

## Project Structure

```
.
├── [main.py](http://_vscodecontentref_/0)                # Entry point for the Streamlit app
├── views/                 # Contains individual app pages
│   ├── 1_👦🏻about_me.py    # About Me page
│   ├── 2_🏠_chat-with-jarvis.py  # Chat with JARVIS page
│   ├── 3_💻_code_analysis.py    # Code Analysis page
│   ├── 4_✍️_essay_mentor.py     # Essay Mentor page
├── profile/               # Contains profile assets (e.g., images)
├── [requirements.txt](http://_vscodecontentref_/1)       # Python dependencies
├── .env                   # Environment variables
└── [README.md](http://_vscodecontentref_/2)              # Project documentation
```
