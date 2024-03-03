import csv

# Open the CSV file for reading
with open("test.csv", "w", newline="") as file:
    file.write("Date,Name,Amount\n")
    file.write("2024-01-01,coke,2\n")
    file.write("2024-01-01,bread,1\n")
    file.write("2024-01-02,coke,2\n")
    file.write("2024-01-02,coke,2\n")
    file.write("2024-01-03,coke,2\n")
    file.write("2024-01-03,lokum,1\n")
    file.write("2024-01-03,lokum,1\n")

    file.close()

