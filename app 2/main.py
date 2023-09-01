# NOTE - We can use figma to make a prototype of our project.

import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Prabhnoor singh")
    content = "Hi I am Prabhnoor Singh! I am a Python Developer and my other skills include - " \
              "|| Data Science - Jupyter notebook || DBMS - Mysql and Mongodb || Ethical Hacking - Penetration tester || Debater and Public Speaker. "
    st.info(content)
