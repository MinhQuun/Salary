import streamlit as st

def homepage():
    st.header("👩‍❤️‍👨 Về chúng mình")

    st.markdown("""
    Chào vợ iu ❤️  
    Đây là một trang web nhỏ anh làm riêng cho em, để lưu lại những kỷ niệm, cảm xúc và cả những điều giản dị như... tính lương 😄  
    """)

    st.markdown("---")
    st.subheader("🧑👧 Thông tin của 2 đứa mình")

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/ckiu.jpg", caption="🧑 Võ Nguyễn Minh Quân", use_container_width=True)
        st.markdown("""
        - 🎂 Ngày sinh: 20/05/2004  
        - 💬 Tính cách: Kiên trì, nóng nảy chút xíu nhưng thật lòng, mà giờ đây đã hết cọc cằn r hehe  
        - 💘 Điều muốn nói: *Anh yêu em nhiều hơn những gì anh từng nghĩ...*
        """)

    with col2:
        st.image("assets/voiu.jpg", caption="👧 Nguyễn Thị Tú Trinh", use_container_width=True)
        st.markdown("""
        - 🎂 Ngày sinh: 12/05/2004  
        - 💬 Tính cách: Dễ thương, xinh gái, bướng bỉnh, thương anh quá trời  
        - 💘 Điều đáng nhớ: *Em đã từng yêu anh rất rất nhiều...*
        """)

    st.markdown("---")
    st.subheader("💌 Những điều anh muốn em nhớ")
    st.markdown("""
    🗓️ Ngày bắt đầu thương nhau: **26/03/2024**

    - Dù thế nào anh vẫn luôn muốn tốt hơn vì em.  
    - Anh xin lỗi vì những tổn thương đã từng gây ra.  
    - Anh muốn cùng em xây lại từ đầu, trưởng thành, nhẹ nhàng và hạnh phúc hơn.
    """)
