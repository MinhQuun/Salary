import streamlit as st

def love_page():
    st.header("💌 Những điều anh muốn gửi đến em")
    
    st.markdown("""
    > “Yêu em không phải là lựa chọn. Mà là điều không thể không làm.”  

    Em biết không, mỗi ngày trôi qua anh đều thấy mình trưởng thành hơn — một phần lớn nhờ em.  
    Cảm ơn em đã từng yêu anh nhiều đến vậy. Dù hiện tại có ra sao, anh vẫn mong có thể đồng hành cùng em theo cách đúng đắn và dịu dàng nhất.

    ---
    **📸 Một số kỷ niệm của chúng ta:**
    """)
    
    st.header("💌 Những kỷ niệm đáng nhớ của chúng mình")

    st.markdown("""
    Đây là những khoảnh khắc đẹp mà anh muốn lưu giữ lại, để mỗi khi nhìn vào, anh sẽ nhớ về em và những điều tuyệt vời chúng ta đã trải qua cùng nhau.
                
    Anh hy vọng em sẽ thích những bức ảnh này, và chúng sẽ mang lại cho em những kỷ niệm ngọt ngào như chúng đã mang lại cho anh.
    Ở đây, anh không chỉ muốn lưu giữ những khoảnh khắc đẹp, mà còn muốn em cảm nhận được tình yêu và sự trân trọng mà anh dành cho em qua từng bức ảnh.
    Hãy cùng nhau nhìn lại những kỷ niệm đáng nhớ này nhé! 💖
                
    Hehe có những khoảnh khắc anh không chụp kịp hoặc không thể chụp nên caption hơi lạ nhan.
    """)

    # Danh sách ảnh và chú thích
    # Dữ liệu chia theo từng chuyến NT
    nt_memories = {
    "🩷 NT lần 1 – (25/06/2024)": [
        {"img": "assets/1.jpg", "caption": "Hun cái chụt nè 💕"},
        {"img": "assets/2.jpg", "caption": "Anh hun má vợ nè 🥰"},
        {"img": "assets/3.jpg", "caption": "Anh ôm vợ nè 😍"},
        {"img": "assets/7.jpg", "caption": "Hoàng tử tặng công chúa 🥺"},
        {"img": "assets/6.jpg", "caption": "Bông hoa ôm bông hoa 😄"},
        {"img": "assets/4.jpg", "caption": "Chồng iu đẹp trai 🥺"},
        {"img": "assets/5.jpg", "caption": "Ngày cuối đi ăn Jollibee 🥰"},
        {"img": "assets/8.jpg", "caption": "Kkk anh chờ mua bánh rồi quay lại ks để về nè 😘"},
    ],

    "🌺 NT lần 2 – (12/11/2024)": [
        {"img": "assets/9.jpg", "caption": "You're the apple of my eye 🍎"},
        {"img": "assets/10.jpg", "caption": "Gia tài kẹp của vợ thúi 🎀"},
        {"img": "assets/11.jpg", "caption": "Chàng tiên cá của em 🧜"},
        {"img": "assets/12.jpg", "caption": "Hai chị em nhà này xinh quá 👭"},
        {"img": "assets/13.jpg", "caption": "Làm miếng bánh tacos nha 🌮"},
        {"img": "assets/14.jpg", "caption": "Lần này là em hun anh cái chụt 😚"},
        {"img": "assets/15.jpg", "caption": "Vợ iu sexy quá 😘"},
        {"img": "assets/16.jpg", "caption": "Đại gia và chân dài 💃🕴️"},
        {"img": "assets/17.jpg", "caption": "Bị vợ iu hãm hiếp xong 😝"},
        {"img": "assets/18.jpg", "caption": "Đi siu thị GO cùng nhau 🛒"},
        {"img": "assets/19.jpg", "caption": "Ngồi ở siu thị nói chuyện nè ☕"},
        {"img": "assets/20.jpg", "caption": "Vợ iu xinh đẹp 🩷"},
    ],

    "💖 NT lần 3 – (28/06/2025)": [
        {"img": "assets/21.jpg", "caption": "Dắt anh xem bói nè 🔮"},
        {"img": "assets/22.jpg", "caption": "Em ôm anh 🤗"},
        {"img": "assets/23.jpg", "caption": "Anh ôm em 😚"},
        {"img": "assets/24.jpg", "caption": "123 chu mỏ 😘"},
        {"img": "assets/25.jpg", "caption": "Hun 1 cái 💏"},
        {"img": "assets/26.jpg", "caption": "Hai 1 cún 🐶"},
        {"img": "assets/27.jpg", "caption": "Kẹp cổ anh 😆"},
        {"img": "assets/28.jpg", "caption": "Kkk biến thái tí 🤪"},
        {"img": "assets/29.jpg", "caption": "Dễ thương dữ trời 😍"},
        {"img": "assets/30.jpg", "caption": "Lại thêm 1 dễ thương khác 🫶"},
    ],

    "🌈 NT lần 4 – (22/07/2025)": [
        {"img": "assets/31.jpg", "caption": "Đường tới nhà em, thấy đẹp quá nên chụp 🚶‍♂️🌳"},
        {"img": "assets/32.jpg", "caption": "Xin tấm ảnh cuối 😢"},
        {"img": "assets/33.jpg", "caption": "iu iu 💗"},
        {"img": "assets/34.jpg", "caption": "Đoán xem anh đang chỗ nào 🤔"},
        {"img": "assets/35.jpg", "caption": "Nhớ chỗ này hăm 🥹"},
        {"img": "assets/36.jpg", "caption": "Chụp trộm em ngủ nè 💤"},
        {"img": "assets/37.jpg", "caption": "Vợ iu và chùm nho 🍇"},
        {"img": "assets/38.jpg", "caption": "Xin chào cả nhà, đây là vợ iu tui 😍"},
    ],
}


    # Hiển thị từng đợt
    for trip, photos in nt_memories.items():
        st.subheader(trip)

        for i in range(0, len(photos), 2):
            col1, col2 = st.columns(2)

            with col1:
                if i < len(photos):
                    st.image(photos[i]["img"], caption=photos[i]["caption"], use_container_width=True)

            with col2:
                if i + 1 < len(photos):
                    st.image(photos[i + 1]["img"], caption=photos[i + 1]["caption"], use_container_width=True)

        st.markdown("---")

    st.markdown("---")
    st.write("❤️ Em là động lực để anh tốt hơn mỗi ngày.")

    st.header("🎓 Những bài học anh đã rút ra")

    st.markdown("""
    Anh đã dành nhiều thời gian để nhìn lại chính mình sau tất cả những gì đã xảy ra. Và anh hiểu rằng:

    - ❌ Yêu không chỉ là cảm xúc mà còn là trách nhiệm với cảm xúc của người kia.
    - 🧠 Ghen tuông, nóng nảy không phải là yêu - mà là nỗi sợ mất, cần học cách kiểm soát và tin tưởng.
    - 💬 Giao tiếp không phải để thắng - mà để hiểu và cùng nhau giải quyết.
    - 🕰️ Không thể đòi hỏi kết quả ngay lập tức - vì tình cảm cần được hồi phục từ từ, bằng sự kiên nhẫn và chân thành.
    - 💞 Một người con gái từng yêu mình nhiều như vậy - xứng đáng nhận được sự bình yên, thay vì mệt mỏi và nước mắt.

    Anh biết lời nói bây giờ không thể xoá hết tổn thương. Nhưng anh mong mỗi hành động từ nay về sau sẽ là một bước nhỏ để chữa lành, dù phải đi chậm – anh vẫn sẽ đi, nếu em còn ở cuối con đường đó.
    """)

    st.header("🌱 Điều anh đang cố gắng mỗi ngày")

    st.markdown("""
    Anh không chỉ nói những điều này cho có, mà mỗi ngày, anh đều đang thay đổi thật sự:

    - 🧘 Tập kiểm soát cảm xúc, không còn hành động bốc đồng như trước.
    - 📚 Học cách giao tiếp đúng, không làm em tổn thương bằng lời nói.
    - 🕊️ Tập sống tích cực, không ủ rũ, không phụ thuộc vào cảm xúc của người khác.
    - 💌 Không còn cố gắng níu kéo, mà cố gắng trở thành phiên bản mà em có thể yên tâm khi ở bên.

    Nếu một ngày nào đó em quay lại, anh muốn là người đàn ông khiến em cảm thấy **an toàn, dịu dàng và tự hào.**
    """)

    st.header("🌟 Nếu có thể một lần nữa…")

    st.markdown("""
    Anh không mong em quên hết những điều buồn, chỉ mong nếu một ngày nào đó em cảm thấy trái tim mình dịu lại...

    Anh sẽ:
    - Đến bên em bằng sự nhẹ nhàng, dịu dàng dù em có sao đi chăng nữa.
    - Nghe em nhiều hơn, hiểu em kỹ hơn, và yêu em đúng cách.
    - Không để em phải khóc vì sự vô tâm của anh nữa.
    
    Nhưng nếu điều đó không bao giờ đến…  
    Anh vẫn sẽ giữ em trong lòng như một người đã từng khiến anh muốn tốt lên, chỉ vì được ở bên em.
    """)



