import sys

print(sys.version)
print("================================================")
print("CSV MODULE")
print("================================================")

import csv

with open('files/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # Reads a csv file

    # next(csv_reader)  # Skips the first line

    with open('files/new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            print(line)  # Every line is a list with all values
            csv_writer.writerow(line)
