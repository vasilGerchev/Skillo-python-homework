numbers = (1, 10, 15)

max_number = -9999999999
for num in numbers:
    if num > max_number:
        max_number = num
print("The max number is: ", max_number)

min_number = 99999999999
for num in  numbers:
    if num < min_number:
        min_number = num
print("the min number is: ", min_number)
