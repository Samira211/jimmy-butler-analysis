import pandas as pd

data = pd.read_csv('jimmy_butler_2023_2024.csv')
data.columns = data.columns.str.strip() 

# average metrics
average_metrics = data[['PTS (Points)', 'AST (Assists)', 'TRB (Total Rebounds)', 'STL (Steals)', 'BLK (Blocks)', 'TOV (Turnovers)', 'FG% (Field Goal Percentage)', 'FT% ( Free Throw Percentage)', '3P% (3-Point Field Goal Percentage)']].mean()

# average metrics
print("Average Metrics:")
print(average_metrics)

#total points scored
total_points = data['PTS (Points)'].sum()
print("\nTotal Points Scored:", total_points)

#game with the highest points scored
max_points_game = data.loc[data['PTS (Points)'].idxmax()]
print("\nGame with Highest Points Scored:")
print(max_points_game[['Date', 'Opp (Opponent)', 'PTS (Points)']])

#games where Jimmy Butler scored above 30 points
high_scoring_games = data[data['PTS (Points)'] > 30]
print("\nGames where Jimmy Butler scored above 30 points:")
print(high_scoring_games[['Date', 'Opp (Opponent)', 'PTS (Points)']])

print("Average Metrics:")
print(average_metrics)
print("\nTotal Points Scored:", total_points)
print("\nGame with Highest Points Scored:")
print("\nGames where Jimmy Butler scored above 30 points:")
print(high_scoring_games)