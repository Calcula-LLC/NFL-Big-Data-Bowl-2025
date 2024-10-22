import numpy as np
import pandas as pd

# create heatmap of combined (normalized?) completion% and average yards gained by location on the field
    # go through each game for a given team, and calculate defensive weakness
    # for each team, aggregate defensive plays from each of their games, and find average yards gained (either from pass or run) and completion percentage based on location on the field
    # split up location with x-by-x yard boxes (x can vary from 1 - 5 yards)
    # OUTPUT: make first heatmap, overlay on image of football field

# use completion%, average yards gained, and other inputs to calculate isolated weakness metric for defensive players
    # inputs: completion% by location, average yards gained by location, probability of completions/yards gained on that player ... 
    # ... man coverage or not, defensive scheme
    # RESEARCH required for other inputs, formulas, etc
    # option 1: construct isolated weakness formula as linear combination of inputs, can be used to compare defensive players and exploit weaknesses offensively or defensively
    # predict isolated weakness using regression
    # option 2: some other formula based on prior research
    # OUTPUT: some novel visualization of weakness, can use gradient live plotting side by side with video of game

# predict optimal defensive coverage by minimizing isolated weakness and maximizing voronoi area
    # given calculation of defensive players' isolated weakness, use ML to find positioning of players that minimizes isolated weakness and maximizes voronoi area
    # can provide a model with predefined schemes (cover 2, quarters, nickel, etc) with constraints to minimize the isolated weakness (array of values for each player)
    # OUTPUT: overlaid voronoi area map on top of play with isolated weakness of each player displayed

games_df = pd.read_csv('data/games.csv')
player_play_df = pd.read_csv('data/player_play.csv')
players_df = pd.read_csv('data/players.csv')
plays_df = pd.read_csv('data/plays.csv')

# Tracking data
tracking_df1 = pd.read_csv('data/tracking_week_1.csv')
tracking_df2 = pd.read_csv('data/tracking_week_2.csv')
tracking_df3 = pd.read_csv('data/tracking_week_3.csv')
tracking_df4 = pd.read_csv('data/tracking_week_4.csv')
tracking_df5 = pd.read_csv('data/tracking_week_5.csv')
tracking_df6 = pd.read_csv('data/tracking_week_6.csv')
tracking_df7 = pd.read_csv('data/tracking_week_7.csv')
tracking_df8 = pd.read_csv('data/tracking_week_8.csv')
tracking_df9 = pd.read_csv('data/tracking_week_9.csv')

# For plays.csv for each play find the matching gameID in tracking data and extract the tracking data for that play, take the completion percentage and average yards
metrics_df = pd.DataFrame(columns=['gameID', 'playID', 'completion%', 'average_yards'])

