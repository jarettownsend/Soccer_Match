# ⚽ 24/25 EPL Player Comparison

This Streamlit application allows users to compare football players based on various statistics like scoring, assists, fouls, dribbling, and passing. The comparison is visualized using radar charts, and it also shows the closest matches for each player based on a similarity matrix computed using **cosine similarity**.

## Features

- **Radar Chart Comparison**: View a radar chart comparing two football players across key metrics.
- **Closest Matches**: Get the top 3 closest player matches from the dataset based on player names using cosine similarity.
- **Key Differences**: Discover the largest statistical differences between the two players in the comparison.

## Requirements

The following Python libraries are required to run this project:

- `scikit-learn`
- `streamlit`
- `pandas`
- `plotly`
- `difflib`
