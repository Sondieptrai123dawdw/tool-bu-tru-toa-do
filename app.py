import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Tool Bù Trừ Nhanh", page_icon="⚙️", layout="centered"
)

st.title("⚙️ Tool Tính Nhanh Thông Số Bù Trừ")
st.write("Dùng trực tiếp trên điện thoại iPhone tại xưởng.")

# 1. Nhập liệu vị trí X, Y
st.subheader("1. Tọa độ X, Y")
col1, col2 = st.columns(2)
with col1:
  draw_x = st.number_input("Mục tiêu X (Bản vẽ)", value=1.67, format="%.3f")
  actual_x = st.number_input("Thực tế đo X", value=1.99, format="%.3f")
with col2:
  draw_y = st.number_input("Mục tiêu Y (Bản vẽ)", value=1.89, format="%.3f")
  actual_y = st.number_input("Thực tế đo Y", value=1.77, format="%.3f")

# 2. Nhập liệu góc xoay A
st.subheader("2. Góc xoay (Angle)")
col3, col4, col5 = st.columns(3)
with col3:
  d_top = st.number_input("Mũi tên trên (Thực tế)", value=1.99, format="%.3f")
with col4:
  d_bottom = st.number_input("Mục tiêu (Bản vẽ)", value=1.89, format="%.3f")
with col5:
  L_dist = st.number_input("Khoảng cách dọc L", value=6.165, format="%.3f")

# Nút tính toán kết quả
if st.button("🚀 XEM KẾT QUẢ BÙ TRỪ", type="primary"):
  delta_x = -(actual_x - draw_x)
  delta_y = draw_y - actual_y

  dim_diff = d_top - d_bottom
  angle_rad = np.arctan(dim_diff / L_dist)
  delta_angle = np.degrees(angle_rad)

  st.markdown("---")
  st.markdown("### 🎯 SỐ LIỆU CẦN NHẬP LÊN MÁY:")

  st.metric(label="Bù trừ Trục X", value=f"{delta_x:+.3f} mm")
  st.metric(label="Bù trừ Trục Y", value=f"{delta_y:+.3f} mm")
  st.metric(label="Bù trừ Góc Xoay (Angle)", value=f"{-delta_angle:+.2f}°")