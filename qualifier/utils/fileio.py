# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


"""Writes the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path provided at prompt from the save_qualifying_loans function in app.py.

    Returns:
        A list of lists that contains the rows of data from the save_qualifying_loans function in app.py.

    """

def save_csv(csvpath,data):
    header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
    #Opens file in write mode.
    with open(csvpath, 'w', newline='') as csvfile:
        #Writes data to file.
        csvwriter = csv.writer(csvfile, delimiter=",")
        #Write the header
        csvwriter.writerow(header)
        #Write the data rows
        for row in data:
            csvwriter.writerow(row)

    
        