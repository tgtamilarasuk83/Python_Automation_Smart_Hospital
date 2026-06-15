import csv
import os

def get_data(filename):

    data = []

    path = "./data_files/" + filename

    with open(path, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if not row:
                continue
            if len(row) != 8:
                print(f"Invalid row skipped: {row}")
                continue

            data.append(row)

    return data