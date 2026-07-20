import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="UFC Fight Outcome Prediction", page_icon="🥊", layout="wide")

st.logo("harry.png", size="large", icon_image="harry.png")

RED = "#E10600"
BLUE = "#1e6fe0"

PAGES = [
    "🏠 Home",
    "📊 Dataset Overview",
    "🔍 Exploratory Data Analysis",
    "🥊 Red vs Blue Comparison",
    "🔎 Fighter Search",
    "🏆 Winner Prediction",
    "ℹ️ About Project",
]


# =========================================================================
# CSS
# =========================================================================
def load_css():
    st.markdown("""
    <style>

    /* ---------- General ---------- */
    .block-container{ padding-top:1.5rem; }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"]{ background-color:#0d0d0d; }
    section[data-testid="stSidebar"] *{ color:#f2f2f2 !important; }

    [data-testid="stSidebar"] [data-testid="stLogo"]{
        display:block;
        margin:20px auto 18px auto;
    }
    [data-testid="stSidebar"] [data-testid="stLogo"] img{
        height:auto !important;
        max-height:90px !important;
        width:auto !important;
        max-width:88% !important;
    }

    /* ---------- Custom nav (radio styled as pill menu) ---------- */
    div[data-testid="stRadio"] > div[role="radiogroup"]{
        display:flex;
        flex-direction:column;
        gap:6px;
    }
    div[data-testid="stRadio"] label{
        background:transparent;
        border-radius:10px;
        padding:12px 16px;
        margin:0 4px;
        cursor:pointer;
        transition:.2s;
        font-weight:600;
        font-size:15px;
        display:flex;
        align-items:center;
        gap:10px;
    }
    div[data-testid="stRadio"] label:hover{
        background:rgba(225,6,0,.18);
    }
    div[data-testid="stRadio"] label:has(input:checked){
        background:#E10600;
        box-shadow:0 4px 14px rgba(225,6,0,.4);
        color:white !important;
    }
    div[data-testid="stRadio"] [data-baseweb="radio"] > div:first-child{
        display:none;
    }

    /* ---------- Hero banner (Home) ---------- */
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
    .hero h1{ font-size:42px; margin-bottom:8px; font-weight:800; }
    .hero p{ font-size:17px; color:#dddddd; line-height:1.6; margin:0; }

    /* ---------- Welcome text (Home) ---------- */
    .welcome-title{ font-size:22px; font-weight:700; margin-bottom:6px; }
    .welcome-text{ color:#555555; font-size:15px; margin-bottom:25px; max-width:900px; }

    /* ---------- Page header (all other pages) ---------- */
    .page-header{ display:flex; align-items:center; gap:12px; margin-bottom:22px; }
    .page-header .bar{
        width:6px; height:36px; background:#E10600; border-radius:3px;
        box-shadow:0 0 12px rgba(225,6,0,.55);
    }
    .page-header h1{ font-size:28px; font-weight:800; margin:0; color:#111; }
    .page-header p{ margin:2px 0 0 0; color:#808080; font-size:14px; }

    /* ---------- Bordered containers / cards ---------- */
    div[data-testid="stVerticalBlockBorderWrapper"]{
        border-radius:16px !important;
        border:1px solid #eeeeee !important;
        box-shadow:0 5px 15px rgba(0,0,0,.06);
        background: rgba(255,255,255,0.82) !important;
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
    }

    /* ---------- Metric cards ---------- */
    .metric-card{
        background: rgba(255,255,255,0.88);
        border-radius:15px;
        padding:18px 20px;
        border:1px solid #eeeeee;
        box-shadow:0 5px 15px rgba(0,0,0,.08);
        transition:.25s;
        display:flex;
        align-items:center;
        gap:14px;
        height:100%;
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
    }
    .metric-card:hover{
        transform:translateY(-5px);
        border:1px solid #E10600;
        box-shadow:0 10px 25px rgba(225,6,0,.25);
    }
    .metric-icon{
        min-width:48px; height:48px; border-radius:50%;
        display:flex; align-items:center; justify-content:center;
        font-size:22px; color:white;
    }
    .icon-red{ background:#E10600; }
    .icon-blue{ background:#1e6fe0; }
    .icon-green{ background:#1fa64a; }
    .icon-purple{ background:#8a3ffc; }

    .metric-value{ font-size:24px; font-weight:800; color:#111111; line-height:1.1; }
    .metric-label{ font-size:13px; color:#777777; font-weight:500; }

    /* ---------- Info / How it works box (Home) ---------- */
    .info-box{
        background:#fff5f5; padding:24px 28px; border-radius:15px;
        border-left:6px solid #E10600; margin-top:28px;
        display:flex; align-items:center; justify-content:space-between; gap:20px;
    }
    .info-box h3{ color:#E10600; margin-bottom:6px; font-size:20px; }
    .info-box p{ color:#444444; font-size:15px; margin:0; max-width:750px; }
    .info-box .info-icon{ font-size:46px; opacity:.85; }

    /* ---------- Section titles ---------- */
    .section-title{
        font-size:16px; font-weight:700; color:#111;
        margin:2px 0 12px 2px; display:flex; align-items:center; gap:8px;
    }
    .section-title .dot{ width:8px; height:8px; border-radius:50%; background:#E10600; }

    .success-box{
        background:#f2fbf4; border-left:6px solid #1fa64a; padding:16px 20px;
        border-radius:12px; color:#1a7a37; font-weight:600; text-align:center;
    }

    /* ---------- Fighter Search ---------- */
    div[data-testid="stMetric"]{
        background:#fafafa; border-radius:12px; padding:10px 14px; border:1px solid #f0f0f0;
    }
    div[data-testid="stMetricValue"]{ color:#111; font-weight:800; }
    div[data-testid="stMetricLabel"]{ color:#777; font-weight:600; }

    .avatar-circle{
        width:130px; height:130px; border-radius:50%;
        background:linear-gradient(135deg,#E10600,#7a0000);
        display:flex; align-items:center; justify-content:center;
        color:white; font-size:52px; font-weight:800;
        margin:0 auto 14px auto;
        box-shadow:0 8px 20px rgba(225,6,0,.35);
    }
    .fighter-name{ text-align:center; font-size:22px; font-weight:800; color:#111; margin-bottom:4px; }
    .fighter-stance{ text-align:center; color:#888; font-size:13px; }

    /* ---------- Winner Prediction ---------- */
    .score-box{ text-align:center; padding:10px 6px; }
    .score-value-red{ font-size:46px; font-weight:800; color:#E10600; line-height:1; }
    .score-value-blue{ font-size:46px; font-weight:800; color:#1e6fe0; line-height:1; }
    .score-name{ color:#555; font-size:13px; font-weight:600; margin-top:6px; }

    .winner-badge{
        background:linear-gradient(135deg,#fff5f5,#ffe9e9);
        border:2px solid #E10600; border-radius:16px; padding:22px; text-align:center;
        height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;
    }
    .winner-badge .trophy{ font-size:36px; margin-bottom:6px; }
    .winner-badge h2{ color:#E10600; margin:0; font-size:24px; font-weight:800; }

    .reason-line{ padding:6px 0; color:#333; font-size:14.5px; }
    .reason-line b{ color:#111; }

    .note-box{
        background:#fff5f5; border-left:6px solid #E10600; border-radius:12px;
        padding:14px 18px; color:#7a1f1f; font-size:13.5px;
    }

    /* ---------- About Project ---------- */
    .card-title{
        font-size:16px; font-weight:800; color:#111;
        margin:2px 0 12px 0; display:flex; align-items:center; gap:8px;
    }
    .card-title .dot{ width:8px; height:8px; border-radius:50%; background:#E10600; }
    .card-text{ color:#555; font-size:14px; line-height:1.7; }
    .fighter-photo{ margin-top:16px; border-radius:12px; width:100%; height:130px; object-fit:cover; }
    .center-icon{ font-size:44px; text-align:center; margin-top:18px; opacity:.9; }
    .checklist-item{ display:flex; align-items:flex-start; gap:10px; margin-bottom:10px; font-size:14px; color:#333; }
    .checklist-item .check{ color:#1fa64a; font-weight:800; margin-top:1px; }
    .tech-item{ display:flex; align-items:center; gap:12px; margin-bottom:14px; font-size:14.5px; color:#222; font-weight:600; }
    .tech-icon{
        min-width:34px; height:34px; border-radius:9px;
        background:#fff5f5; display:flex; align-items:center; justify-content:center; font-size:17px;
    }
    .data-item{ display:flex; justify-content:space-between; align-items:center; padding:9px 0; border-bottom:1px solid #f2f2f2; font-size:14px; }
    .data-item:last-child{ border-bottom:none; }
    .data-item .label{ color:#777; }
    .data-item .value{ color:#111; font-weight:700; }

    .workflow-row{ display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:6px; padding:10px 0 4px 0; }
    .workflow-step{ display:flex; flex-direction:column; align-items:center; gap:8px; min-width:110px; }
    .workflow-circle{
        width:56px; height:56px; border-radius:50%; background:#fff5f5; border:2px solid #E10600;
        display:flex; align-items:center; justify-content:center; font-size:24px;
    }
    .workflow-label{ text-align:center; font-size:12.5px; font-weight:700; color:#333; line-height:1.3; }
    .workflow-arrow{ font-size:22px; color:#E10600; font-weight:800; margin:0 2px 30px 2px; }

    .about-footer{
        text-align:center; color:#999; font-size:13px; margin-top:30px; padding-top:16px; border-top:1px solid #eeeeee;
    }

    /* ============ PREMIUM BACKGROUND ============ */
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
    [data-testid="stAppViewContainer"] .block-container{ position:relative; z-index:1; }
    section[data-testid="stSidebar"]{
        background: radial-gradient(circle at 50% -10%, #2a0000 0%, #0d0d0d 55%) !important;
        box-shadow: 4px 0 24px rgba(0,0,0,.35);
    }

    </style>
    """, unsafe_allow_html=True)


