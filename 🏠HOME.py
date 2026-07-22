import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from style import load_css, metric_card

from app_pages.dataset_overview import render_dataset_overview
from app_pages.eda import render_eda
from app_pages.comparison import render_comparison
from app_pages.fighter_search import render_fighter_search
from app_pages.winner_prediction import render_winner_prediction
from app_pages.about_project import render_about

st.set_page_config(page_title="UFC Fight Outcome Prediction", page_icon="🥊", layout="wide")

st.logo("harry.png", size="large", icon_image="harry.png")

load_css()


def render_home():
    df = pd.read_csv("train_data_cleaned.csv")
    df.rename(columns={'R_fighter': 'Red Fighter', 'B_fighter': 'Blue Fighter'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df["year"] = df['date'].dt.year

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

    total_fighters = len(set(df['Red Fighter'].unique()) | set(df['Blue Fighter'].unique()))

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("🥊", "icon-red", f"{df.shape[0]:,}", "Total Fights")
    with c2:
        metric_card("🧑", "icon-blue", f"{total_fighters:,}", "Total Fighters")
    with c3:
        metric_card("📊", "icon-green", f"{df.shape[1]}", "Total Features")
    with c4:
        metric_card("📅", "icon-purple", f"{df['year'].min()}-{df['year'].max()}", "Date Range")

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


# ---- Pages registry: label, bootstrap icon name, render function ----
PAGES = [
    {"label": "Home", "icon": "house-fill", "func": render_home},
    {"label": "Dataset Overview", "icon": "bar-chart-fill", "func": render_dataset_overview},
    {"label": "Exploratory Data Analysis", "icon": "search", "func": render_eda},
    {"label": "Red vs Blue Comparison", "icon": "people-fill", "func": render_comparison},
    {"label": "Fighter Search", "icon": "person-bounding-box", "func": render_fighter_search},
    {"label": "Winner Prediction", "icon": "trophy-fill", "func": render_winner_prediction},
    {"label": "About Project", "icon": "info-circle-fill", "func": render_about},
]

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=[p["label"] for p in PAGES],
        icons=[p["icon"] for p in PAGES],
        default_index=0,
        styles={
            "container": {"padding": "6px 4px", "background-color": "transparent"},
            "icon": {"color": "#E10600", "font-size": "16px"},
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "color": "#f2f2f2",
                "text-align": "left",
                "margin": "3px 0",
                "padding": "10px 14px",
                "border-radius": "10px",
                "--hover-color": "rgba(225,6,0,.18)",
            },
            "nav-link-selected": {
                "background-color": "#E10600",
                "color": "white",
                "font-weight": "700",
            },
        },
    )

for p in PAGES:
    if p["label"] == selected:
        p["func"]()
        break
