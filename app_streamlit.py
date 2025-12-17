import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Mobile Price Predictor", layout="centered")

st.title("📱 Mobile Price Predictor")
st.write("Enter your mobile specifications to predict price range")

model = joblib.load("mobile_price_model.pkl")

battery_power = st.number_input("Battery Power (mAh)", 500, 6000, 4000)
blue = st.selectbox("Bluetooth", [0, 1])
clock_speed = st.number_input("Clock Speed (GHz)", 0.5, 3.0, 2.0)
dual_sim = st.selectbox("Dual SIM", [0, 1])
fc = st.number_input("Front Camera (MP)", 0, 50, 8)
four_g = st.selectbox("4G Support", [0, 1])
int_memory = st.number_input("Internal Memory (GB)", 2, 512, 64)
m_dep = st.number_input("Mobile Thickness", 0.1, 1.5, 0.8)
mobile_wt = st.number_input("Mobile Weight (g)", 80, 300, 180)
n_cores = st.number_input("Number of Cores", 1, 8, 8)
pc = st.number_input("Primary Camera (MP)", 2, 108, 48)
px_height = st.number_input("Pixel Height", 500, 3000, 1920)
px_width = st.number_input("Pixel Width", 500, 3000, 1080)
ram = st.number_input("RAM (MB)", 256, 12000, 6000)
sc_h = st.number_input("Screen Height (cm)", 5, 20, 15)
sc_w = st.number_input("Screen Width (cm)", 3, 15, 7)
talk_time = st.number_input("Talk Time (hours)", 2, 40, 20)
three_g = st.selectbox("3G Support", [0, 1])
touch_screen = st.selectbox("Touch Screen", [0, 1])
wifi = st.selectbox("WiFi", [0, 1])

features = np.array([[
    battery_power, blue, clock_speed, dual_sim, fc,
    four_g, int_memory, m_dep, mobile_wt, n_cores,
    pc, px_height, px_width, ram, sc_h, sc_w,
    talk_time, three_g, touch_screen, wifi
]])

if st.button("🔮 Predict Price Range"):
    prediction = model.predict(features)[0]

    price_map = {
        0: "Low Price 💰",
        1: "Medium Price 💵",
        2: "High Price 💸",
        3: "Very High Price 🤑"
    }

    st.success(f"Predicted Result: **{price_map[prediction]}**")
