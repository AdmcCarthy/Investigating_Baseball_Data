#!/usr/bin/python
from __future__ import print_function
from urllib import request
import zipfile
import os


def download_file(skip_this=False):
    """Download the dataset from a website
    then unzip it.
    """

    if not skip_this:

        if not os.path.isdir("../../baseballdatabank-2017.1"):

            print("Starting download")
            # Get baseball data in csv form from website
            url = "http://seanlahman.com/files/database/baseballdatabank-2017.1.zip"
            request.urlretrieve(url, filename="../../baseballdatabank-2017.1.zip")

            # Unzip the dataset in the folder above the repo.
            with zipfile.ZipFile("../../baseballdatabank-2017.1.zip", "r") as zfile:
                zfile.extractall("../../")
            print("Data downloaded and unzipped")
            print("This database is copyright 1996-2017 by Sean Lahman.")
            print("Data licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.")

        else:
            print("Data not downloaded")
