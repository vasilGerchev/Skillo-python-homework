import csv

# Open the CSV file for reading
with open("test.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    # Iterate through each row in the CSV file
    for row in reader:
        # Each row is a list of values
        print(row)

