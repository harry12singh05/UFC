import streamlit as st
import pandas as pd

from style import page_header, card_title


def render_about():
    df = pd.read_csv("train_data_cleaned.csv")
    df["date"] = pd.to_datetime(df["date"])

    total_fights = len(df)
    total_fighters = len(set(df["R_fighter"].unique()) | set(df["B_fighter"].unique()))
    total_features = df.shape[1]
    date_range = f"{df['date'].dt.year.min()} - {df['date'].dt.year.max()}"

    page_header("ℹ️", "About / Project Information", "What this dashboard does and how it was built")

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

    st.markdown("""
    <div class="about-footer">
    © 2026 UFC Fight Outcome Prediction Dashboard &nbsp;|&nbsp; Built with Streamlit ❤️
    </div>
    """, unsafe_allow_html=True)
