import plotly.express as px
import streamlit as st
import pandas as pd



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


def style_fig(fig, height=320):
    fig.update_layout(
        height=height,
        paper_bgcolor="white",
        plot_bgcolor="#fafafa",
        margin=dict(t=50, b=10, l=10, r=10),
        title_font=dict(size=15)
    )
    return fig


df = pd.read_csv("train_data_cleaned.csv")

page_header("📊", "Exploratory Data Analysis", "Distributions, trends and patterns across the UFC dataset")

c1, c2 = st.columns(2)

with c1:
    with st.container(border=True):
        fig1 = px.histogram(df, x="Red Age", title="🔴 Red Fighter Age Distribution",
                             color_discrete_sequence=[RED])
        st.plotly_chart(style_fig(fig1), use_container_width=True)
with c2:
    with st.container(border=True):
        fig2 = px.histogram(df, x="Blue Age", title="🔵 Blue Fighter Age Distribution",
                             color_discrete_sequence=[BLUE])
        st.plotly_chart(style_fig(fig2), use_container_width=True)

with c1:
    with st.container(border=True):
        fig3 = px.histogram(df, x="Red Height", title="🔴 Red Fighter Height Distribution",
                             color_discrete_sequence=[RED], nbins=30)
        st.plotly_chart(style_fig(fig3), use_container_width=True)
with c2:
    with st.container(border=True):
        fig4 = px.histogram(df, x="Blue Height", title="🔵 Blue Fighter Height Distribution",
                             color_discrete_sequence=[BLUE], nbins=30)
        st.plotly_chart(style_fig(fig4), use_container_width=True)

weight_df = df[(df["Red Weight"] <= 300) & (df["Blue Weight"] <= 300)]
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
        fig7 = px.histogram(df, x="Red Reach", title="🔴 Red Fighter Reach Distribution",
                             nbins=25, color_discrete_sequence=[RED])
        st.plotly_chart(style_fig(fig7), use_container_width=True)
with c2:
    with st.container(border=True):
        fig8 = px.histogram(df, x="Blue Reach", nbins=25, title="🔵 Blue Fighter Reach Distribution",
                             color_discrete_sequence=[BLUE])
        st.plotly_chart(style_fig(fig8), use_container_width=True)

df = df[df["Win By"] != "Decision_Split"]
win_method = df["Win By"].value_counts()
with c1:
    with st.container(border=True):
        fig9 = px.pie(values=win_method.values, names=win_method.index, hole=0.5,
                       title="Win Method Distribution",
                       color_discrete_sequence=[RED, "#ff8c00", BLUE, "#1fa64a", "#8a3ffc"])
        st.plotly_chart(style_fig(fig9), use_container_width=True)

fight = df["Fight Type"].value_counts().head(10)
with c2:
    with st.container(border=True):
        fig10 = px.bar(x=fight.values, y=fight.index, orientation="h", color=fight.values,
                        color_continuous_scale="Reds", title="Top 10 Fight Types")
        fig10.update_layout(yaxis=dict(autorange="reversed"), coloraxis_showscale=True)
        st.plotly_chart(style_fig(fig10), use_container_width=True)

df["date"] = pd.to_datetime(df["date"])
df["Year"] = df["date"].dt.year
yearly = df.groupby("Year").size().reset_index(name="Total Fights")
with c1:
    with st.container(border=True):
        fig11 = px.line(yearly, x="Year", y="Total Fights", markers=True,
                         title="UFC Fights per Year", color_discrete_sequence=[RED])
        st.plotly_chart(style_fig(fig11), use_container_width=True)

wins = df["Winner"].value_counts().head(10)
with c2:
    with st.container(border=True):
        fig12 = px.bar(x=wins.values, y=wins.index, color_continuous_scale="Reds",
                        title="Top 10 Winners", color=wins.values)
        fig12.update_layout(yaxis=dict(autorange="reversed"), coloraxis_showscale=True)
        st.plotly_chart(style_fig(fig12), use_container_width=True)