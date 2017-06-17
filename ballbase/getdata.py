#!/usr/bin/python
import urllib
import tarfile
import os

def download_file():
    """Download the dataset from a website
    then unzip it.
    """

    # Get baseball data in csv form from website
    url = "http://seanlahman.com/files/database/baseballdatabank-2017.1.zip"
    urllib.request.urlretrieve(url, filename="../baseballdatabank-2017.1.zip")

    # Unzip the dataset in the folder above the repo.
    os.chdir("..")
    tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
    tfile.extractall(".")
