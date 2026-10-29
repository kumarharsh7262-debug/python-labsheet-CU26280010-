# Combine multiple CSV files into one file

import csv

files = ["file1.csv", "file2.csv"]

with open("combined.csv", "w", newline="") as out:
    w = csv.writer(out)

    for i, filename in enumerate(files):
        with open(filename, "r") as f:
            r = csv.reader(f)

            for j, row in enumerate(r):
                if i == 0 or j > 0:
                    w.writerow(row)

print("CSV files combined")