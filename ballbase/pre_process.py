#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import pandas as pd
import numpy as np


def standarize_column(column):
    """
    Calculate the standardized
    value for each row based on
    a column of values.

    To be used in df.apply using
    axis='index' or '0', so that
    it is applied on a column of data.

    Modified from Udacity lesson

    Parameters
    ----------
    column : array_like
        column of data, pandas series or DataFrame

    Returns
    -------
    value : int/float
        Each rows standardised value.
    """

    value = (column - column.mean()) / column.std()

    return value


def gpby_tranpose_stats(df, group, column):
    """
    Groupby column values, 'group', then tranpose
    a set of values, 'column' on a dataframe.

    This will create a series of columns for all
    the values of 'column'.

    Following this calulcate statistics along this
    row (axis = 'columns').

    Combine results into a dataframe and return.

    Parameters
    ----------
    df : DataFrame
        pandas DataFrame
    group : string
        column header name to be used to
        group the DataFrame
    column : string
        column header to be used to
        get values from

    Returns
    -------
    df_group : DataFrame
    """

    # Groupby and transpose a column of values
    # according to column used to groupby.
    group_column = (
                    df.sort_values(group)
                    .groupby(group)[column]
                    .apply(
                           lambda df: df.reset_index(drop=True)
                           )
                    .unstack()
                    )

    # Calculate statistics for all values in a row
    group_mean = group_column.mean(axis='columns')
    group_mean.name = ('mean_' + str(column))

    group_max = group_column.max(axis='columns')
    group_max.name = ('max_' + str(column))

    group_min = group_column.min(axis='columns')
    group_min.name = ('min_' + str(column))

    # Combine into a dataframe for output
    df_group = pd.concat(
                         [group_mean, group_max, group_min],
                         axis=1
                         )

    return df_group


def gpby_tranpose_college(df, group, column):
    """Groupby a column (group), then tranpose
    a set of values (column) on a dataframe (df).

    This will create a series of columns for all
    the values of (column).

    Following this calulcate which column value
    occurs the most often.

    If tied select the first occurence.

    Combine results into a dataframe and return.

    Parameters
    ----------
    df : DataFrame
        pandas DataFrame
    group : string
        column header name to be used to
        group the DataFrame
    column : string
        column header to be used to
        get values from

    Returns
    -------
    df_group : DataFrame
    """

    # Groupby and transpose a column of values
    # according to column used to groupby.
    group_columns = (
                    df.sort_values(group)
                    .groupby(group)[column]
                    .apply(
                           lambda df: df.reset_index(drop=True)
                           )
                    .unstack()
                    )

    # Calculate the most common value
    group_mode = group_columns.mode(axis='columns')

    # Select only the first column, chooses alphabetically
    # given a tie
    mode_college = group_mode[0]
    mode_college.name = ('mode_' + str(column))

    return mode_college


def p_hallfame(folder):
    """Get dataframe after processing
    through the hall of fame csv file.

    The objective is to create a new table with only
    players who have been inducted into
    the hall of fame.

    Paramters
    ---------
    folder : string
        Takes folder as a positional argument specifying
        the folder where the baseballdatabank folder is stored.

    Returns
    -------
    df_ind : DataFrame
        Returns a dataframe fitting the conditions above.
    """

    directory = folder
    file_loc = os.path.join(
                            directory,
                            "baseballdatabank-2017.1",
                            "core",
                            "HallOfFame.csv"
                            )

    df_hof = pd.read_csv(file_loc)

    # Only interested in players
    df_player = (
                df_hof.loc                        # Find position of
                [df_hof['category'] == 'Player']  # all 'player' rows
                .copy()                           # and create a copy
                )

    # Only interested in those inducted into the Hall of Fame
    df_ind = (
              df_player.loc                   # Find position of
              [df_player['inducted'] == 'Y']  # inducted rows
              .copy()                         # and create a copy
              )
    # Change index to playerID to be used as key value
    # to concatenate on.
    df_ind.set_index("playerID", inplace=True)

    print('Processed hall of fame data')

    return df_ind


def p_allstar(folder):
    """
    Get a DataFrame after processing
    through the All Star Full csv file.

    The objective is to create a new table counting how many
    times a player has been in an All Star Game.

    Parameters
    ----------
    folder : string
        Takes folder as a positional argument specifying
        the folder where the baseballdatabank folder is stored.

    Returns
    -------
    df_times_allstar : DataFrame
        Returns a dataframe fitting the conditions above.
    """

    directory = folder
    file_loc = os.path.join(
                            directory,
                            "baseballdatabank-2017.1",
                            "core",
                            "AllstarFull.csv"
                            )

    df_allstar = pd.read_csv(file_loc)

    # Get the number of times a player has been in an all
    # star game.
    #
    # Count the number of occurences of a value within a column
    df_times_allstar = df_allstar['playerID'].value_counts()
    df_times_allstar.name = 'allstar_count'

    print('')
    print('Processed All Star data')

    return df_times_allstar


