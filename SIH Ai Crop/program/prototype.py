import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from gtts import gTTS
import base64


crops = [
    {"name": "Wheat", "yield": 3.2, "profit": 45000, "sustainability": 8, "risk": 0.25, "rotation": ["Pulses", "Mustard"]},
    {"name": "Rice", "yield": 2.8, "profit": 38000, "sustainability": 6, "risk": 0.40, "rotation": ["Pulses", "Vegetables"]},
    {"name": "Mustard", "yield": 2.5, "profit": 50000, "sustainability": 9, "risk": 0.20, "rotation": ["Wheat", "Vegetables"]},
    {"name": "Barley", "yield": 2.0, "profit": 30000, "sustainability": 7, "risk": 0.30, "rotation": ["Maize", "Mustard"]},
    {"name": "Maize", "yield": 3.0, "profit": 42000, "sustainability": 8, "risk": 0.22, "rotation": ["Potato", "Pulses"]},
]

def recommend_crops(soil, ph, rainfall, temp, prev_crop):
    return random.sample(crops, 3)  # random for demo

def text_to_speech(text, lang="hi"):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    with open(filename, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f'<audio autoplay controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'


# UI
st.set_page_config(page_title="AI Crop Advisor", page_icon="🌱", layout="wide")

st.title("🌱 AI-Powered Crop Recommendation System /")
st.title("AI संचालित फसल अनुशंसा प्रणाली")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("### 🤖 Personalized, science-guided advice for Indian farmers /")
st.markdown("### भारतीय किसानों के लिए व्यक्तिगत, विज्ञान-आधारित सलाह ")

# Input Sidebar
st.sidebar.header("🌍 Farm Details / खेत का विवरण")
soil = st.sidebar.selectbox("Soil Type / मिट्टी का प्रकार", ["Alluvial", "Black", "Red", "Sandy", "Laterite"])
ph = st.sidebar.slider("Soil pH / मिट्टी का pH", 3.5, 9.0, 6.5)
rainfall = st.sidebar.number_input("Rainfall (mm) / वर्षा (mm)", 0, 500, 120)
temp = st.sidebar.number_input("Temperature (°C) / तापमान (°C)", 5, 45, 25)
prev_crop = st.sidebar.selectbox("Previous Crop / पिछली फसल", ["None", "Wheat", "Rice", "Maize", "Mustard", "Barley"])

if st.sidebar.button("🚀 Recommend Crops / फसल सुझाएँ"):
    results = recommend_crops(soil, ph, rainfall, temp, prev_crop)
    df = pd.DataFrame(results)

    # Tabs
    tabs = st.tabs([
        "🌾 Recommendations / अनुशंसाएँ", 
        "📊 Smart Economics / स्मार्ट अर्थशास्त्र", 
        "🌍 Crop Rotation / फसल चक्र", 
        "🔊 Voice Assistant / वॉयस असिस्टेंट"
    ])

    # Recommendations Tab
    with tabs[0]:
        st.subheader("🌾 Recommended Crops for You / 🌾 आपके लिए अनुशंसित फसलें")
        for crop in results:
            col1, col2, col3, col4 = st.columns(4)
            with col1: st.metric("Crop / फ़सल", crop["name"])
            with col2: st.metric("Yield (t/ha) / उत्पादन (टन प्रति हेक्टेयर)", crop["yield"])
            with col3: st.metric("Profit / लाभ (₹)", f"{crop['profit']}")
            with col4: st.metric("Sustainability / स्थिरता", f"{crop['sustainability']}/10")

        # Profit Chart
        st.markdown("### 💰 Profit Comparison / लाभ तुलना")
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(df["name"], df["profit"], color=["#2e8b57", "#3cb371", "#66cdaa"])
        ax.set_ylabel("Profit (₹/hectare)")
        ax.set_title("Crop Profitability")
        st.pyplot(fig)

    # Economics Tab
    with tabs[1]:
        st.subheader("📊 Smart Economics Insights / स्मार्ट अर्थशास्त्र अंतर्दृष्टि")
        for crop in results:
            risk_level = "🟢 Low / कम" if crop["risk"] < 0.25 else "🟡 Medium / मध्यम" if crop["risk"] < 0.4 else "🔴 High / उच्च"
            score = round(crop["profit"] / (crop["risk"]*100000), 2)
    
            with st.container():
                st.write(f"**{crop['name']}** → Profit / लाभ: ₹{crop['profit']} | Risk / जोखिम: {risk_level} | Smart Score / स्मार्ट स्कोर: {score}")
                st.markdown("<br>", unsafe_allow_html=True)

    # Rotation Tab
    with tabs[2]:
        st.subheader("🌍 Smart Crop Rotation Planner / स्मार्ट फसल चक्र योजनाकार")
        for crop in results:
            with st.container():
                st.info(f"After **{crop['name']}** / **{crop['name']}** के बाद → {', '.join(crop['rotation'])}")
                st.markdown("<br>", unsafe_allow_html=True)

    # Voice Tab
    with tabs[3]:
        st.subheader("🔊 Voice Assistant / वॉयस असिस्टेंट")
        response_text = f"आपके खेत के लिए सबसे अच्छे फसल हैं {results[0]['name']}, {results[1]['name']} और {results[2]['name']}."
        st.markdown(text_to_speech(response_text, lang="hi"), unsafe_allow_html=True)
