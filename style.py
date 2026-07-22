
import streamlit as st

RED = "#E10600"
BLUE = "#1e6fe0"


def load_css():
    st.markdown("""
    <style>
    .block-container{ padding-top:1.5rem; padding-bottom:2rem; }

    /* ---------- Sidebar ---------- */
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
        background: rgba(255,255,255,0.97) !important;
    }

    /* ---------- Metric cards (custom, colored-circle style) ---------- */
    .metric-card{
        background: rgba(255,255,255,0.97);
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
        min-width:46px; height:46px; border-radius:50%;
        display:flex; align-items:center; justify-content:center;
        font-size:20px; color:white;
    }
    .icon-red{ background:#E10600; }
    .icon-blue{ background:#1e6fe0; }
    .icon-green{ background:#1fa64a; }
    .icon-purple{ background:#8a3ffc; }

    .metric-value{ font-size:22px; font-weight:800; color:#111; line-height:1.1; }
    .metric-label{ font-size:12.5px; color:#777; font-weight:500; }

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


def card_title(text):
    st.markdown(f'<div class="card-title"><span class="dot"></span>{text}</div>', unsafe_allow_html=True)


def style_fig(fig, height=320):
    """Apply consistent sizing + dark, readable text color to a Plotly figure."""
    fig.update_layout(
        height=height,
        paper_bgcolor="white",
        plot_bgcolor="#fafafa",
        margin=dict(t=55, b=10, l=10, r=10),
        showlegend=False,
        title=dict(font=dict(size=15, color="#111111")),
        font=dict(color="#333333"),
    )
    return fig
