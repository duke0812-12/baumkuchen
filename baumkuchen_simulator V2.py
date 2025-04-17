
import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="年輪蛋糕模擬器", page_icon="🎂")

st.title("🎂 年輪蛋糕模擬器（AI 模擬版）")
st.markdown("模擬不同製作參數對年輪蛋糕品質的影響，並由 AI 模型預測結果。")

st.sidebar.header("🔧 製作參數設定")

# 原料比例設定
eggs = st.sidebar.slider("蛋含量 (%)", 20, 40, 30)
sugar = st.sidebar.slider("糖含量 (%)", 20, 40, 30)
honey_ratio = st.sidebar.slider("蜂蜜替代糖比例 (%)", 0, 100, 0)
butter_fat = st.sidebar.slider("奶油脂肪率 (%)", 70, 85, 80)

# 攪拌參數
mix_time = st.sidebar.slider("攪拌時間 (分鐘)", 3, 15, 8)
mix_speed_label = st.sidebar.selectbox("攪拌速度", ["低速", "中速", "高速"])
mix_speed = {"低速": 0, "中速": 1, "高速": 2}[mix_speed_label]

# 烘烤參數
layer_count = st.sidebar.slider("烘烤層數", 5, 20, 12)
layer_time = st.sidebar.slider("每層烘烤時間 (秒)", 30, 120, 60)
bake_temp = st.sidebar.slider("烘烤溫度 (°C)", 180, 250, 220)

st.subheader("🧁 製作參數總覽")
st.write(f"🥚 蛋含量：{eggs}%")
st.write(f"🍯 蜂蜜比例：{honey_ratio}%")
st.write(f"🧈 奶油脂肪率：{butter_fat}%")
st.write(f"🌀 攪拌時間：{mix_time} 分鐘（{mix_speed_label}）")
st.write(f"🔥 烘烤層數：{layer_count} 層，每層 {layer_time} 秒，溫度 {bake_temp}°C")

if st.button("🚀 執行模擬"):
    st.markdown("---")
    st.subheader("🤖 AI 模型預測結果")

    # 載入模型
    model_softness = joblib.load("model_softness.pkl")
    model_color = joblib.load("model_color.pkl")
    model_accept = joblib.load("model_accept.pkl")

    # 建立輸入資料
    input_df = pd.DataFrame([{
        "eggs": eggs,
        "sugar": sugar,
        "honey_ratio": honey_ratio,
        "butter_fat": butter_fat,
        "mix_time": mix_time,
        "mix_speed": mix_speed,
        "layer_count": layer_count,
        "layer_time": layer_time,
        "bake_temp": bake_temp
    }])

    # 預測
    pred_softness = model_softness.predict(input_df)[0]
    pred_color = model_color.predict(input_df)[0]
    pred_accept = model_accept.predict(input_df)[0]

    # 顯示結果
    st.write(f"🧽 **濕潤柔軟度預測**：{pred_softness:.1f} / 100")
    st.write(f"🎨 **色澤飽和度預測**：{pred_color:.1f} / 100")
    st.write(f"👍 **整體接受度預測**：{pred_accept:.1f} / 100")

    # 簡單文字建議
    if pred_accept > 75:
        st.success("✨ 模擬結果極佳，推薦配方！")
    elif pred_accept > 50:
        st.info("🙂 模擬結果普通，可微調攪拌或蜂蜜比例")
    else:
        st.warning("⚠️ 預測接受度偏低，請考慮調整配方或烘烤條件")
