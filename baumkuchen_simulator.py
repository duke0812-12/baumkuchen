
import streamlit as st

st.set_page_config(page_title="年輪蛋糕模擬器", page_icon="🎂")

st.title("🎂 年輪蛋糕模擬器")
st.markdown("模擬不同製作參數對年輪蛋糕品質的影響。")

st.sidebar.header("🔧 製作參數設定")

# 原料比例設定
eggs = st.sidebar.slider("蛋含量 (%)", 20, 40, 30)
sugar = st.sidebar.slider("糖含量 (%)", 20, 40, 30)
honey_ratio = st.sidebar.slider("蜂蜜替代糖比例 (%)", 0, 100, 0)
butter_fat = st.sidebar.slider("奶油脂肪率 (%)", 70, 85, 80)

# 攪拌參數
mix_time = st.sidebar.slider("攪拌時間 (分鐘)", 3, 15, 8)
mix_speed = st.sidebar.selectbox("攪拌速度", ["低速", "中速", "高速"])

# 烘烤參數
layer_count = st.sidebar.slider("烘烤層數", 5, 20, 12)
layer_time = st.sidebar.slider("每層烘烤時間 (秒)", 30, 120, 60)
bake_temp = st.sidebar.slider("烘烤溫度 (°C)", 180, 250, 220)

# 模擬結果
st.subheader("🧁 模擬結果預測")
st.write(f"🥚 蛋含量為 {eggs}%")
st.write(f"🍯 蜂蜜佔糖比例為 {honey_ratio}%")
st.write(f"🧈 奶油脂肪率為 {butter_fat}%")
st.write(f"🌀 攪拌時間 {mix_time} 分鐘，速度為 {mix_speed}")
st.write(f"🔥 烘烤 {layer_count} 層，每層 {layer_time} 秒，溫度 {bake_temp}°C")

# 模擬簡易推論
if eggs >= 35 and honey_ratio > 30:
    st.success("預測：蛋糕濕潤、層次分明，蜂蜜香氣濃郁。")
elif mix_time < 5 or bake_temp > 240:
    st.warning("可能過乾或上色過深，建議調整時間或溫度。")
else:
    st.info("蛋糕質地適中，適合基礎年輪蛋糕。")
