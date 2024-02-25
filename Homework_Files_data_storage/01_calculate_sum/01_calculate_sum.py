with open("numbers.txt", "r") as file:
    lines = file.readlines()
    total = 0

    for line in lines:
        total += int(line.strip())

print("The sum of the numbers is:", total)
