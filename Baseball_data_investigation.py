#!/usr/bin/python

from ballbase import (
    getdata,
    pre_process
    )

def process_data():
    """Process the dataset for analysis
    """

    getdata.download_file(skip_this=True)

    

if __name__ == '__main__':
    process_data()
