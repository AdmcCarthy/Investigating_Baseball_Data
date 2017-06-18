#!/usr/bin/python
from urllib import request
import tarfile
import os


def download_file():
    """Download the dataset from a website
    then unzip it.
    """

    os.chdir("..")
    if not os.path.isdir("baseballdatabank-2017.1"):

        print("Starting download")
        # Get baseball data in csv form from website
        url = "http://seanlahman.com/files/database/baseballdatabank-2017.1.zip"
        request.urlretrieve(url, filename="../baseballdatabank-2017.1.zip")

        # Unzip the dataset in the folder above the repo.
        tfile = tarfile.open("baseballdatabank-2017.1.zip", "r:gz")
        tfile.extractall(".")
        print("Data downloaded and unzipped")
        print("This database is copyright 1996-2017 by Sean Lahman.")
        print("Data licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.")

    else:
        print("Data previously downloaded")
