#!/usr/bin/python
import os
import pandas as pd


def p_hallfame(folder):
    """Function to process through the hall of fame
    csv file.

    The objective is to create a new table with only
    players and the number of times they have been in
    the hall of fame.
    """

    # Get file location
    directory = folder
    file_loc = os.path.join(directory, "baseballdatabank-2017.1", "core", "HallOfFame.csv")

    # Use pandas to convert the csv to a dataframe.
    df_hof = pd.read_csv(file_loc)

    # Only interested in players
    df_player = df_hof.loc[df_hof['category'] == 'Player']

    # Only interested in those inducted into the Hall of Fame
    df_ind = df_player.loc[df_player['inducted'] == 'Y']

    # How many Hall of Fame members
    (a, b) = df_ind.shape

    print('Processed hall of fame data')
    print('There are {0} members of the Hall of Fame'.format(a))

    return df_ind
