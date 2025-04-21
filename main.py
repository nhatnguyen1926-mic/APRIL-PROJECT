import streamlit as st

# --- PAGE SETUP ---

about_page = st.Page(
  page ="views/1_👦🏻about_me.py",
  title = "About Me",
  default = True,
  )

project_1_page = st.Page(
  page = "views/2_🏠_chat-with-jarvis.py",
  title = "Chat With Jarvis",
)

project_2_page = st.Page(
  page = "views/3_💻_code_analysis.py",
  title = "Jarvis Debugger Mode",
)
project_3_page = st.Page(
  page = "views/4_✍️_essay_mentor.py",
  title = "Essay Mentor"
)



# --- Navigation Setup (without sections) ---

pg = st.navigation(
  {
    "Infomation" : [about_page],
    "Features" : [project_1_page, project_2_page, project_3_page]
  }
)


# --- Run Navigation ---

pg.run()