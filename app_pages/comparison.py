import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from style import page_header, metric_card, style_fig, RED, BLUE


def render_comparison():
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
            fig = style_fig(fig)
            fig.update_layout(showlegend=True)
            st.plotly_chart(fig, use_container_width=True)

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
            fig2 = style_fig(fig2)
            fig2.update_layout(showlegend=True)
            st.plotly_chart(fig2, use_container_width=True)

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
            fig4 = style_fig(fig4)
            fig4.update_layout(showlegend=True)
            st.plotly_chart(fig4, use_container_width=True)

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
