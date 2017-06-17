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

        # Get baseball data in csv form from website
        url = "http://seanlahman.com/files/database/baseballdatabank-2017.1.zip"
        request.urlretrieve(url, filename="../baseballdatabank-2017.1.zip")

        # Unzip the dataset in the folder above the repo.
        tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
        tfile.extractall(".")
        print("Data downloaded and unzipped")

    else:
        print("Data previously downloaded")
