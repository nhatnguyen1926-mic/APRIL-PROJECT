import streamlit as st

# --- PAGE SETUP ---

about_page = st.Page(
  page ="views/1_about_me.py",
  title = "About Me",
  default= True,
  )

project_1_page = st.Page(
  page = "views/2_chat-with-jarvis.py",
  title = "Chat With Jarvis",
)

project_2_page = st.Page(
  page = "views/3_code_analysis.py",
  title = "Jarvis Debugger Mode",
)
project_3_page = st.Page(
  page = "views/4_essay_mentor.py",
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