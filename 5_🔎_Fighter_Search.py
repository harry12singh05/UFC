import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go



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

    div[data-testid="stMetric"]{
        background:#fafafa;
        border-radius:12px;
        padding:10px 14px;
        border:1px solid #f0f0f0;
    }
    div[data-testid="stMetricValue"]{ color:#111; font-weight:800; }
    div[data-testid="stMetricLabel"]{ color:#777; font-weight:600; }

    .section-title{
        font-size:15px; font-weight:700; color:#111;
        margin:2px 0 12px 2px; display:flex; align-items:center; gap:8px;
    }
    .section-title .dot{ width:8px; height:8px; border-radius:50%; background:#E10600; }

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


def section_title(text):
    st.markdown(f'<div class="section-title"><span class="dot"></span>{text}</div>', unsafe_allow_html=True)


df = pd.read_csv("train_data_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])

page_header("🔍", "Fighter Search", "Look up any fighter's career profile and recent form")

all_fighters = pd.concat([df["R_fighter"], df["B_fighter"]]).unique()
all_fighters = sorted(all_fighters)

selected_fighter = st.selectbox("Select Fighter", all_fighters)

red_fights = df[df["R_fighter"] == selected_fighter].copy()
red_fights["corner"] = "R"
blue_fights = df[df["B_fighter"] == selected_fighter].copy()
blue_fights["corner"] = "B"

fights = pd.concat([red_fights, blue_fights])
fights = fights.sort_values("date")

if fights.empty:
    st.warning("No data found for this fighter.")
else:
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

    sig_str_list = []
    opp_sig_str_list = []
    kd_list = []
    td_acc_list = []
    td_landed_list = []
    sub_att_list = []
    td_def_list = []

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
    td_avg = np.mean(td_landed_list)
    sub_avg = np.mean(sub_att_list)
    if len(td_def_list) > 0:
        td_defense = np.mean(td_def_list) * 100
    else:
        td_defense = 0

    win_fights = fights[fights["Winner"] == selected_fighter]
    finishes = len(win_fights[win_fights["Win By"].isin(["KO/TKO", "Submission"])])
    if wins > 0:
        finish_rate = (finishes / wins) * 100
    else:
        finish_rate = 0

    performance_score = (sig_strike_acc * 0.3) + (td_accuracy * 0.2) + (win_percent * 0.4) + (finish_rate * 0.1)
    if performance_score > 100:
        performance_score = 100

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
            r=values,
            theta=categories,
            fill="toself",
            name=selected_fighter,
            line_color="#E10600",
            fillcolor="rgba(225,6,0,0.25)"
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False,
            height=400,
            paper_bgcolor="white",
            margin=dict(t=10, b=10, l=10, r=10)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.write("")
    with st.container(border=True):
        section_title("Recent Fights")

        recent = fights.sort_values("date", ascending=False).head(5)
        table_rows = []
        for i, row in recent.iterrows():
            if row["corner"] == "R":
                opponent = row["B_fighter"]
            else:
                opponent = row["R_fighter"]

            if row["Winner"] == selected_fighter:
                result = "Win"
            else:
                result = "Loss"

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