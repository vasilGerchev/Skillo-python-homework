import random

number = random.randint(1, 100)
answer = int(input("Please gues the number: "))

while answer != number and answer < number:
    answer = int(input("Too low: "))
    while answer != number and answer > number:
        answer = int(input("Too high: "))
if answer == number:
    print("Congratulation, True answer, the number is", number)