def p_awards(folder):
    """
    Get a DataFrame after processing
    through the Awards Players csv file.

    The objective is to create a new table counting how many
    times a player has recieved an award.

    Parameters
    ----------
    folder : string
        Takes folder as a positional argument specifying
        the folder where the baseballdatabank folder is stored.

    Returns
    -------
    df_times_awards : DataFrame
        Returns a dataframe fitting the conditions above.
    """

    directory = folder
    file_loc = os.path.join(
                            directory,
                            "baseballdatabank-2017.1",
                            "core",
                            "AwardsPlayers.csv"
                            )

    df_awards = pd.read_csv(file_loc)

    # Get the number of times a player has recieved
    # an award.
    #
    # Count the number of occurences of a value within a column.
    df_times_awards = df_awards['playerID'].value_counts()
    df_times_awards.name = 'award_count'

    print('')
    print('Processed Player Awards data')

    return df_times_awards


def p_salaries(folder):
    """
    Geta DataFrame after processing
    through the salaries csv file.

    The objective is to find the players salary per year
    and standardize this so it is comparable to all salaries
    that year (seeing as salaries amounts change from 1985 to 2016)

    Based on this standardization each players max year, min year
    and average over all years played will be stored as new columns.

    This should allow for relative comparisson of each player
    even with changing salaries over time.

    The original salary value will be stored
    for max year, min year and average of all years played.


    Parameters
    ----------
    folder : string
        Takes folder as a positional argument specifying
        the folder where the baseballdatabank folder is stored.

    Returns
    -------
    df_player_salary_stats : DataFrame
        Returns a dataframe fitting the conditions above.
    """

    directory = folder
    file_loc = os.path.join(
                            directory,
                            "baseballdatabank-2017.1",
                            "core",
                            "Salaries.csv"
                            )

    df_salary = pd.read_csv(file_loc)

    # Groupy playerid and then transpose all salary values
    # get mean, min and max and all players and return.
    #
    # Used as each player will have a row for each year they have
    # played and were paid.
    player_salary = gpby_tranpose_stats(
                                        df_salary,
                                        'playerID',
                                        'salary')

    # Stanrdize the salary for each year
    yearly_mean = (
                   df_salary.groupby('yearID')  # Groupby yearID
                   ['salary']                   # Select salary column
                   .apply(standarize_column)    # and apply function
                   )
    yearly_mean.name = 'salary_standardized_annually'

    # Merge the new column onto the dataframe to be used
    # as input for gpby_tranpose_stats
    df_salary_2 = pd.concat([df_salary, yearly_mean], axis=1)

    # Groupy player id and then tranpose all standardized salary values
    # get mean, min and max and all players and return.
    player_std_salary = gpby_tranpose_stats(
                                            df_salary_2,
                                            'playerID',
                                            'salary_standardized_annually'
                                            )

    # Concatenate the two dataframes for each player
    df_player_salary_stats = pd.concat(
                                       [player_salary, player_std_salary],
                                       axis=1
                                       )

    print('')
    print('Processed Salary data')

    return df_player_salary_stats


def p_college_loc(folder):
    """
    Get DataFrame after processing both
    College Playing csv file and Schools
    csv file.

    Objective is to create a single output
    stating which college a player attended and
    where that college is located.

    Some players will have attended more than
    one educational institute. To solve this issue
    the institute with the most years attended
    will be selected. Given a tie,
    the college selected alphabetically
    (e.g. a before b, d before j).

    The output will be a series of columns for a single
    institute for each player.

    Parameters
    ----------
    folder : string
        Takes folder as a positional argument specifying
        the folder where the baseballdatabank folder is stored.

    Returns
    -------
    college_location : DataFrame
        Returns a dataframe fitting the conditions above.
    """

    directory = folder
    file_loc = os.path.join(
                            directory,
                            "baseballdatabank-2017.1",
                            "core",
                            "CollegePlaying.csv"
                            )
    df_college = pd.read_csv(file_loc)

    file_loc = os.path.join(
                            directory,
                            "baseballdatabank-2017.1",
                            "core",
                            "Schools.csv"
                            )
    df_schools = pd.read_csv(file_loc)
    df_schools = df_schools.set_index(['schoolID'])

    # Get the mode value for college for each player
    mode_college = gpby_tranpose_college(
                                         df_college,
                                         'playerID',
                                         'schoolID'
                                         )

    def get_value(row, column_name, dataframe=df_schools):
        """
        Short function to be used in
        .apply in pandas
        """

        # Check if value is in schools.csv schools id.
        #
        # Return NAN if there is an error.
        if row in df_schools.index:
            value = dataframe.loc[row, column_name]

        else:
            value = 'NAN'

        return value

    # Select each column needed from within college data
    name_full = mode_college.apply(get_value, column_name='name_full')
    name_full.name = 'college_name_full'
    city = mode_college.apply(get_value, column_name='city')
    city.name = 'college_city'
    state = mode_college.apply(get_value, column_name='state')
    state.name = 'college_state'
    country = mode_college.apply(get_value, column_name='country')
    country.name = 'college_country'

    college_location = pd.concat(
                                 [mode_college, name_full,
                                  city, state, country],
                                 axis=1
                                 ).copy()

    print("")
    print('Processed college locations')

    return college_location


def p_master(folder):
    """
    Dataframe from the master.csv.

    Parameters
    ----------
    folder : string
        Takes folder as a positional argument specifying
        the folder where the baseballdatabank folder is stored.

    Returns
    -------
    df_master : DataFrame
        Returns a dataframe fitting the conditions above.
    """

    directory = folder
    file_loc = os.path.join(
                            directory,
                            "baseballdatabank-2017.1",
                            "core",
                            "Master.csv"
                            )
    df_master = pd.read_csv(file_loc)
    df_master.set_index("playerID", inplace=True)

    print("")
    print('Processed master file')

    return df_master
