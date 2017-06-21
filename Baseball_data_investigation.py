#!/usr/bin/python

import os
from ballbase import (
    getdata,
    pre_process
    )

def main():
    """Process the dataset for analysis
    """

    # Specify folder location
    directory = os.path.dirname(os.path.abspath(__file__))

    # Choose to download the data
    getdata.download_file(skip_this=True)

    # Process hall of fame file to get all inducted members.
    # df_hallfame = pre_process.p_hallfame(directory)

    # Process AllstarFull file to find the number of times a
    # player has been in an all stars game.
    # df_allstar = pre_process.p_allstar(directory)

    # Process AwardsPlayers file to find the number of times
    # a player has recieved an award.
    # df_awards = pre_process.p_awards(directory)

    # Process Salaries file to calculate a number of attributes
    # based on this information.
    # pre_process.p_salaries(directory)

    # Process CollegePlaying file to select a single college
    # for each player (based on most attended).
    #
    # Add college location information for each player
    # from Schools.csv
    pre_process.p_college_loc(directory)

if __name__ == '__main__':
    main()
