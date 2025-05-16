# ⚽ 24/25 EPL Player Comparison

This Streamlit application allows users to compare football players based on various statistics like scoring, assists, fouls, dribbling, and passing. The comparison is visualized using radar charts, and it also shows the closest matches for each player based on a similarity matrix computed using **cosine similarity**.

---

## 🚀 Demo

Try it live on **[Streamlit Cloud](https://soccermatch.streamlit.app/)**

---

## Features

- **Radar Chart Comparison**: View a radar chart comparing two football players across key metrics.
- **Closest Matches**: Get the top 3 closest player matches from the dataset based on player names using cosine similarity. This comparison reflects *relative* similarity in play style and strengths—not absolute performance.
- **Key Differences**: Discover the largest statistical differences between the two players in the comparison.

---

## 🛠️ Tech Stack

- **Scikit-learn**
- **Python**
- **Pandas**
- **Streamlit**

---

## 💡 Potential Improvements

- **Better Underlying Data**  
  Some of the features in this app are limited by the data available. For example “passing” is based solely on progressive passes per 90, but doesn’t account for passing accuracy or volume, both of which are important for evaluating a player’s distribution ability.

- **Better Defensive Stats**  
  The current dataset lacks important defensive metrics like tackles won, interceptions, and clearances. As a result, defenders may not be fairly represented, and the comparison model leans more heavily on offensive metrics like goals and assists.
