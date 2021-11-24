# Script to modify excel


import pandas as pd


top_players = pd.read_excel('./ttt.xlsx')
top_players.head()


print(top_players.head())