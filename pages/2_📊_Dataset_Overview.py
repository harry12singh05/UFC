import streamlit as st
import pandas as pd
import plotly.express as px



st.logo("harry.png",size="large",icon_image="harry.png")

def load_css():
    st.markdown("""
    <style>
    .block-container{ padding-top:1.5rem; }

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

    .metric-card{
        background:white; border-radius:15px; padding:18px 20px;
        border:1px solid #eeeeee; box-shadow:0 5px 15px rgba(0,0,0,.08);
        transition:.25s; display:flex; align-items:center; gap:14px; height:100%;
    }
    .metric-card:hover{
        transform:translateY(-5px); border:1px solid #E10600;
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

    .section-title{
        font-size:16px; font-weight:700; color:#111;
        margin:2px 0 12px 2px; display:flex; align-items:center; gap:8px;
    }
    .section-title .dot{ width:8px; height:8px; border-radius:50%; background:#E10600; }

    .success-box{
        background:#f2fbf4; border-left:6px solid #1fa64a; padding:16px 20px;
        border-radius:12px; color:#1a7a37; font-weight:600; text-align:center;
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


df = pd.read_csv("train_data_cleaned.csv")
df = df.rename(columns={
    "R_fighter": "Red Fighter",
    "B_fighter": "Blue Fighter"
})

page_header("📊", "Dataset Overview", "Structure, quality and statistics of the UFC fight dataset")

rows = len(df)
columns = len(df.columns)
missing_values = df.isnull().sum().sum()
duplicate = df.duplicated().sum()

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

dtype_counts = df.dtypes.astype(str).value_counts()

fig = px.pie(
    values=dtype_counts.values,
    names=dtype_counts.index,
    title="Column Data Types",
    hole=0.5,
    color_discrete_sequence=["#E10600", "#1e6fe0", "#1fa64a"]
)
fig.update_layout(height=330, paper_bgcolor="white", margin=dict(t=50, b=10, l=10, r=10))

left, right = st.columns(2)

with left:
    with st.container(border=True):
        st.plotly_chart(fig, use_container_width=True)

with right:
    with st.container(border=True):
        section_title("Missing Values by Column")

        missing_col = df.isnull().sum()
        missing_col = missing_col[missing_col > 0]

        if len(missing_col) == 0:
            st.markdown('<div class="success-box">✅ No missing values found in the dataset.</div>',
                        unsafe_allow_html=True)
        else:
            st.dataframe(missing_col, use_container_width=True)

st.write("")

with st.container(border=True):
    section_title("Dataset Sample (First 5 Rows)")
    st.dataframe(df.head(), use_container_width=True)

st.write("")

with st.container(border=True):
    section_title("Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)