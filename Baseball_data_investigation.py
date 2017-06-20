#!/usr/bin/python

import os
from ballbase import (
    getdata,
    pre_process
    )

def process_data():
    """Process the dataset for analysis
    """

    # Specify folder location
    directory = os.path.dirname(os.path.abspath(__file__))

    # Choose to download the data
    getdata.download_file(skip_this=True)

    # Process hall of fame file to get all inducted members.
    df_hallfame = pre_process.p_hallfame(directory)

    # Process AllstarFull file to find the number of times a
    # player has been in an all stars game
    df_allstar = pre_process.p_allstar(directory)

    # Process AwardsPlayers file to find the number of times
    # a player has recieved an award
    df_awards = pre_process.p_awards(directory)

if __name__ == '__main__':
    process_data()
