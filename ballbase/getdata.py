#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    getdata
    ~~~~~~~~

    This module will extract the dataset for this study.
    The data is the baseball databank.
    This database is copyright 1996-2017 by Sean Lahman.
    Data licensed under a Creative Commons
    Attribution-ShareAlike 3.0 Unported License.
"""
from __future__ import print_function
from six.moves.urllib import request
import zipfile
import os
import sys

last_percent_reported = None


def download_progress_hook(count, blockSize, totalSize):
    """
    A hook to report the progress of a download.
    This is mostly intended for users with
    slow internet connections.
    Reports every 5% change in download progress.

    Entirely taken from:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/1_notmnist.ipynb
    """
    global last_percent_reported
    percent = int(count * blockSize * 100 / totalSize)

    if last_percent_reported != percent:
        if percent % 5 == 0:
            sys.stdout.write("%s%%" % percent)
            sys.stdout.flush()
        else:
            sys.stdout.write(".")
            sys.stdout.flush()

        last_percent_reported = percent


def download_file(skip_this=False):
    """
    Download the dataset from a website
    then unzip it.

    Suggestion is to path outside of repo
    before using this function to not store
    the dataset within a repository.
    """

    if not skip_this:

        # Pass if data is already downloaded
        if not os.path.isdir("baseballdatabank-2017.1"):

            print("Starting download")
            # Get baseball data in csv form from website
            url = ("http://seanlahman.com/files/database/"
                   "baseballdatabank-2017.1.zip")
            request.urlretrieve(
                                url,
                                filename="baseballdatabank-2017.1.zip",
                                reporthook=download_progress_hook
                                )

            # Unzip the dataset in the folder above the repo.
            with zipfile.ZipFile("baseballdatabank-2017.1.zip", "r") as zfile:
                zfile.extractall("")
            print("Data downloaded and unzipped")
            print("This database is copyright 1996-2017 by Sean Lahman.")
            print("Data licensed under a Creative Commons"
                  " Attribution-ShareAlike 3.0 Unported License.")

        else:
            print("Data not downloaded")
