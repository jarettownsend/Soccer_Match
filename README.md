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
- **difflib**

---

## 💡 Potential Improvements

- **Better Underlying Data**  
  Some of the features in this app are limited by the data available. For example, "fouls", which is not a great stat in the first place, is represented by cards per 90 minutes (yellow + red), which is an imperfect proxy and doesn’t capture all foul behavior. Similarly, “passes” is based solely on progressive passes per 90, but doesn’t account for passing accuracy or volume, both of which are important for evaluating a player’s distribution ability.

- **Better Defensive Stats**  
  The current dataset lacks important defensive metrics like tackles won, interceptions, and clearances. As a result, defenders may not be fairly represented, and the comparison model leans more heavily on offensive metrics like goals and assists.

- **Interactive Filtering**  
  Giving users more control over which features are most important (e.g., prioritize defense vs. offense) could help tailor comparisons to specific scouting or analytical needs.