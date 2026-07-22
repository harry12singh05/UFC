import plotly.express as px
import streamlit as st
import pandas as pd

from style import page_header, style_fig, RED, BLUE


def render_eda():
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
            fig9 = style_fig(fig9)
            fig9.update_layout(showlegend=True, legend=dict(font=dict(color="#333333")))
            st.plotly_chart(fig9, use_container_width=True)

    fight = df["Fight Type"].value_counts().head(10)
    with c2:
        with st.container(border=True):
            fig10 = px.bar(x=fight.values, y=fight.index, orientation="h", color=fight.values,
                            color_continuous_scale="Reds", title="Top 10 Fight Types")
            fig10.update_layout(
                yaxis=dict(autorange="reversed"),
                coloraxis_showscale=True,
                coloraxis_colorbar=dict(tickfont=dict(color="#333333")),
            )
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
            fig12.update_layout(
                yaxis=dict(autorange="reversed"),
                coloraxis_showscale=True,
                coloraxis_colorbar=dict(tickfont=dict(color="#333333")),
            )
            st.plotly_chart(style_fig(fig12), use_container_width=True)
