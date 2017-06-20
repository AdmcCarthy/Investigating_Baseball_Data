#!/usr/bin/python
from __future__ import print_function
import os
import pandas as pd
import numpy as np


def standarize_column(column):
    """ Calculate the standardized
    value for a column.

    To be used in df.apply

    Modified from Udacity lesson
    """

    value = (column - column.mean()) / column.std()

    return value


def gpby_tranpose_stats(df, group, column):
    """Groupby a column (group), then tranpose
    a set of values (column) on a dataframe (df).

    This will create a series of columns for all
    the values of (column).

    Following this calulcate statistics along this
    row (axis = 'columns').

    Combine results into a dataframe and return.
    """

    # Groupby and transpose a column of values according to column used to groupby
    group_column = df.sort_values(group).groupby(group)[column].apply(lambda df: df.reset_index(drop=True)).unstack()

    # Calculate statistics for all values in a row
    group_mean = group_column.mean(axis = 'columns')
    group_mean.name = ('mean_'+ str(column))
    group_max = group_column.max(axis = 'columns')
    group_max.name = ('max_' + str(column))
    group_min = group_column.min(axis = 'columns')
    group_min.name = ('min_' + str(column))

    # Combine into a dataframe for output
    df_group = pd.concat([group_mean, group_max, group_min], axis=1)

    return df_group


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


def p_salaries(folder):
    """Function to process through the salaries
    csv file.

    The objective is to find the players salary per year
    and standardize this so it is comparable to all salaries
    that year (seeing as salaries amounts change from 1985 to 2016)

    Based on this standardization each players max year, min year
    and average over all years played will be stored as new columns.

    The salary value will be stored
    for max year, min year and average of all years played.

    This should allow for relative comparisson of each player
    even with changing salaries over time.

    Maximum salary value will also be recorded as an additional
    column.

    Takes folder as a positional argument specifying
    the folder where the baseballdatabank folder is stored.

    Returns a dataframe fitting the conditions above.
    """

    # Get file location
    directory = folder
    file_loc = os.path.join(directory, "baseballdatabank-2017.1", "core", "Salaries.csv")

    # Use pandas to convert the csv to a dataframe.
    df_salary = pd.read_csv(file_loc)

    # Groupy playerid and then transpose all salary values
    # get mean, min and max and all players and return.
    player_salary = gpby_tranpose_stats(df_salary, 'playerID', 'salary')

    # Stanrdize the salary for each year
    yearly_mean = df_salary.groupby('yearID')['salary'].apply(standarize_column)
    yearly_mean.name = 'salary_standardized_annually'

    # Merge the new column onto the dataframe
    df_salary_2 = pd.concat([df_salary, yearly_mean], axis=1)

    # Groupy player id and then tranpose all standardized salary values
    # get mean, min and max and all players and return.
    player_std_salary = gpby_tranpose_stats(df_salary_2, 'playerID', 'salary_standardized_annually')

    # Concatenate the two dataframes for each player
    df_player_salary_stats = pd.concat([player_salary, player_std_salary], axis=1)

    print('')
    print('Processed Salary data')
    print(df_player_salary_stats.head())

    return df_player_salary_stats