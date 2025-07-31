import streamlit as st
from homepage import homepage
from love import love_page
from salary import salary_page

st.set_page_config(page_title="Tặng Em 💖", page_icon=":sparkling_heart:", layout="wide")

st.title("💑 Ứng dụng dành riêng cho tình yêu của tụi mình")

page = st.sidebar.selectbox("📖 Chọn trang", ["Trang giới thiệu", "Trang tình cảm", "Tính lương"])

if page == "Trang giới thiệu":
    homepage()
elif page == "Trang tình cảm":
    love_page()
else:
    salary_page()
