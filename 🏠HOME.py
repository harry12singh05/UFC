import streamlit as st
import pandas as pd


st.set_page_config(page_title="UFC HOME DASHBOARD", page_icon="🥊", layout="wide")

st.logo("harry.png",size="large",icon_image="harry.png")


def load_css():
    st.markdown("""
    <style>

    /* ---------- General ---------- */
    .block-container{
        padding-top:1.5rem;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"]{
        background-color:#0d0d0d;
    }

    section[data-testid="stSidebar"] *{
        color:#f2f2f2 !important;
    }
    [data-testid="stSidebar"] [data-testid="stLogo"]{
        display:block;
        margin:20px auto 10px auto;
    }
    [data-testid="stSidebar"] [data-testid="stLogo"] img{
        height:auto !important;
        max-height:90px !important;
        width:auto !important;
        max-width:88% !important;
    }
   

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a{
        border-radius:8px;
        padding:8px 12px;
        margin:2px 8px;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover{
        background-color:rgba(225,6,0,.15);
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"]{
        background-color:#E10600 !important;
        color:white !important;
        font-weight:600;
    }

    /* ---------- Hero banner ---------- */
    .hero{
        background:linear-gradient(rgba(0,0,0,.75),rgba(0,0,0,.75)),
        url('https://images.unsplash.com/photo-1547347298-4074fc3086f0?auto=format&fit=crop&w=1800&q=80');
        background-size:cover;
        background-position:center;
        padding:40px 35px;
        border-radius:18px;
        color:white;
        border-left:7px solid #E10600;
        margin-bottom:25px;
        box-shadow:0 20px 50px rgba(225,6,0,.18);
    }

    .hero h1{
        font-size:42px;
        margin-bottom:8px;
        font-weight:800;
    }

    .hero p{
        font-size:17px;
        color:#dddddd;
        line-height:1.6;
        margin:0;
    }

    /* ---------- Welcome text ---------- */
    .welcome-title{
        font-size:22px;
        font-weight:700;
        margin-bottom:6px;
    }

    .welcome-text{
        color:#555555;
        font-size:15px;
        margin-bottom:25px;
        max-width:900px;
    }

    /* ---------- Metric cards ---------- */
    .metric-card{
        background:white;
        border-radius:15px;
        padding:18px 20px;
        border:1px solid #eeeeee;
        box-shadow:0 5px 15px rgba(0,0,0,.08);
        transition:.25s;
        display:flex;
        align-items:center;
        gap:14px;
        height:100%;
    }

    .metric-card:hover{
        transform:translateY(-5px);
        border:1px solid #E10600;
        box-shadow:0 10px 25px rgba(225,6,0,.25);
    }

    .metric-icon{
        min-width:48px;
        height:48px;
        border-radius:50%;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:22px;
        color:white;
    }

    .icon-red{ background:#E10600; }
    .icon-blue{ background:#1e6fe0; }
    .icon-green{ background:#1fa64a; }
    .icon-purple{ background:#8a3ffc; }

    .metric-value{
        font-size:24px;
        font-weight:800;
        color:#111111;
        line-height:1.1;
    }

    .metric-label{
        font-size:13px;
        color:#777777;
        font-weight:500;
    }

    /* ---------- Info / How it works box ---------- */
    .info-box{
        background:#fff5f5;
        padding:24px 28px;
        border-radius:15px;
        border-left:6px solid #E10600;
        margin-top:28px;
        display:flex;
        align-items:center;
        justify-content:space-between;
        gap:20px;
    }

    .info-box h3{
        color:#E10600;
        margin-bottom:6px;
        font-size:20px;
    }

    .info-box p{
        color:#444444;
        font-size:15px;
        margin:0;
        max-width:750px;
    }

    .info-box .info-icon{
        font-size:46px;
        opacity:.85;
    }

    
    /* ============ PREMIUM BACKGROUND UPGRADE ============ */
    [data-testid="stAppViewContainer"]{
        background:
            radial-gradient(circle at 6% 8%, rgba(225,6,0,0.07), transparent 28%),
            radial-gradient(circle at 96% 4%, rgba(30,111,224,0.06), transparent 30%),
            radial-gradient(circle at 90% 92%, rgba(225,6,0,0.05), transparent 32%),
            radial-gradient(circle at 4% 96%, rgba(138,63,252,0.05), transparent 30%),
            linear-gradient(180deg, #fbfbfc 0%, #f3f4f6 100%) !important;
        background-attachment: fixed;
    }

    [data-testid="stAppViewContainer"] > .main::before{
        content:"";
        position:fixed;
        inset:0;
        background-image: radial-gradient(rgba(0,0,0,0.035) 1px, transparent 1px);
        background-size: 24px 24px;
        pointer-events:none;
        z-index:0;
    }

    [data-testid="stAppViewContainer"] .block-container{
        position:relative;
        z-index:1;
    }

    section[data-testid="stSidebar"]{
        background: radial-gradient(circle at 50% -10%, #2a0000 0%, #0d0d0d 55%) !important;
        box-shadow: 4px 0 24px rgba(0,0,0,.35);
    }

    div[data-testid="stVerticalBlockBorderWrapper"]{
        background: rgba(255,255,255,0.82) !important;
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
    }

    .metric-card{
        background: rgba(255,255,255,0.88) !important;
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
    }

    </style>
    """, unsafe_allow_html=True)


load_css()

df = pd.read_csv("train_data_cleaned.csv")
df.rename(columns={'R_fighter': 'Red Fighter', 'B_fighter': 'Blue Fighter'}, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df["year"] = df['date'].dt.year

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <h1>🥊 UFC FIGHT OUTCOME ANALYSIS</h1>
    <p>
    Analyze fighters. Compare statistics. Predict the winner.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- Welcome ----------
st.markdown("""
<div class="welcome-title">Welcome to the UFC Fight Outcome Prediction Dashboard!</div>
<div class="welcome-text">
This app analyzes historical UFC fight data and helps you compare two fighters and predict the most
likely winner using a rule-based scoring system.
</div>
""", unsafe_allow_html=True)

# ---------- Metric cards ----------
total_fighters = len(set(df['Red Fighter'].unique()) | set(df['Blue Fighter'].unique()))

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon icon-red">🥊</div>
        <div>
            <div class="metric-value">{df.shape[0]:,}</div>
            <div class="metric-label">Total Fights</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon icon-blue">🧑</div>
        <div>
            <div class="metric-value">{total_fighters:,}</div>
            <div class="metric-label">Total Fighters</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon icon-green">📊</div>
        <div>
            <div class="metric-value">{df.shape[1]}</div>
            <div class="metric-label">Total Features</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon icon-purple">📅</div>
        <div>
            <div class="metric-value">{df['year'].min()}-{df['year'].max()}</div>
            <div class="metric-label">Date Range</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- How it works ----------
st.markdown("""
<div class="info-box">
    <div>
        <h3>How it works?</h3>
        <p>Explore the dataset, analyze visualizations, compare fighters and predict the winner
        based on key statistics.</p>
    </div>
    <div class="info-icon">🥊</div>
</div>
""", unsafe_allow_html=True)
