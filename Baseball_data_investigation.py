#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Baseball data investigation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Script to run a data processing pipeline
    to prepare the base ball database.

    Includes downloading the dataset.
    Followed by pre-processing individual csv files
    and calulating new attributes from each of these tables.

    Output of pre-processing will be concatenated into one
    master data table suitable for exploratory data analysis.
"""
from __future__ import print_function
import os
import pandas as pd
from ballbase import (
    getdata,
    pre_process,
    auditdata
    )


def main():
    """
    Script to run a data processing pipeline
    to prepare the base ball database.
    """

    # Reset path, ensure it starts within repository
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    os.chdir("..")  # Store downloaded data outside of repo
    getdata.download_file(skip_this=True)  # Choose to skip download

    # Specify data folder location
    #
    # Can be manually set if data is stored in a different location.
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

    # Concatenate all tables together with df_college_location
    master_merge = pd.concat(
                             table_list,
                             axis=1,
                             join='inner',
                             join_axes=[df_college_location.index],
                             verify_integrity=True
                             )
    print('')
    print('Master_Merge is ready')

    master_merge = auditdata.data_audit(master_merge)
    print('')
    print('Data Audit complete')

    return master_merge


if __name__ == '__main__':
    main()