load_css()


# =========================================================================
# Cached data — loaded once, reused across every navigation click
# =========================================================================
@st.cache_data
def load_data():
    df = pd.read_csv("train_data_cleaned.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    return df


df = load_data()


# =========================================================================
# Shared helper components
# =========================================================================
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


def metric_card(icon, icon_class, value, label):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon {icon_class}">{icon}</div>
        <div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def section_title(text):
    st.markdown(f'<div class="section-title"><span class="dot"></span>{text}</div>', unsafe_allow_html=True)


def style_fig(fig, height=320):
    fig.update_layout(
        height=height,
        paper_bgcolor="white",
        plot_bgcolor="#fafafa",
        margin=dict(t=50, b=10, l=10, r=10),
        title_font=dict(size=15)
    )
    return fig


# =========================================================================
# PAGE: Home
# =========================================================================
def render_home(df):
    named = df.rename(columns={'R_fighter': 'Red Fighter', 'B_fighter': 'Blue Fighter'})
    total_fighters = len(set(named['Red Fighter'].unique()) | set(named['Blue Fighter'].unique()))

    st.markdown("""
    <div class="hero">
        <h1>🥊 UFC FIGHT OUTCOME PREDICTION</h1>
        <p>Analyze fighters. Compare statistics. Predict the winner.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-title">Welcome to the UFC Fight Outcome Prediction Dashboard!</div>
    <div class="welcome-text">
    This app analyzes historical UFC fight data and helps you compare two fighters and predict the most
    likely winner using a rule-based scoring system.
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("🥊", "icon-red", f"{named.shape[0]:,}", "Total Fights")
    with c2:
        metric_card("🧑", "icon-blue", f"{total_fighters:,}", "Total Fighters")
    with c3:
        metric_card("📊", "icon-green", f"{named.shape[1]}", "Total Features")
    with c4:
        metric_card("📅", "icon-purple", f"{named['year'].min()}-{named['year'].max()}", "Date Range")

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


# =========================================================================
# PAGE: Dataset Overview
# =========================================================================
def render_dataset_overview(df):
    named = df.rename(columns={"R_fighter": "Red Fighter", "B_fighter": "Blue Fighter"})

    page_header("📊", "Dataset Overview", "Structure, quality and statistics of the UFC fight dataset")

    rows = len(named)
    columns = len(named.columns)
    missing_values = named.isnull().sum().sum()
    duplicate = named.duplicated().sum()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("📄", "icon-red", f"{rows:,}", "Rows")
    with c2:
        metric_card("📶", "icon-blue", f"{columns}", "Columns")
    with c3:
        metric_card("⚠️", "icon-green", f"{missing_values}", "Missing Values")
    with c4:
        metric_card("🧬", "icon-purple", f"{duplicate}", "Duplicate Rows")

    st.write("")

    dtype_counts = named.dtypes.astype(str).value_counts()
    fig = px.pie(
        values=dtype_counts.values,
        names=dtype_counts.index,
        title="Column Data Types",
        hole=0.5,
        color_discrete_sequence=[RED, BLUE, "#1fa64a"]
    )
    fig.update_layout(height=330, paper_bgcolor="white", margin=dict(t=50, b=10, l=10, r=10))

    left, right = st.columns(2)
    with left:
        with st.container(border=True):
            st.plotly_chart(fig, use_container_width=True)

    with right:
        with st.container(border=True):
            section_title("Missing Values by Column")
            missing_col = named.isnull().sum()
            missing_col = missing_col[missing_col > 0]
            if len(missing_col) == 0:
                st.markdown('<div class="success-box">✅ No missing values found in the dataset.</div>',
                            unsafe_allow_html=True)
            else:
                st.dataframe(missing_col, use_container_width=True)

    st.write("")
    with st.container(border=True):
        section_title("Dataset Sample (First 5 Rows)")
        st.dataframe(named.head(), use_container_width=True)

    st.write("")
    with st.container(border=True):
        section_title("Statistical Summary")
        st.dataframe(named.describe(), use_container_width=True)


# =========================================================================
# PAGE: Exploratory Data Analysis
# =========================================================================
def render_eda(df):
    working = df.copy()
    page_header("📊", "Exploratory Data Analysis", "Distributions, trends and patterns across the UFC dataset")

    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            fig1 = px.histogram(working, x="Red Age", title="🔴 Red Fighter Age Distribution",
                                 color_discrete_sequence=[RED])
            st.plotly_chart(style_fig(fig1), use_container_width=True)
    with c2:
        with st.container(border=True):
            fig2 = px.histogram(working, x="Blue Age", title="🔵 Blue Fighter Age Distribution",
                                 color_discrete_sequence=[BLUE])
            st.plotly_chart(style_fig(fig2), use_container_width=True)

    with c1:
        with st.container(border=True):
            fig3 = px.histogram(working, x="Red Height", title="🔴 Red Fighter Height Distribution",
                                 color_discrete_sequence=[RED], nbins=30)
            st.plotly_chart(style_fig(fig3), use_container_width=True)
    with c2:
        with st.container(border=True):
            fig4 = px.histogram(working, x="Blue Height", title="🔵 Blue Fighter Height Distribution",
                                 color_discrete_sequence=[BLUE], nbins=30)
            st.plotly_chart(style_fig(fig4), use_container_width=True)

    weight_df = working[(working["Red Weight"] <= 300) & (working["Blue Weight"] <= 300)]
    with c1:
        with st.container(border=True):
            fig5 = px.histogram(weight_df, x=weight_df["Red Weight"], nbins=25,
                                 title="🔴 Red Fighter Weight Distribution", color_discrete_sequence=[RED])
            st.plotly_chart(style_fig(fig5), use_container_width=True)
    with c2:
        with st.container(border=True):
            fig6 = px.histogram(weight_df, x=weight_df["Blue Weight"], nbins=25,
                                 title="🔵 Blue Fighter Weight Distribution", color_discrete_sequence=[BLUE])
            st.plotly_chart(style_fig(fig6), use_container_width=True)

    with c1:
        with st.container(border=True):
            fig7 = px.histogram(working, x="Red Reach", title="🔴 Red Fighter Reach Distribution",
                                 nbins=25, color_discrete_sequence=[RED])
            st.plotly_chart(style_fig(fig7), use_container_width=True)
    with c2:
        with st.container(border=True):
            fig8 = px.histogram(working, x="Blue Reach", nbins=25, title="🔵 Blue Fighter Reach Distribution",
                                 color_discrete_sequence=[BLUE])
            st.plotly_chart(style_fig(fig8), use_container_width=True)

    working = working[working["Win By"] != "Decision_Split"]
    win_method = working["Win By"].value_counts()
    with c1:
        with st.container(border=True):
            fig9 = px.pie(values=win_method.values, names=win_method.index, hole=0.5,
                           title="Win Method Distribution",
                           color_discrete_sequence=[RED, "#ff8c00", BLUE, "#1fa64a", "#8a3ffc"])
            st.plotly_chart(style_fig(fig9), use_container_width=True)

    fight = working["Fight Type"].value_counts().head(10)
    with c2:
        with st.container(border=True):
            fig10 = px.bar(x=fight.values, y=fight.index, orientation="h", color=fight.values,
                            color_continuous_scale="Reds", title="Top 10 Fight Types")
            fig10.update_layout(yaxis=dict(autorange="reversed"), coloraxis_showscale=False)
            st.plotly_chart(style_fig(fig10), use_container_width=True)

    working["Year"] = working["date"].dt.year
    yearly = working.groupby("Year").size().reset_index(name="Total Fights")
    with c1:
        with st.container(border=True):
            fig11 = px.line(yearly, x="Year", y="Total Fights", markers=True,
                             title="UFC Fights per Year", color_discrete_sequence=[RED])
            st.plotly_chart(style_fig(fig11), use_container_width=True)

    wins = working["Winner"].value_counts().head(10)
    with c2:
        with st.container(border=True):
            fig12 = px.bar(x=wins.values, y=wins.index, color_continuous_scale="Reds",
                            title="Top 10 Winners", color=wins.values)
            fig12.update_layout(yaxis=dict(autorange="reversed"), coloraxis_showscale=False)
            st.plotly_chart(style_fig(fig12), use_container_width=True)


# =========================================================================
# PAGE: Red vs Blue Comparison
# =========================================================================
def render_comparison(df):
    working = df.copy()
    page_header("🔴🔵", "Red vs Blue Fighter Comparison", "How the two corners stack up, on average, across the dataset")

    red_age = working["Red Age"].mean()
    blue_age = working["Blue Age"].mean()
    red_reach = working["Red Reach"].mean()
    blue_reach = working["Blue Reach"].mean()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("🔴", "icon-red", f"{red_age:.2f}", "Avg Age")
    with c2:
        metric_card("🔵", "icon-blue", f"{blue_age:.2f}", "Avg Age")
    with c3:
        metric_card("🔴", "icon-red", f"{red_reach:.2f}", "Avg Reach")
    with c4:
        metric_card("🔵", "icon-blue", f"{blue_reach:.2f}", "Avg Reach")

    st.write("")

    weight_df = working[(working["Red Weight"] <= 300) & (working["Blue Weight"] <= 300)]
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=["Age", "Height", "Weight", "Reach"],
                y=[working["Red Age"].mean(), working["Red Height"].mean(),
                   weight_df["Red Weight"].mean(), working["Red Reach"].mean()],
                name="Red", marker_color=RED
            ))
            fig.add_trace(go.Bar(
                x=["Age", "Height", "Weight", "Reach"],
                y=[working["Blue Age"].mean(), working["Blue Height"].mean(),
                   weight_df["Blue Weight"].mean(), working["Blue Reach"].mean()],
                name="Blue", marker_color=BLUE
            ))
            fig.update_layout(title="Average Physical Attributes", barmode="group")
            st.plotly_chart(style_fig(fig, height=380), use_container_width=True)

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=["KD", "SIG STR %", "TD %", "SUB ATT"],
        y=[working["R_KD"].mean(), working["R_SIG_STR_pct"].mean(),
           working["R_TD_pct"].mean(), working["R_SUB_ATT"].mean()],
        name="Red", marker_color=RED
    ))
    fig2.add_trace(go.Bar(
        x=["KD", "SIG STR %", "TD %", "SUB ATT"],
        y=[working["B_KD"].mean(), working["B_SIG_STR_pct"].mean(),
           working["B_TD_pct"].mean(), working["B_SUB_ATT"].mean()],
        name="Blue", marker_color=BLUE
    ))
    fig2.update_layout(title="Average Fighter Skills", barmode="group")
    with col2:
        with st.container(border=True):
            st.plotly_chart(style_fig(fig2, height=380), use_container_width=True)

    age = pd.DataFrame({
        "Age": pd.concat([working["Red Age"], working["Blue Age"]]),
        "Corner": ["Red"] * len(working) + ["Blue"] * len(working)
    })
    fig3 = px.box(age, x="Corner", y="Age", color="Corner", color_discrete_map={"Red": RED, "Blue": BLUE})
    fig3.update_layout(title="Age Comparison")
    with col1:
        with st.container(border=True):
            st.plotly_chart(style_fig(fig3, height=380), use_container_width=True)

    fig4 = px.scatter(working, x="Red Reach", y="Blue Reach", color="Winner",
                       title="Red Reach vs Blue Reach", opacity=0.7)
    fig4.update_traces(marker=dict(size=8))
    with col2:
        with st.container(border=True):
            st.plotly_chart(style_fig(fig4, height=380), use_container_width=True)

    cols = ["Red Age", "Blue Age", "Red Height", "Blue Height",
            "Red Weight", "Blue Weight", "Red Reach", "Blue Reach"]
    corr = working[cols].corr()
    fig5 = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r",
                      title="Correlation Between Red and Blue Fighter Attributes")
    with st.container(border=True):
        st.plotly_chart(style_fig(fig5, height=460), use_container_width=True)


# =========================================================================
# PAGE: Fighter Search
# =========================================================================
def render_fighter_search(df):
    working = df.copy()
    page_header("🔍", "Fighter Search", "Look up any fighter's career profile and recent form")

    all_fighters = pd.concat([working["R_fighter"], working["B_fighter"]]).unique()
    all_fighters = sorted(all_fighters)

    selected_fighter = st.selectbox("Select Fighter", all_fighters, key="fighter_search_select")

    red_fights = working[working["R_fighter"] == selected_fighter].copy()
    red_fights["corner"] = "R"
    blue_fights = working[working["B_fighter"] == selected_fighter].copy()
    blue_fights["corner"] = "B"

    fights = pd.concat([red_fights, blue_fights]).sort_values("date")

    if fights.empty:
        st.warning("No data found for this fighter.")
        return

    total_fights = len(fights)
    wins = len(fights[fights["Winner"] == selected_fighter])
    losses = total_fights - wins
    win_percent = (wins / total_fights) * 100

    last_fight = fights.iloc[-1]
    if last_fight["corner"] == "R":
        age = last_fight["Red Age"]
        height = last_fight["Red Height"]
        weight = last_fight["Red Weight"]
        reach = last_fight["Red Reach"]
        stance = last_fight["Red Stance"]
        win_streak = last_fight["R_current_win_streak"]
        lose_streak = last_fight["R_current_lose_streak"]
    else:
        age = last_fight["Blue Age"]
        height = last_fight["Blue Height"]
        weight = last_fight["Blue Weight"]
        reach = last_fight["Blue Reach"]
        stance = last_fight["Blue Stance"]
        win_streak = last_fight["B_current_win_streak"]
        lose_streak = last_fight["B_current_lose_streak"]

    sig_str_list, opp_sig_str_list, kd_list = [], [], []
    td_acc_list, td_landed_list, sub_att_list, td_def_list = [], [], [], []

    for i, row in fights.iterrows():
        if row["corner"] == "R":
            sig_str_list.append(row["R_SIG_STR_pct"])
            opp_sig_str_list.append(row["B_SIG_STR_pct"])
            kd_list.append(row["R_KD"])
            td_acc_list.append(row["R_TD_pct"])
            td_landed_list.append(row["R_TD_landed"])
            sub_att_list.append(row["R_SUB_ATT"])
            opp_td_att = row["B_TD_att"]
            opp_td_landed = row["B_TD_landed"]
        else:
            sig_str_list.append(row["B_SIG_STR_pct"])
            opp_sig_str_list.append(row["R_SIG_STR_pct"])
            kd_list.append(row["B_KD"])
            td_acc_list.append(row["B_TD_pct"])
            td_landed_list.append(row["B_TD_landed"])
            sub_att_list.append(row["B_SUB_ATT"])
            opp_td_att = row["R_TD_att"]
            opp_td_landed = row["R_TD_landed"]

        if opp_td_att > 0:
            td_def_list.append(1 - (opp_td_landed / opp_td_att))

    sig_strike_acc = np.mean(sig_str_list) * 100
    opp_sig_strike_acc = np.mean(opp_sig_str_list) * 100
    str_acc_diff = sig_strike_acc - opp_sig_strike_acc
    kd_avg = np.mean(kd_list)
    td_accuracy = np.mean(td_acc_list) * 100
    sub_avg = np.mean(sub_att_list)
    td_defense = np.mean(td_def_list) * 100 if len(td_def_list) > 0 else 0

    win_fights = fights[fights["Winner"] == selected_fighter]
    finishes = len(win_fights[win_fights["Win By"].isin(["KO/TKO", "Submission"])])
    finish_rate = (finishes / wins) * 100 if wins > 0 else 0

    st.write("")
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 1.3, 1.3])

        with col1:
            initial = selected_fighter.strip()[0].upper() if selected_fighter.strip() else "?"
            st.markdown(f'<div class="avatar-circle">{initial}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="fighter-name">{selected_fighter}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="fighter-stance">Stance: {stance}</div>', unsafe_allow_html=True)

        with col2:
            section_title("Personal Information")
            c1, c2 = st.columns(2)
            c1.metric("Age", f"{age:.0f}")
            c1.metric("Weight (lbs)", f"{weight:.0f}")
            c2.metric("Height (cm)", f"{height:.1f}")
            c2.metric("Reach (cm)", f"{reach:.1f}")

        with col3:
            section_title("Career Statistics")
            c1, c2 = st.columns(2)
            c1.metric("Total Fights", total_fights)
            c1.metric("Wins", wins)
            c2.metric("Losses", losses)
            c2.metric("Win %", f"{win_percent:.1f}%")

    st.write("")
    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            section_title("Striking")
            st.metric("Sig. Strike Accuracy", f"{sig_strike_acc:.1f}%")
            st.metric("Knockdowns Avg", f"{kd_avg:.2f}")
            st.metric("Str. Acc. Differential", f"{str_acc_diff:.1f}%")

    with col5:
        with st.container(border=True):
            section_title("Grappling")
            st.metric("Takedown Accuracy", f"{td_accuracy:.1f}%")
            st.metric("Takedown Defense", f"{td_defense:.1f}%")
            st.metric("Submission Avg", f"{sub_avg:.2f}")

    with col6:
        with st.container(border=True):
            section_title("Performance")
            st.metric("Current Win Streak", int(win_streak))
            st.metric("Current Lose Streak", int(lose_streak))
            st.metric("Finish Rate", f"{finish_rate:.1f}%")

    st.write("")
    with st.container(border=True):
        section_title("Overall Profile")

        categories = ["Sig. Strike Acc.", "Takedown Acc.", "Takedown Def.", "Win %", "Finish Rate"]
        values = [sig_strike_acc, td_accuracy, td_defense, win_percent, finish_rate]
        categories.append(categories[0])
        values.append(values[0])

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values, theta=categories, fill="toself", name=selected_fighter,
            line_color="#E10600", fillcolor="rgba(225,6,0,0.25)"
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False, height=400, paper_bgcolor="white",
            margin=dict(t=10, b=10, l=10, r=10)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.write("")
    with st.container(border=True):
        section_title("Recent Fights")

        recent = fights.sort_values("date", ascending=False).head(5)
        table_rows = []
        for i, row in recent.iterrows():
            opponent = row["B_fighter"] if row["corner"] == "R" else row["R_fighter"]
            result = "Win" if row["Winner"] == selected_fighter else "Loss"
            table_rows.append({
                "Opponent": opponent,
                "Result": result,
                "Method": row["Win By"],
                "Round": row["last_round"],
                "Fight Type": row["Fight Type"],
                "Date": row["date"].strftime("%Y-%m-%d")
            })
        recent_table = pd.DataFrame(table_rows)
        st.dataframe(recent_table, use_container_width=True, hide_index=True)


# =========================================================================
# PAGE: Winner Prediction
# =========================================================================
def render_winner_prediction(df):
    working = df.copy()
    page_header("🏆", "Winner Prediction",
                "Rule-based prediction using each fighter's past fight statistics (no machine learning)")

    all_fighters = pd.concat([working["R_fighter"], working["B_fighter"]]).unique()
    all_fighters = sorted(all_fighters)

    with st.container(border=True):
        section_title("Select Fighters")
        col_a, col_b, col_c = st.columns([2, 2, 1])
        with col_a:
            red_name = st.selectbox("Red Corner Fighter", all_fighters, index=0, key="wp_red")
        with col_b:
            blue_name = st.selectbox("Blue Corner Fighter", all_fighters, index=1, key="wp_blue")
        with col_c:
            st.write("")
            st.write("")
            st.button("Predict Winner", type="primary", use_container_width=True, key="wp_predict")

    if red_name == blue_name:
        st.warning("Please select two different fighters.")
        return

    fighter_names = [red_name, blue_name]
    fighter_stats = []

    for name in fighter_names:
        red_fights = working[working["R_fighter"] == name].copy()
        red_fights["corner"] = "R"
        blue_fights = working[working["B_fighter"] == name].copy()
        blue_fights["corner"] = "B"
        fights = pd.concat([red_fights, blue_fights]).sort_values("date")

        total_fights = len(fights)
        wins = len(fights[fights["Winner"] == name])
        win_percent = (wins / total_fights) * 100 if total_fights > 0 else 0

        last_fight = fights.iloc[-1]
        if last_fight["corner"] == "R":
            age = last_fight["Red Age"]
            height = last_fight["Red Height"]
            weight = last_fight["Red Weight"]
            reach = last_fight["Red Reach"]
            win_streak = last_fight["R_current_win_streak"]
        else:
            age = last_fight["Blue Age"]
            height = last_fight["Blue Height"]
            weight = last_fight["Blue Weight"]
            reach = last_fight["Blue Reach"]
            win_streak = last_fight["B_current_win_streak"]

        sig_str_list, td_acc_list, td_def_list = [], [], []
        for i, row in fights.iterrows():
            if row["corner"] == "R":
                sig_str_list.append(row["R_SIG_STR_pct"])
                td_acc_list.append(row["R_TD_pct"])
                opp_td_att = row["B_TD_att"]
                opp_td_landed = row["B_TD_landed"]
            else:
                sig_str_list.append(row["B_SIG_STR_pct"])
                td_acc_list.append(row["B_TD_pct"])
                opp_td_att = row["R_TD_att"]
                opp_td_landed = row["R_TD_landed"]
            if opp_td_att > 0:
                td_def_list.append(1 - (opp_td_landed / opp_td_att))

        sig_strike_acc = np.mean(sig_str_list) * 100
        td_accuracy = np.mean(td_acc_list) * 100
        td_defense = np.mean(td_def_list) * 100 if len(td_def_list) > 0 else 0

        win_fights = fights[fights["Winner"] == name]
        finishes = len(win_fights[win_fights["Win By"].isin(["KO/TKO", "Submission"])])
        finish_rate = (finishes / wins) * 100 if wins > 0 else 0

        fighter_stats.append({
            "name": name, "age": age, "height": height, "weight": weight, "reach": reach,
            "total_fights": total_fights, "wins": wins, "win_percent": win_percent,
            "win_streak": win_streak, "sig_strike_acc": sig_strike_acc,
            "td_accuracy": td_accuracy, "td_defense": td_defense, "finish_rate": finish_rate,
        })

    red, blue = fighter_stats[0], fighter_stats[1]

    st.write("")
    with st.container(border=True):
        section_title("Fighter Comparison")
        comparison_table = pd.DataFrame({
            "Feature": ["Age", "Height (cm)", "Weight (lbs)", "Reach (cm)", "Total Fights",
                        "Wins", "Win %", "Win Streak", "Sig. Strike Accuracy",
                        "Takedown Accuracy", "Takedown Defense", "Finish Rate"],
            f"{red['name']} (Red)": [
                f"{red['age']:.0f}", f"{red['height']:.1f}", f"{red['weight']:.0f}", f"{red['reach']:.1f}",
                red['total_fights'], red['wins'], f"{red['win_percent']:.1f}%", int(red['win_streak']),
                f"{red['sig_strike_acc']:.1f}%", f"{red['td_accuracy']:.1f}%",
                f"{red['td_defense']:.1f}%", f"{red['finish_rate']:.1f}%"
            ],
            f"{blue['name']} (Blue)": [
                f"{blue['age']:.0f}", f"{blue['height']:.1f}", f"{blue['weight']:.0f}", f"{blue['reach']:.1f}",
                blue['total_fights'], blue['wins'], f"{blue['win_percent']:.1f}%", int(blue['win_streak']),
                f"{blue['sig_strike_acc']:.1f}%", f"{blue['td_accuracy']:.1f}%",
                f"{blue['td_defense']:.1f}%", f"{blue['finish_rate']:.1f}%"
            ],
        })
        st.dataframe(comparison_table, use_container_width=True, hide_index=True)

    red_score = 0
    blue_score = 0
    reasons = []

    if red["age"] < blue["age"]:
        red_score += 1
    elif blue["age"] < red["age"]:
        blue_score += 1

    for key, label in [("win_percent", "Better career win percentage"),
                        ("win_streak", "Better current win streak"),
                        ("sig_strike_acc", "Better striking accuracy"),
                        ("td_accuracy", "Better takedown accuracy"),
                        ("td_defense", "Better takedown defense"),
                        ("finish_rate", "Better finishing ability"),
                        ("reach", "Longer reach")]:
        if red[key] > blue[key]:
            red_score += 1
            reasons.append(("red", label))
        elif blue[key] > red[key]:
            blue_score += 1
            reasons.append(("blue", label))

    if red_score > blue_score:
        predicted_winner = red["name"]
    elif blue_score > red_score:
        predicted_winner = blue["name"]
    else:
        predicted_winner = "Too close to call"

    st.write("")
    score_col, result_col = st.columns(2)

    with score_col:
        with st.container(border=True):
            section_title("Score Calculation")
            s1, s2 = st.columns(2)
            with s1:
                st.markdown(f"""
                <div class="score-box">
                    <div class="score-value-red">{red_score}</div>
                    <div class="score-name">{red['name']} (Red)</div>
                </div>
                """, unsafe_allow_html=True)
            with s2:
                st.markdown(f"""
                <div class="score-box">
                    <div class="score-value-blue">{blue_score}</div>
                    <div class="score-name">{blue['name']} (Blue)</div>
                </div>
                """, unsafe_allow_html=True)

    with result_col:
        st.markdown(f"""
        <div class="winner-badge">
            <div class="trophy">🏆</div>
            <div class="score-name">Predicted Winner</div>
            <h2>{predicted_winner}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    with st.container(border=True):
        section_title("Reason for Prediction")
        for side, reason in reasons:
            name = red["name"] if side == "red" else blue["name"]
            st.markdown(f'<div class="reason-line">✅ <b>{name}</b>: {reason}</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div class="note-box">
    ℹ️ <b>Note:</b> This is a rule-based prediction using statistical comparison of past fight history.
    Actual fight outcome may vary.
    </div>
    """, unsafe_allow_html=True)


# =========================================================================
# PAGE: About Project
# =========================================================================
def render_about(df):
    named = df.rename(columns={"R_fighter": "Red Fighter", "B_fighter": "Blue Fighter"})

    total_fights = len(named)
    total_fighters = len(set(named["Red Fighter"].unique()) | set(named["Blue Fighter"].unique()))
    total_features = named.shape[1]
    date_range = f"{named['date'].dt.year.min()} - {named['date'].dt.year.max()}"

    page_header("ℹ️", "About / Project Information", "What this dashboard does and how it was built")

    r1c1, r1c2, r1c3 = st.columns(3)

    with r1c1:
        with st.container(border=True):
            st.markdown('<div class="card-title"><span class="dot"></span>Project Scenario</div>', unsafe_allow_html=True)
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
            st.markdown('<div class="card-title"><span class="dot"></span>Problem Statement</div>', unsafe_allow_html=True)
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
            st.markdown('<div class="card-title"><span class="dot"></span>Objectives</div>', unsafe_allow_html=True)
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
    r2c1, r2c2 = st.columns(2)

    with r2c1:
        with st.container(border=True):
            st.markdown('<div class="card-title"><span class="dot"></span>Technologies Used</div>', unsafe_allow_html=True)
            technologies = [("🐍", "Python"), ("🐼", "Pandas"), ("🔢", "NumPy"),
                             ("📊", "Matplotlib"), ("🌊", "Seaborn"), ("🔴", "Streamlit")]
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
            st.markdown('<div class="card-title"><span class="dot"></span>Dataset Information</div>', unsafe_allow_html=True)
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
    with st.container(border=True):
        st.markdown('<div class="card-title"><span class="dot"></span>Project Workflow</div>', unsafe_allow_html=True)
        steps = [
            ("🗄️", "Raw Data"), ("🧹", "Data Cleaning"), ("📈", "Exploratory Data Analysis"),
            ("⚖️", "Compare Fighters"), ("🏆", "Predict Winner"), ("✅", "Result & Explanation"),
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

    st.markdown("""
    <div class="about-footer">
    © 2026 UFC Fight Outcome Prediction Dashboard &nbsp;|&nbsp; Built with Streamlit ❤️
    </div>
    """, unsafe_allow_html=True)


# =========================================================================
# Sidebar navigation
# =========================================================================
if "nav" not in st.session_state:
    st.session_state.nav = PAGES[0]

with st.sidebar:
    nav = st.radio(
        "Navigation",
        PAGES,
        index=PAGES.index(st.session_state.nav),
        label_visibility="collapsed",
        key="nav_radio",
    )
    st.session_state.nav = nav


# =========================================================================
# Router
# =========================================================================
if nav == "🏠 Home":
    render_home(df)
elif nav == "📊 Dataset Overview":
    render_dataset_overview(df)
elif nav == "🔍 Exploratory Data Analysis":
    render_eda(df)
elif nav == "🥊 Red vs Blue Comparison":
    render_comparison(df)
elif nav == "🔎 Fighter Search":
    render_fighter_search(df)
elif nav == "🏆 Winner Prediction":
    render_winner_prediction(df)
elif nav == "ℹ️ About Project":
    render_about(df)
