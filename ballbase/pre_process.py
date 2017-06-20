#!/usr/bin/python
import os
import pandas as pd


def p_hallfame():
    """Function to process through the hall of fame
    csv file.

    The objective is to create a new table with only
    players and the number of times they have been in
    the hall of fame.
    """

    # Get file location
    directory = os.path.dirname(os.path.abspath(__file__))
    file_loc = os.path.join(directory, "baseballdatabank-2017.1", "HallOfFame.csv")

    # Use pandas to convert the csv to a dataframe.
    df = pd.read_csv(file_loc)
