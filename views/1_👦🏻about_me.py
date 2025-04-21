import streamlit as st

# Title Section
st.set_page_config(page_title="About Me", page_icon="👦🏻")
st.title("About Me")

# Personal in4
st.subheader("Personal Information")

# Info
col1, col2 = st.columns([1, 2])  

with col1:
    st.image("profile/mic.jpg", width=350)  
    st.write("**Name:** Nguyen Tien Nhat Nguyen")
    st.write("**Location:** Vinh City, Nghe An Province")
    st.write("**Email:** [nhatnguyenmich274@gmail.com](mailto:nhatnguyenmich274@gmail.com)")
    st.write("**GitHub:** [nhatnguyen1926-mic](https://github.com/nhatnguyen1926-mic)")

with col2:
    st.write("**Education:** Vinh University High School For The Gifted")
    st.write("**Academic Achievement And Skill:**")
    st.write("- Fourth Prize in English Provincial Competition in 12th grade")
    st.write("- Self-Taught CS50 Introduction to Computer Science (Harvard University)")
    st.write("**Hobbies:** Cycling, Jogging")

# Reason for Pursuing Computer Science Section
st.divider()
st.subheader("Why I Pursue Computer Science")
st.write(
    """
    I am a passionate learner, currently focusing on exploring more the field of Computer Science, with a special interest in Artificial Intelligence.  
    I self-studied the CS50x course by Harvard University through YouTube lectures and problem sets. Initially, I majored in English, but I quickly fell in love with the excitement and challenge of pushing myself outside my comfort zone, especially through troubleshooting bugs and designing creative features.  

    My project, **'AI Coding Tutor'**, inspired by the CS50 Duck Debugger, reflects my dedication to continuous growth in Computer Science. I’m particularly excited about delving deeper into areas such as machine learning and natural language processing.
    """
)

# Optional Styling: Add some markdown for extra formatting
st.markdown("---")  # Horizontal line for separation
st.caption("### Thank you for reading! Feel free to reach out if you have any questions or suggestions.😊")