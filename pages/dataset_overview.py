
import streamlit as st
import pandas as pd
import plotly.express as px

from style import page_header, metric_card, section_title


def render_dataset_overview():
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
    fig.update_layout(
        height=330,
        paper_bgcolor="white",
        margin=dict(t=50, b=10, l=10, r=10),
        title=dict(font=dict(color="#111111")),
        font=dict(color="#333333"),
        legend=dict(font=dict(color="#333333")),
    )

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
