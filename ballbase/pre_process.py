#!/usr/bin/python
from __future__ import print_function
import os
import pandas as pd


def p_hallfame(folder):
    """Function to process through the hall of fame
    csv file.

    The objective is to create a new table with only
    players who have been inducted into
    the hall of fame.

    Takes folder as a positional argument specifying
    the folder where the baseballdatabank folder is stored.

    Returns a dataframe fitting the conditions above.
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


def p_allstar(folder):
    """Function to process through the All Star Full
    csv file.

    The objective is to create a new table counting how many
    times a player has been in an All Star Game.

    Takes folder as a positional argument specifying
    the folder where the baseballdatabank folder is stored.

    Returns a dataframe fitting the conditions above.
    """

    # Get file location
    directory = folder
    file_loc = os.path.join(directory, "baseballdatabank-2017.1", "core", "AllstarFull.csv")

    # Use pandas to convert the csv to a dataframe.
    df_allstar = pd.read_csv(file_loc)

    # Get the number of times a player has been in an all
    # star game.
    #
    # Count the number of occurences of a value within a column
    df_times_allstar = df_allstar['playerID'].value_counts()

    print('')
    print('Processed All Star data')
    print(df_times_allstar.head())

    return df_times_allstar


def p_awards(folder):
    """Function to process through the Awards Players
    csv file.

    The objective is to create a new table counting how many
    times a player has recieved an award.

    Takes folder as a positional argument specifying
    the folder where the baseballdatabank folder is stored.

    Returns a dataframe fitting the conditions above.
    """

    # Get file location
    directory = folder
    file_loc = os.path.join(directory, "baseballdatabank-2017.1", "core", "AwardsPlayers.csv")

    # Use pandas to convert the csv to a dataframe.
    df_awards = pd.read_csv(file_loc)

    # Get the number of times a player has recieved
    # an award.
    #
    # Count the number of occurences of a value within a column.
    df_times_awards = df_awards['playerID'].value_counts()

    print('')
    print('Processed Player Awards data')
    print(df_times_awards.head())

    return df_times_awards
