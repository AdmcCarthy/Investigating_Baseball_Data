#!/usr/bin/python
from __future__ import print_function

def data_audit(dataset):
    """Run a series of functions
    to audit the dataset.abs

    Designed for the master_merge
    data set created during
    pre-processing and combing the csv
    files.
    """

    dataset = check_consitency(dataset)

    dataset = check_uniformity(dataset)

    dataset = check_validity(dataset)

    dataset = check_accuracy(dataset)

    # No data completeleness check undertaken

    return dataset

def check_uniformity(data_uniform):
    """Check uniformity of columns
    to ensure they match the desired
    data types.

    Report number of missing values.
    """

    return data_uniform

def check_consitency(data_cons):
    """Check consitency of data in
    columns. Ensure values across dataset
    do not contradict each other.
    """

    return data_cons

def check_validity(data_vali):
    """Check validity of data by
    performing cross-field constraint
    checks.
    """

    return data_vali

def check_accuracy(data_acc):
    """Check accuracy of data by
    compraing to gold standards.
    """

    return data_acc
