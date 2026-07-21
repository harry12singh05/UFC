import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go



st.logo("harry.png",size="large",icon_image="harry.png")

RED = "#E10600"
BLUE = "#1e6fe0"


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

    .metric-value{ font-size:22px; font-weight:800; color:#111; line-height:1.1; }
    .metric-label{ font-size:12.5px; color:#777; font-weight:500; }
    
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


def style_fig(fig, height=380):
    fig.update_layout(
        height=height,
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="#fafafa",
        margin=dict(t=50, b=10, l=10, r=10),
        title_font=dict(size=15)
    )
    return fig


df = pd.read_csv("train_data_cleaned.csv")

page_header("🔴🔵", "Red vs Blue Fighter Comparison", "How the two corners stack up, on average, across the dataset")

red_age = df["Red Age"].mean()
blue_age = df["Blue Age"].mean()
red_reach = df["Red Reach"].mean()
blue_reach = df["Blue Reach"].mean()

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

weight_df = df[(df["Red Weight"] <= 300) & (df["Blue Weight"] <= 300)]
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=["Age", "Height", "Weight", "Reach"],
            y=[df["Red Age"].mean(), df["Red Height"].mean(), weight_df["Red Weight"].mean(), df["Red Reach"].mean()],
            name="Red",
            marker_color=RED
        ))
        fig.add_trace(go.Bar(
            x=["Age", "Height", "Weight", "Reach"],
            y=[df["Blue Age"].mean(), df["Blue Height"].mean(), weight_df["Blue Weight"].mean(), df["Blue Reach"].mean()],
            name="Blue",
            marker_color=BLUE
        ))
        fig.update_layout(title="Average Physical Attributes", barmode="group")
        st.plotly_chart(style_fig(fig), use_container_width=True)

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=["KD", "SIG STR %", "TD %", "SUB ATT"],
    y=[df["R_KD"].mean(), df["R_SIG_STR_pct"].mean(), df["R_TD_pct"].mean(), df["R_SUB_ATT"].mean()],
    name="Red",
    marker_color=RED
))
fig2.add_trace(go.Bar(
    x=["KD", "SIG STR %", "TD %", "SUB ATT"],
    y=[df["B_KD"].mean(), df["B_SIG_STR_pct"].mean(), df["B_TD_pct"].mean(), df["B_SUB_ATT"].mean()],
    name="Blue",
    marker_color=BLUE
))
fig2.update_layout(title="Average Fighter Skills", barmode="group")

with col2:
    with st.container(border=True):
        st.plotly_chart(style_fig(fig2), use_container_width=True)

age = pd.DataFrame({
    "Age": pd.concat([df["Red Age"], df["Blue Age"]]),
    "Corner": ["Red"] * len(df) + ["Blue"] * len(df)
})
fig3 = px.box(age, x="Corner", y="Age", color="Corner", color_discrete_map={"Red": RED, "Blue": BLUE})
fig3.update_layout(title="Age Comparison")
with col1:
    with st.container(border=True):
        st.plotly_chart(style_fig(fig3), use_container_width=True)

fig4 = px.scatter(df, x="Red Reach", y="Blue Reach", color="Winner",
                   title="Red Reach vs Blue Reach", opacity=0.7)
fig4.update_traces(marker=dict(size=8))
with col2:
    with st.container(border=True):
        st.plotly_chart(style_fig(fig4), use_container_width=True)

cols = [
    "Red Age", "Blue Age", "Red Height", "Blue Height",
    "Red Weight", "Blue Weight", "Red Reach", "Blue Reach"
]
corr = df[cols].corr()
fig5 = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Correlation Between Red and Blue Fighter Attributes"
)
with st.container(border=True):
    st.plotly_chart(style_fig(fig5, height=460), use_container_width=True)