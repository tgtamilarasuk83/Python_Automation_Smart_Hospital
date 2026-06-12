import csv
import os

def get_data(filename):
    data = []
    path = "./data_files/"+filename
    with open(path, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            data.append(row)

    return data