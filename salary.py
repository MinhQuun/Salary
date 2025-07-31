import streamlit as st
import datetime
import calendar

def salary_page():
    st.title("📊 Tính lương theo tháng")

    # Nhập tháng, năm, lương
    col1, col2, col3 = st.columns(3)
    with col1:
        year = st.number_input("🗓️ Năm", min_value=2000, max_value=2100, value=datetime.datetime.now().year)
    with col2:
        month = st.number_input("📆 Tháng", min_value=1, max_value=12, value=datetime.datetime.now().month)
    with col3:
        hourly_wage = st.number_input("💰 Lương theo giờ (VNĐ)", min_value=0, value=19000, step=1000)

    # Tính số ngày
    _, num_days = calendar.monthrange(year, month)

    st.markdown("---")
    st.subheader(f"🕒 Nhập thời gian làm việc cho từng ngày (Tháng {month}/{year})")

    total_hours = 0.0
    daily_log = []

    for day in range(1, num_days + 1):
        date_str = f"{day:02d}/{month:02d}/{year}"
        key_prefix = f"{day}_{month}_{year}"

        with st.expander(f"📅 Ngày {date_str}"):
            is_day_off = st.checkbox("🛌 Nghỉ ngày này", key=f"off_{key_prefix}")

            if not is_day_off:
                col1, col2 = st.columns(2)
                with col1:
                    start = st.time_input("🕑 Giờ bắt đầu", key=f"start_{key_prefix}", value=None)
                with col2:
                    end = st.time_input("🕓 Giờ kết thúc", key=f"end_{key_prefix}", value=None)

                if start is not None and end is not None:
                    start_dt = datetime.datetime.combine(datetime.date(2000, 1, 1), start)
                    end_dt = datetime.datetime.combine(datetime.date(2000, 1, 1), end)

                    duration = (end_dt - start_dt).total_seconds() / 3600

                    if duration < 0:
                        st.error("❌ Giờ kết thúc phải sau giờ bắt đầu!")
                        duration = 0
                        status = "❌"
                        color = "red"
                    else:
                        st.success(f"✅ Số giờ làm: **{duration:.2f} giờ**")
                        st.success(f"💵 Lương ngày: **{duration * hourly_wage:,.0f} VNĐ**")
                        status = "✅"
                        color = "green"
                else:
                    st.warning("⚠️ Chưa nhập đủ giờ bắt đầu/kết thúc.")
                    duration = 0
                    status = "⚠️"
                    color = "orange"
            else:
                st.info("☑️ Nghỉ ngày này.")
                duration = 0
                status = "🛌"
                color = "#888888"

            daily_log.append({
                "ngày": date_str,
                "giờ làm": round(duration, 2),
                "lương ngày": round(duration * hourly_wage),
                "status": status,
                "color": color
            })

            total_hours += duration

    total_salary = total_hours * hourly_wage

    st.markdown("---")
    st.subheader("📊 Kết quả tổng kết")
    st.success(f"🕒 **Tổng số giờ làm:** {total_hours:.2f} giờ")
    st.success(f"💰 **Tổng lương tháng:** {total_salary:,.0f} VNĐ")

    # Bảng chi tiết
    with st.expander("📋 Bảng chi tiết từng ngày"):
        for log in daily_log:
            st.markdown(
                f"<div style='background-color:{log['color']};padding:8px;border-radius:8px;margin-bottom:5px;'>"
                f"<b>{log['status']}</b> {log['ngày']} — {log['giờ làm']} giờ → {log['lương ngày']:,} VNĐ"
                f"</div>",
                unsafe_allow_html=True
            )
