import sys

print(sys.version)
print("================================================")
print("CSV MODULE")
print("================================================")

import csv

with open("files/names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)  # Reads a csv file

    # next(csv_reader)  # Skips the first line

    with open("files/new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            print(line)  # Every line is a list with all values
            csv_writer.writerow(line)

print("")
print("")
print("================================================")
print("DICT MODULE")
print("================================================")

with open("files/names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)  # Prints every line as an ordered dictionary and first line does not use field names

with open("files/names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print("")
    for line in csv_reader:
        print(line["email"])  # Prints every value at the "email" key

with open("files/names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("files/new_names_dict.csv", "w") as new_file:
        fieldnames = ["first_name", "email"]  # Choose fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()  # Writes the header for the csv file

        for line in csv_reader:
            del line["last_name"]  # Deletes the value at given key
            csv_writer.writerow(line)
