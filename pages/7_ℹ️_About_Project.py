import streamlit as st
import pandas as pd


st.logo("harry.png",size="large",icon_image="harry.png")

def load_css():
    st.markdown("""
    <style>
    .block-container{ padding-top:1.5rem; padding-bottom:2rem; }

    section[data-testid="stSidebar"]{ background-color:#0d0d0d; }
    section[data-testid="stSidebar"] *{ color:#f2f2f2 !important; }
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
        border-radius:8px; padding:8px 12px; margin:2px 8px;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover{
        background-color:rgba(225,6,0,.15);
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"]{
        background-color:#E10600 !important; color:white !important; font-weight:600;
    }

    .page-header{ display:flex; align-items:center; gap:12px; margin-bottom:22px; }
    .page-header .bar{ width:6px; height:36px; background:#E10600; border-radius:3px; box-shadow:0 0 12px rgba(225,6,0,.55); }
    .page-header h1{ font-size:28px; font-weight:800; margin:0; color:#111; }
    .page-header p{ margin:2px 0 0 0; color:#808080; font-size:14px; }

    div[data-testid="stVerticalBlockBorderWrapper"]{
        border-radius:16px !important;
        border:1px solid #eeeeee !important;
        box-shadow:0 5px 15px rgba(0,0,0,.06);
    }

    .card-title{
        font-size:16px; font-weight:800; color:#111;
        margin:2px 0 12px 0; display:flex; align-items:center; gap:8px;
    }
    .card-title .dot{ width:8px; height:8px; border-radius:50%; background:#E10600; }

    .card-text{
        color:#555; font-size:14px; line-height:1.7;
    }

    .fighter-photo{
        margin-top:16px;
        border-radius:12px;
        width:100%;
        height:130px;
        object-fit:cover;
    }

    .center-icon{
        font-size:44px;
        text-align:center;
        margin-top:18px;
        opacity:.9;
    }

    .checklist-item{
        display:flex; align-items:flex-start; gap:10px;
        margin-bottom:10px; font-size:14px; color:#333;
    }
    .checklist-item .check{
        color:#1fa64a; font-weight:800; margin-top:1px;
    }

    .tech-item{
        display:flex; align-items:center; gap:12px;
        margin-bottom:14px; font-size:14.5px; color:#222; font-weight:600;
    }
    .tech-icon{
        min-width:34px; height:34px; border-radius:9px;
        background:#fff5f5; display:flex; align-items:center; justify-content:center;
        font-size:17px;
    }

    .data-item{
        display:flex; justify-content:space-between; align-items:center;
        padding:9px 0; border-bottom:1px solid #f2f2f2; font-size:14px;
    }
    .data-item:last-child{ border-bottom:none; }
    .data-item .label{ color:#777; }
    .data-item .value{ color:#111; font-weight:700; }

    .workflow-row{
        display:flex; align-items:center; justify-content:space-between;
        flex-wrap:wrap; gap:6px; padding:10px 0 4px 0;
    }
    .workflow-step{
        display:flex; flex-direction:column; align-items:center;
        gap:8px; min-width:110px;
    }
    .workflow-circle{
        width:56px; height:56px; border-radius:50%;
        background:#fff5f5; border:2px solid #E10600;
        display:flex; align-items:center; justify-content:center;
        font-size:24px;
    }
    .workflow-label{
        text-align:center; font-size:12.5px; font-weight:700; color:#333;
        line-height:1.3;
    }
    .workflow-arrow{
        font-size:22px; color:#E10600; font-weight:800;
        margin:0 2px 30px 2px;
    }

    .about-footer{
        text-align:center; color:#999; font-size:13px;
        margin-top:30px; padding-top:16px; border-top:1px solid #eeeeee;
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


def page_header(icon, title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <div class="bar"></div>
        <div>
            <h1>{icon} {title}</h1>
            <p>{subtitle}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def card_title(text):
    st.markdown(f'<div class="card-title"><span class="dot"></span>{text}</div>', unsafe_allow_html=True)


df = pd.read_csv("train_data_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])

total_fights = len(df)
total_fighters = len(set(df["R_fighter"].unique()) | set(df["B_fighter"].unique()))
total_features = df.shape[1]
date_range = f"{df['date'].dt.year.min()} - {df['date'].dt.year.max()}"

page_header("ℹ️", "About / Project Information", "What this dashboard does and how it was built")

# ---------- Row 1: Scenario / Problem / Objectives ----------
r1c1, r1c2, r1c3 = st.columns(3)

with r1c1:
    with st.container(border=True):
        card_title("Project Scenario")
        st.markdown("""
        <div class="card-text">
        In UFC, every fight has two competitors: Red Corner vs Blue Corner. Before the fight, fans and
        analysts want to know who has a higher chance of winning.<br><br>
        This project analyzes historical UFC fight data and compares two fighters using important
        statistics to predict the most likely winner using a rule-based scoring system.
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            '<img class="fighter-photo" '
            'src="https://images.unsplash.com/photo-1517438322307-e67111335449?auto=format&fit=crop&w=800&q=80">',
            unsafe_allow_html=True
        )

