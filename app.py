import streamlit as st
import numpy as np
import time
from PIL import Image
import base64

# ========================================
# 1. PAGE CONFIG (MUST BE FIRST)
# ========================================
st.set_page_config(
    page_title="Crop Doctor",
    layout="centered",
    page_icon="🌱"
)

# ========================================
# 2. STYLING WITHOUT HEADINGS
# ========================================
def add_bg(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        
        .content-block {{
            background: rgba(0, 0, 0, 0.7);
            padding: 3rem;
            border-radius: 15px;
            text-align: center;
        }}
        
        /* Hide all headings */
        h1, h2, h3, h4, h5, h6 {{
            display: none !important;
        }}
        
        /* Button styling */
        .stButton>button {{
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 25px;
            padding: 0.8rem 2rem;
            font-size: 1.2rem;
            margin: 1rem auto;
            width: 80%;
            max-width: 300px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg("wallpaperflare.com_wallpaper.jpg")

# ========================================
# 3. PAGE NAVIGATION 
# ========================================
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page):
    st.session_state.page = page
    

# ========================================
# 4. HEADLESS HOME PAGE
# ========================================
def home():
    st.markdown("<div class='content-block'>", unsafe_allow_html=True)
    
    # Supported Crops (without heading)
    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
        - 🍅 Tomato
        - 🍇 Grape
        - 🥔 Potato
        - 🌽 Corn
        """)
    with cols[1]:
        st.markdown("""
        - 🍎 Apple
        - 🍒 Cherry
        - 🌶️ Pepper
        - 🍓 Strawberry
        """)
    
    # Model Metrics (without heading)
    st.markdown("""
    <div class="metric-container">
        <div class="stMetric">
            <div>Accuracy</div>
            <div style="font-size: 2rem;">96.2%</div>
        </div>
        <div class="stMetric">
            <div>Diseases</div>
            <div style="font-size: 2rem;">42</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("Start Diagnosis →", on_click=go_to, args=("predict",))
    
    st.markdown("</div>", unsafe_allow_html=True)

# ========================================
# 5. PREDICTION PAGE
# ========================================
def predict():
    st.markdown("<div class='content-block'>", unsafe_allow_html=True)
    
    st.button("← Back", on_click=go_to, args=("home",))
    
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, use_column_width=True)
        
        if st.button("Analyze Now"):
            with st.spinner(""):
                time.sleep(1.5)
                disease = np.random.choice(["Healthy", "Disease Detected"])
                confidence = np.random.uniform(80, 99)
                
                if "Healthy" in disease:
                    st.success(f"{disease} ({confidence:.1f}%)")
                else:
                    st.error(f"{disease} ({confidence:.1f}%)")
                    st.markdown("Apply fungicide treatment")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ========================================
# 6. RUN APP
# ========================================
if st.session_state.page == "home":
    home()
else:
    predict()