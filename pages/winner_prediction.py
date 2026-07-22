import pandas as pd
import numpy as np
import streamlit as st

from style import page_header, section_title


def render_winner_prediction():
    df = pd.read_csv("train_data_cleaned.csv")
    df["date"] = pd.to_datetime(df["date"])

    page_header("🏆", "Winner Prediction",
                "Rule-based prediction using each fighter's past fight statistics (no machine learning)")

    all_fighters = pd.concat([df["R_fighter"], df["B_fighter"]]).unique()
    all_fighters = sorted(all_fighters)

    with st.container(border=True):
        section_title("Select Fighters")
        col_a, col_b, col_c = st.columns([2, 2, 1])
        with col_a:
            red_name = st.selectbox("Red Corner Fighter", all_fighters, index=0)
        with col_b:
            blue_name = st.selectbox("Blue Corner Fighter", all_fighters, index=1)
        with col_c:
            st.write("")
            st.write("")
            st.button("Predict Winner", type="primary", use_container_width=True)

    if red_name == blue_name:
        st.warning("Please select two different fighters.")
        return

    fighter_names = [red_name, blue_name]
    fighter_stats = []

    for name in fighter_names:
        red_fights = df[df["R_fighter"] == name].copy()
        red_fights["corner"] = "R"
        blue_fights = df[df["B_fighter"] == name].copy()
        blue_fights["corner"] = "B"
        fights = pd.concat([red_fights, blue_fights]).sort_values("date")

        total_fights = len(fights)
        wins = len(fights[fights["Winner"] == name])
        win_percent = (wins / total_fights) * 100 if total_fights > 0 else 0

        last_fight = fights.iloc[-1]
        if last_fight["corner"] == "R":
            age = last_fight["Red Age"]
            height = last_fight["Red Height"]
            weight = last_fight["Red Weight"]
            reach = last_fight["Red Reach"]
            win_streak = last_fight["R_current_win_streak"]
        else:
            age = last_fight["Blue Age"]
            height = last_fight["Blue Height"]
            weight = last_fight["Blue Weight"]
            reach = last_fight["Blue Reach"]
            win_streak = last_fight["B_current_win_streak"]

        sig_str_list = []
        td_acc_list = []
        td_def_list = []

        for i, row in fights.iterrows():
            if row["corner"] == "R":
                sig_str_list.append(row["R_SIG_STR_pct"])
                td_acc_list.append(row["R_TD_pct"])
                opp_td_att = row["B_TD_att"]
                opp_td_landed = row["B_TD_landed"]
            else:
                sig_str_list.append(row["B_SIG_STR_pct"])
                td_acc_list.append(row["B_TD_pct"])
                opp_td_att = row["R_TD_att"]
                opp_td_landed = row["R_TD_landed"]

            if opp_td_att > 0:
                td_def_list.append(1 - (opp_td_landed / opp_td_att))

        sig_strike_acc = np.mean(sig_str_list) * 100
        td_accuracy = np.mean(td_acc_list) * 100
        if len(td_def_list) > 0:
            td_defense = np.mean(td_def_list) * 100
        else:
            td_defense = 0

        win_fights = fights[fights["Winner"] == name]
        finishes = len(win_fights[win_fights["Win By"].isin(["KO/TKO", "Submission"])])
        finish_rate = (finishes / wins) * 100 if wins > 0 else 0

        fighter_stats.append({
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "reach": reach,
            "total_fights": total_fights,
            "wins": wins,
            "win_percent": win_percent,
            "win_streak": win_streak,
            "sig_strike_acc": sig_strike_acc,
            "td_accuracy": td_accuracy,
            "td_defense": td_defense,
            "finish_rate": finish_rate,
        })

    red = fighter_stats[0]
    blue = fighter_stats[1]

    st.write("")
    with st.container(border=True):
        section_title("Fighter Comparison")

        comparison_table = pd.DataFrame({
            "Feature": ["Age", "Height (cm)", "Weight (lbs)", "Reach (cm)", "Total Fights",
                        "Wins", "Win %", "Win Streak", "Sig. Strike Accuracy",
                        "Takedown Accuracy", "Takedown Defense", "Finish Rate"],
            f"{red['name']} (Red)": [
                f"{red['age']:.0f}", f"{red['height']:.1f}", f"{red['weight']:.0f}", f"{red['reach']:.1f}",
                red['total_fights'], red['wins'], f"{red['win_percent']:.1f}%", int(red['win_streak']),
                f"{red['sig_strike_acc']:.1f}%", f"{red['td_accuracy']:.1f}%",
                f"{red['td_defense']:.1f}%", f"{red['finish_rate']:.1f}%"
            ],
            f"{blue['name']} (Blue)": [
                f"{blue['age']:.0f}", f"{blue['height']:.1f}", f"{blue['weight']:.0f}", f"{blue['reach']:.1f}",
                blue['total_fights'], blue['wins'], f"{blue['win_percent']:.1f}%", int(blue['win_streak']),
                f"{blue['sig_strike_acc']:.1f}%", f"{blue['td_accuracy']:.1f}%",
                f"{blue['td_defense']:.1f}%", f"{blue['finish_rate']:.1f}%"
            ],
        })
        st.dataframe(comparison_table, use_container_width=True, hide_index=True)

    red_score = 0
    blue_score = 0
    reasons = []

    if red["age"] < blue["age"]:
        red_score += 1
    elif blue["age"] < red["age"]:
        blue_score += 1

    if red["win_percent"] > blue["win_percent"]:
        red_score += 1
        reasons.append(("red", "Better career win percentage"))
    elif blue["win_percent"] > red["win_percent"]:
        blue_score += 1
        reasons.append(("blue", "Better career win percentage"))

    if red["win_streak"] > blue["win_streak"]:
        red_score += 1
        reasons.append(("red", "Better current win streak"))
    elif blue["win_streak"] > red["win_streak"]:
        blue_score += 1
        reasons.append(("blue", "Better current win streak"))

    if red["sig_strike_acc"] > blue["sig_strike_acc"]:
        red_score += 1
        reasons.append(("red", "Better striking accuracy"))
    elif blue["sig_strike_acc"] > red["sig_strike_acc"]:
        blue_score += 1
        reasons.append(("blue", "Better striking accuracy"))

    if red["td_accuracy"] > blue["td_accuracy"]:
        red_score += 1
        reasons.append(("red", "Better takedown accuracy"))
    elif blue["td_accuracy"] > red["td_accuracy"]:
        blue_score += 1
        reasons.append(("blue", "Better takedown accuracy"))

    if red["td_defense"] > blue["td_defense"]:
        red_score += 1
        reasons.append(("red", "Better takedown defense"))
    elif blue["td_defense"] > red["td_defense"]:
        blue_score += 1
        reasons.append(("blue", "Better takedown defense"))

    if red["finish_rate"] > blue["finish_rate"]:
        red_score += 1
        reasons.append(("red", "Better finishing ability"))
    elif blue["finish_rate"] > red["finish_rate"]:
        blue_score += 1
        reasons.append(("blue", "Better finishing ability"))

    if red["reach"] > blue["reach"]:
        red_score += 1
        reasons.append(("red", "Longer reach"))
    elif blue["reach"] > red["reach"]:
        blue_score += 1
        reasons.append(("blue", "Longer reach"))

    if red_score > blue_score:
        predicted_winner = red["name"]
    elif blue_score > red_score:
        predicted_winner = blue["name"]
    else:
        predicted_winner = "Too close to call"

    st.write("")
    score_col, result_col = st.columns(2)

    with score_col:
        with st.container(border=True):
            section_title("Score Calculation")
            s1, s2 = st.columns(2)
            with s1:
                st.markdown(f"""
                <div class="score-box">
                    <div class="score-value-red">{red_score}</div>
                    <div class="score-name">{red['name']} (Red)</div>
                </div>
                """, unsafe_allow_html=True)
            with s2:
                st.markdown(f"""
                <div class="score-box">
                    <div class="score-value-blue">{blue_score}</div>
                    <div class="score-name">{blue['name']} (Blue)</div>
                </div>
                """, unsafe_allow_html=True)

    with result_col:
        st.markdown(f"""
        <div class="winner-badge">
            <div class="trophy">🏆</div>
            <div class="score-name">Predicted Winner</div>
            <h2>{predicted_winner}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    with st.container(border=True):
        section_title("Reason for Prediction")
        for side, reason in reasons:
            if side == "red":
                st.markdown(f'<div class="reason-line">✅ <b>{red["name"]}</b>: {reason}</div>',
                             unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="reason-line">✅ <b>{blue["name"]}</b>: {reason}</div>',
                             unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div class="note-box">
    ℹ️ <b>Note:</b> This is a rule-based prediction using statistical comparison of past fight history.
    Actual fight outcome may vary.
    </div>
    """, unsafe_allow_html=True)
