#!/usr/bin/python

import os
from ballbase import (
    getdata,
    pre_process
    )

def process_data():
    """Process the dataset for analysis
    """

    directory = os.path.dirname(os.path.abspath(__file__))

    getdata.download_file(skip_this=True)

    df_hallfame = pre_process.p_hallfame(directory)

    df_allstar = pre_process.p_allstar(directory)

if __name__ == '__main__':
    process_data()
