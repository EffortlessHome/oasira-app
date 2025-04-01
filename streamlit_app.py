
import streamlit as st
import time


#st.title("Oasira")
#st.write("Welcome")
#st.write("[Google](http://www.google.com)")

st.set_page_config(page_title="Smart Home Dashboard", layout="wide")

# --- STYLES ---
st.markdown("""
    <style>
        .main {background-color: #f8f8f8;}
        .stTabs [data-baseweb="tab-list"] {justify-content: center;}
        .stTabs [data-baseweb="tab"] {font-size: 20px; font-weight: 600;}
        .category-card {border-radius: 10px; padding: 20px; text-align: center; font-weight: bold;}
        .toggle {margin-top: 10px;}
        .music-box {border-radius: 15px; padding: 20px; background-color: #ffffff; text-align: center;}
        .camera-box {border-radius: 15px; padding: 20px; background-color: #ffffff;}
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
tabs = st.tabs(["My Home", "Living Room", "Kitchen", "Study", "Outdoor"])

with tabs[0]:  # "My Home" tab
    st.title("🏠 My Home")

    # --- CATEGORIES ---
    st.subheader("Categories")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown('<div class="category-card" style="background-color:#FFF5CC;">Lighting<br>8 lights</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="category-card" style="background-color:#E6F0FF;">Blinds<br>2 devices</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="category-card" style="background-color:#F0E6FF;">Cameras<br>4 devices</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="category-card" style="background-color:#FFE6E6;">Climate<br>2 devices</div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="category-card" style="background-color:#FFE6CC;">Speakers & TVs<br>5 devices</div>', unsafe_allow_html=True)

    st.markdown("---")

    # --- FAVORITES ---
    st.subheader("Favorites")
    col1, col2 = st.columns([2, 1])

    with col1:
        floor_lamp = st.toggle("Floor Lamp", value=False)
        bar_lamp = st.toggle("Bar Lamp", value=True)
        blinds = st.toggle("Blinds", value=True)

    with col2:
        # --- MUSIC PLAYER ---
        st.markdown('<div class="music-box">🎵 <b>Nest Mini</b><br><i>Bohemian Rhapsody - Queen</i></div>', unsafe_allow_html=True)
        progress = st.slider("Now Playing", 0, 100, 30)
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.button("⏮️")
        with col_m2:
            st.button("▶️" if progress == 0 else "⏸️")
        with col_m3:
            st.button("⏭️")

    st.markdown("---")

    # --- CAMERA ---
    st.subheader("Camera Feed")
    st.markdown('<div class="camera-box">📷 <b>Camera #1</b> - <span style="color:red;">🔴 Live</span></div>', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/400x200", caption="Live Camera View")