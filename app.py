# app.py - Streamlit demo for F1 Top-10 predictor (Enhanced F1-themed dark UI)
import os
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -------------------------
# PATHS & CONFIG
# -------------------------
st.set_page_config(
    page_title="F1 Top-10 Predictor",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_PATH = Path(__file__).resolve().parent
DATA_PATH = BASE_PATH / "processed"
MODEL_PATH = BASE_PATH / "models"

# --- UPDATED IMAGE PATH ---
# Pointing to the specific file inside your 'processed' folder
LOGO_PATH = DATA_PATH / "F1-logo-500x281png.webp" 

SAMPLE_IMG = Path("/mnt/data/817f8f73-88ea-4350-b46e-0deda2224a4c.png")

# -------------------------
# ENHANCED F1 DARK THEME CSS
# -------------------------
st.markdown("""
<style>
    /* Import fonts (optional - using fallbacks) */
    @import url('https://fonts.googleapis.com/css2?family=Titillium+Web:wght@400;600;700&display=swap');

    /* Main background - Deeper, smoother gradient */
    .stApp {
        background: radial-gradient(ellipse at top, #1a1a2e 0%, #0a0a0a 100%);
        color: #e0e0e0;
        font-family: 'Titillium Web', sans-serif;
    }

    /* Main container styling to make content pop */
    .main .block-container {
        background-color: rgba(20, 20, 20, 0.8);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        border: 1px solid #333;
        margin-top: 20px;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111116 0%, #08080a 100%);
        border-right: 3px solid #e10600;
        box-shadow: 5px 0 15px rgba(225, 6, 0, 0.1);
    }

    /* Headers */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ffffff !important;
        font-family: 'Titillium Web', sans-serif;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    h1 {
        background: linear-gradient(90deg, #ffffff 0%, #e10600 70%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        margin-bottom: 0px;
    }

    /* Input labels */
    .stTextInput label, .stNumberInput label, .stSelectbox label, .stSlider label, .stCheckbox label {
        color: #bbbbbb !important;
        font-weight: 600;
        font-size: 0.95rem;
        text-transform: uppercase;
    }

    /* Input boxes & Selects */
    input, select, [data-baseweb="select"] > div {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
        border-radius: 4px !important;
        transition: all 0.3s ease;
    }

    /* Focus state for inputs - Red Glow */
    input:focus, select:focus, [data-baseweb="select"] > div:focus-within {
        border-color: #e10600 !important;
        box-shadow: 0 0 10px rgba(225, 6, 0, 0.5) !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #c30000 0%, #ff1e00 100%);
        color: white;
        font-weight: 800;
        font-size: 1.2rem;
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 2px; /* Sharper corners for F1 feel */
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #ff1e00 0%, #e10600 100%);
        box-shadow: 0 0 25px rgba(225, 6, 0, 0.8);
        transform: translateY(-3px) skewX(-5deg); /* Slight skew for speed look */
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #e10600 !important;
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 10px rgba(225, 6, 0, 0.3);
    }

    [data-testid="stMetricLabel"] {
        color: #aaaaaa !important;
        font-size: 1.1rem !important;
        text-transform: uppercase;
        font-weight: 600;
    }

    /* Tables/Dataframes */
    .dataframe {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: none !important;
    }

    .dataframe th {
        background-color: #333 !important;
        color: #e10600 !important;
        font-weight: bold !important;
        text-transform: uppercase;
        border-bottom: 2px solid #e10600 !important;
    }

    .dataframe td {
        background-color: #1a1a1a !important;
        color: #dddddd !important;
        border: 1px solid #333 !important;
    }

    /* Alert boxes */
    .stAlert {
        background-color: rgba(26, 26, 26, 0.95);
        border: 1px solid rgba(255,255,255,0.1);
    }
    .stAlert[data-baseweb="notification"][class*="st-ae"] { /* Success Green */
         border-left: 5px solid #00d26a;
    }
    .stAlert[data-baseweb="notification"][class*="st-af"] { /* Info Yellow */
         border-left: 5px solid #fcd53f;
    }
    .stAlert[data-baseweb="notification"][class*="st-ag"] { /* Warning Red */
         border-left: 5px solid #e10600;
    }


    /* Dividers */
    hr {
        border-color: #444 !important;
        margin: 2em 0;
    }

    /* Racing stripes decoration */
    .racing-stripe {
        height: 6px;
        background: repeating-linear-gradient(
            -45deg,
            #e10600,
            #e10600 10px,
            #ffffff 10px,
            #ffffff 20px
        );
        margin: 10px 0 30px 0;
        border-radius: 2px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.5);
    }

    /* Sidebar Image Container */
    .sidebar-logo-container {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
        border-bottom: 4px solid #e10600;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Helper: friendly file check
# -------------------------
def assert_file(path: Path, desc: str):
    if not path.exists():
        st.error(f"⚠️ Required {desc} not found at:\n{path}")
        st.stop()

# -------------------------
# Load resources (cached)
# -------------------------
@st.cache_resource
def load_model_and_features(model_path: Path, feature_path: Path):
    assert_file(model_path, "model file (joblib)")
    assert_file(feature_path, "feature list (joblib)")
    model = joblib.load(model_path)
    feature_info = joblib.load(feature_path)
    if isinstance(feature_info, dict) and "features" in feature_info:
        features = feature_info["features"]
    elif isinstance(feature_info, list):
        features = feature_info
    else:
        raise ValueError("feature_list content not understood; expected dict with 'features' or list.")
    return model, features

@st.cache_resource
def load_lookup_csv(name: str):
    path = DATA_PATH / name
    # Return empty DF if missing instead of stopping, for robustness
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)

# -------------------------
# Initialization / checks
# -------------------------
MODEL_FILE = MODEL_PATH / "rf_top10_model.joblib"
FEATURES_FILE = MODEL_PATH / "feature_list.joblib"

if not DATA_PATH.exists():
    st.error(f"⚠️ Data folder not found: {DATA_PATH}")
    st.stop()
if not MODEL_PATH.exists():
    st.error(f"⚠️ Models folder not found: {MODEL_PATH}")
    st.stop()

try:
    model, features = load_model_and_features(MODEL_FILE, FEATURES_FILE)
except Exception as e:
    st.error("⚠️ Error loading model/features: " + str(e))
    st.stop()

drivers = load_lookup_csv("drivers.csv")
constructors = load_lookup_csv("constructors.csv")
races = load_lookup_csv("races.csv")

# -------------------------
# SIDEBAR - LOGO & INFO
# -------------------------
with st.sidebar:
    # Display the F1 Logo prominently
    if LOGO_PATH.exists():
        # Using a container with a white background so the logo looks correct
        st.markdown('<div class="sidebar-logo-container">', unsafe_allow_html=True)
        # FIX: use_container_width instead of use_column_width
        st.image(str(LOGO_PATH), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
         # Just a fallback warning, won't break the app
         st.warning(f"Image not found at: {LOGO_PATH}")

    st.markdown("### ℹ️ ABOUT")
    st.info(
        """
        This tool predicts the probability of an F1 driver finishing in the **Top 10** based on qualifying performance, historical data, and current season stats.
        """
    )
    st.markdown("---")
    st.markdown("**Model:** Random Forest Classifier")
    st.markdown(f"**Features:** {len(features)} inputs")

# -------------------------
# MAIN PAGE HEADER
# -------------------------
st.title("🏎️ F1 TOP-10 FINISH PREDICTOR")
st.markdown("### **LIGHTS OUT AND AWAY WE GO!**")
st.markdown('<div class="racing-stripe"></div>', unsafe_allow_html=True)

# -------------------------
# Layout: Two columns for inputs
# -------------------------
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 🏁 DRIVER & TEAM CONTEXT")

    if not drivers.empty and "surname" in drivers.columns:
        driver_choice = st.selectbox("DRIVER", options=sorted(drivers["surname"].unique()))
    else:
        driver_choice = st.text_input("DRIVER", placeholder="e.g., Hamilton")

    if not constructors.empty and "name" in constructors.columns:
        constructor_choice = st.selectbox("CONSTRUCTOR", options=sorted(constructors["name"].unique()))
    else:
        constructor_choice = st.text_input("CONSTRUCTOR", placeholder="e.g., Mercedes")

    if not races.empty and "name" in races.columns:
        race_choice = st.selectbox("GRAND PRIX", options=list(races["name"].unique()))
    else:
        race_choice = st.text_input("GRAND PRIX", placeholder="e.g., Monaco Grand Prix")

    st.markdown("### 📊 QUALIFYING PERFORMANCE")
    c1a, c1b = st.columns(2)
    with c1a:
        grid = st.number_input("GRID POSITION", min_value=1, max_value=40, value=10, help="Starting position on Sunday")
    with c1b:
        qual_pos = st.number_input("QUALIFYING RESULT", min_value=1, max_value=40, value=10, help="Saturday's qualifying classification")

    st.markdown("### 🏆 SEASON STANDINGS (Pre-Race)")
    c2a, c2b = st.columns(2)
    with c2a:
        driver_points_so_far = st.number_input("DRIVER POINTS", min_value=0.0, max_value=3000.0, value=50.0, step=1.0)
        driver_rank_season = st.number_input("DRIVER RANK", min_value=1, max_value=50, value=5)
    with c2b:
        constructor_points_so_far = st.number_input("CONSTRUCTOR POINTS", min_value=0.0, max_value=5000.0, value=120.0, step=1.0)
        constructor_rank_season = st.number_input("CONSTRUCTOR RANK", min_value=1, max_value=50, value=2)

with col2:
    st.markdown("### 📈 RECENT FORM (Last 3 Races)")
    recent_mean_finish = st.number_input("DRIVER AVG FINISH", min_value=1.0, max_value=30.0, value=12.0, step=0.1)
    recent_top10_rate = st.slider("DRIVER TOP-10 RATE", min_value=0.0, max_value=1.0, value=0.30, step=0.01, help="Percentage of recent races finished in points")
    constr_recent_mean_finish = st.number_input("CONSTRUCTOR AVG FINISH", min_value=1.0, max_value=30.0, value=11.0, step=0.1)

    st.markdown("### 🔧 PIT STRATEGY & TRACK")
    c3a, c3b = st.columns(2)
    with c3a:
         pit_stop_count = st.number_input("EST. PIT STOPS", min_value=0, max_value=5, value=1)
    with c3b:
         circuit_is_street = st.checkbox("STREET CIRCUIT?", value=False)

    st.markdown("##### Pit Stop Timing (Advanced)")
    # Using columns for tighter layout of technical inputs
    c4a, c4b = st.columns(2)
    with c4a:
        avg_pit_time = st.number_input("AVG PIT TIME (ms)", min_value=0, max_value=200000, value=22000, step=500)
    with c4b:
        total_pit_time = st.number_input("TOTAL PIT TIME (ms)", min_value=0, max_value=300000, value=22000, step=500)

    slow_pit_flag = st.checkbox("PREDICT SLOW STOP ISSUE?", value=False, help="Check if anticipating a major issue (>4s stationary)")


# -------------------------
# Prepare the feature vector
# -------------------------
input_dict = {
    'grid': grid,
    'qual_pos': qual_pos,
    'recent_mean_finish': recent_mean_finish,
    'recent_top10_rate': recent_top10_rate,
    'constr_recent_mean_finish': constr_recent_mean_finish,
    'pit_stop_count': pit_stop_count,
    'total_pit_time': total_pit_time,
    'avg_pit_time': avg_pit_time,
    'slow_pit_flag': int(slow_pit_flag),
    'circuit_is_street': int(circuit_is_street),
    'driver_points_so_far': driver_points_so_far,
    'driver_rank_season': driver_rank_season,
    'constructor_points_so_far': constructor_points_so_far,
    'constructor_rank_season': constructor_rank_season
}

X_in = pd.DataFrame([input_dict])
# Ensure all model features exist, fill missing with 0
for f in features:
    if f not in X_in.columns:
        X_in[f] = 0
# Ensure correct order
X_in = X_in[features]

st.markdown('<div class="racing-stripe"></div>', unsafe_allow_html=True)

# -------------------------
# Prediction section
# -------------------------
st.markdown("### 🎯 RACE PREDICTION")

# Center the prediction area
_, col_pred_main, _ = st.columns([1, 2, 1])

with col_pred_main:
    if st.button("🏁 CALCULATE TOP-10 PROBABILITY 🏁"):
        with st.spinner("Crunching the telemetry data..."):
            try:
                # Assuming class 1 is Top-10
                proba = model.predict_proba(X_in)[:, 1][0]
            except Exception as e:
                st.error("⚠️ Prediction Engine Failure: " + str(e))
                st.stop()

        # Visual Result Display
        st.markdown('<div style="text-align: center; margin-bottom: 20px;">', unsafe_allow_html=True)
        st.metric("PROBABILITY OF POINTS FINISH", f"{proba:.1%}", delta=None)
        st.markdown('</div>', unsafe_allow_html=True)

        if proba >= 0.7:
            st.success("🟢 **PODIUM CONTENTION LIKELY** - Excellent chance of heavy points.")
        elif proba >= 0.4:
            st.info("🟡 **MIDFIELD BATTLE** - Good chance of scraping into the top 10.")
        else:
            st.warning("🔴 **BACKMARKER CHALLENGE** - Needs chaos ahead to score points.")

        # Simple progress bar visualization
        st.progress(proba, text=f"Confidence Level: {proba:.2f}")


# -------------------------
# Diagnostics section
# -------------------------
st.markdown("---")
with st.expander("🔍 VIEW TELEMETRY INPUTS (DEBUG)"):
    # Transpose for better readability
    st.dataframe(X_in.T.style.format("{:.2f}"), use_container_width=True)

if SAMPLE_IMG.exists():
    st.markdown("### 📈 MODEL BENCHMARKS")
    # FIX: use_container_width instead of use_column_width
    st.image(str(SAMPLE_IMG), use_container_width=True, caption="Historical Model Performance on Test Set")