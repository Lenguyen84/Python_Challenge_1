import os
import csv

csvpath = os.path.join("PyBank","Resources","Budget_data.csv")

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        print(csvreader)
        csv_header = next(csvreader)
        print(f"csv Header: {csv_header}")
