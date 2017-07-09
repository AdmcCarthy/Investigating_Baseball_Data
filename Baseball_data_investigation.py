#!/usr/bin/python

from __future__ import print_function
import os
import pandas as pd
from ballbase import (
    getdata,
    pre_process,
    auditdata
    )

def main():
    """Process the dataset for analysis
    """

    # Reset path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    os.chdir("..") # Store downloaded data outside of repo
    getdata.download_file(skip_this=True) # Choose to download

    # Specify data folder location
    directory = os.path.dirname(os.path.abspath(os.path.join(__file__, "..")))

    # Process hall of fame file to get all inducted members.
    df_hallfame = pre_process.p_hallfame(directory)

    # Process AllstarFull file to find the number of times a
    # player has been in an all stars game.
    df_allstar = pre_process.p_allstar(directory)

    # Process AwardsPlayers file to find the number of times
    # a player has recieved an award.
    df_awards = pre_process.p_awards(directory)

    # Process Salaries file to calculate a number of attributes
    # based on this information.
    df_salary = pre_process.p_salaries(directory)

    # Process CollegePlaying file to select a single college
    # for each player (based on most attended).
    #
    # Add college location information for each player
    # from Schools.csv
    df_college_location = pre_process.p_college_loc(directory)

    # Process Master.csv file
    df_master = pre_process.p_master(directory)

    table_list = [
        df_master,
        df_allstar,
        df_awards,
        df_hallfame,
        df_salary,
        df_college_location
        ]

    # Merge all tables together with df_college_location
    master_merge = pd.concat(table_list, axis=1, join='inner', join_axes=[df_college_location.index], verify_integrity=True)

    print('master_merge is ready')

    master_merge = auditdata.data_audit(master_merge)

    print('data audit complete')
    temp2 = master_merge["birthYear"].dropna().copy()
    print("final birth year size", temp2.size)
    return master_merge

if __name__ == '__main__':
    main()
