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