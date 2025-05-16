import streamlit as st
import pandas as pd
import plotly.graph_objects as go

stats = pd.read_csv("data/normalized_stats.csv")
similarity_matrix = pd.read_csv("data/similarity_matrix.csv", index_col=0)
player_names = stats["Player"].unique().tolist()

default_player1 = "Bruno Fernandes"
default_player2 = "Erling Haaland"
index1 = player_names.index(default_player1)
index2 = player_names.index(default_player2)

st.title("⚽ 24/25 EPL Player Comparison")
st.markdown("##### Compare two players based on their stats")

col1, col2 = st.columns(2)

with col1:
    player1 = st.selectbox("Select Player 1", options=player_names, index=index1)

with col2:
    player2 = st.selectbox("Select Player 2", options=player_names, index=index2)


def get_top_matches(player, similarity_matrix, top_n=3):
    if player in similarity_matrix.index:
        similar_players = similarity_matrix[player].sort_values(ascending=False)
        similar_players = similar_players[similar_players.index != player]
        return similar_players.head(top_n).index.tolist()
    else:
        return []


top_matches1 = get_top_matches(player1, similarity_matrix)
top_matches2 = get_top_matches(player2, similarity_matrix)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"##### Closest players to {player1}")
    st.write(", ".join(top_matches1))

with col2:
    st.markdown(f"##### Closest players to {player2}")
    st.write(", ".join(top_matches2))

row1 = stats[stats["Player"] == player1].iloc[0]
row2 = stats[stats["Player"] == player2].iloc[0]


metrics = ["Scoring", "Assisting", "Dribbling", "Passing", "Minutes Played"]


values1 = [row1[m] for m in metrics] + [row1[metrics[0]]]
values2 = [row2[m] for m in metrics] + [row2[metrics[0]]]
metrics += [metrics[0]] # This closes the radar chart loop

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values1,
    theta=metrics,
    fill='toself',
    name=player1,
    fillcolor='rgba(31, 119, 180, 0.3)',
    line=dict(color='rgba(31, 119, 180, 1)')
))

fig.add_trace(go.Scatterpolar(
    r=values2,
    theta=metrics,
    fill='toself',
    name=player2,
    fillcolor='rgba(255, 127, 14, 0.3)',
    line=dict(color='rgba(255, 127, 14, 1)')
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=False,
            range=[0.3, 1]
        )
    ),
    showlegend=True
)

differences = {}
for metric in metrics[:-1]:  # exclude the duplicated first metric at the end
    diff = abs(row1[metric] - row2[metric])
    differences[metric] = diff

biggest_diff_metric = max(differences, key=differences.get)

if row1[biggest_diff_metric] > row2[biggest_diff_metric]:
    stronger_player = player1
else:
    stronger_player = player2

st.markdown("#### 🔍 Key Difference")
st.write(f"The biggest difference between these players is that **{stronger_player}** is stronger at **{biggest_diff_metric}**.")

st.plotly_chart(fig, use_container_width=True)