with r1c2:
    with st.container(border=True):
        card_title("Problem Statement")
        st.markdown("""
        <div class="card-text">
        Fight predictions are often based on opinions, popularity, or emotions.<br><br>
        There is a need for a data-driven system that can analyze fighters objectively and provide
        transparent predictions.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="center-icon">🎯</div>', unsafe_allow_html=True)

with r1c3:
    with st.container(border=True):
        card_title("Objectives")
        objectives = [
            "Clean and prepare UFC historical data",
            "Perform Exploratory Data Analysis",
            "Visualize important patterns and insights",
            "Compare two fighters side by side",
            "Predict the winner using a rule-based system",
            "Explain the reason behind the prediction",
        ]
        for obj in objectives:
            st.markdown(f'<div class="checklist-item"><span class="check">✔</span><span>{obj}</span></div>',
                        unsafe_allow_html=True)

st.write("")

# ---------- Row 2: Technologies / Dataset Info ----------
r2c1, r2c2 = st.columns(2)

with r2c1:
    with st.container(border=True):
        card_title("Technologies Used")
        technologies = [
            ("🐍", "Python"),
            ("🐼", "Pandas"),
            ("🔢", "NumPy"),
            ("📊", "Plotly"),
            
            ("🔴", "Streamlit"),
        ]
        t1, t2 = st.columns(2)
        for i, (icon, name) in enumerate(technologies):
            target = t1 if i % 2 == 0 else t2
            with target:
                st.markdown(f"""
                <div class="tech-item">
                    <div class="tech-icon">{icon}</div>
                    <div>{name}</div>
                </div>
                """, unsafe_allow_html=True)

with r2c2:
    with st.container(border=True):
        card_title("Dataset Information")
        data_items = [
            ("Source", "UFC Stats Dataset"),
            ("Total Fights", f"{total_fights:,}"),
            ("Total Fighters", f"{total_fighters:,}"),
            ("Total Features", f"{total_features}"),
            ("Date Range", date_range),
        ]
        for label, value in data_items:
            st.markdown(f"""
            <div class="data-item">
                <span class="label">{label}</span>
                <span class="value">{value}</span>
            </div>
            """, unsafe_allow_html=True)

st.write("")

# ---------- Row 3: Project Workflow ----------
with st.container(border=True):
    card_title("Project Workflow")
    steps = [
        ("🗄️", "Raw Data"),
        ("🧹", "Data Cleaning"),
        ("📈", "Exploratory Data Analysis"),
        ("⚖️", "Compare Fighters"),
        ("🏆", "Predict Winner"),
        ("✅", "Result & Explanation"),
    ]

    step_html = '<div class="workflow-row">'
    for i, (icon, label) in enumerate(steps):
        step_html += f"""
        <div class="workflow-step">
            <div class="workflow-circle">{icon}</div>
            <div class="workflow-label">{label}</div>
        </div>
        """
        if i < len(steps) - 1:
            step_html += '<div class="workflow-arrow">→</div>'
    step_html += "</div>"

    st.markdown(step_html, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
<div class="about-footer">
© 2026 UFC Fight Outcome Prediction Dashboard &nbsp;|&nbsp; Built with Streamlit ❤️
</div>
""", unsafe_allow_html=True)