number = 1

while number < 1000:
    number += 1
    if (number % 3) == 0 and (number % 5) == 0:
        print(number, "FizzBuzz")
    elif (number % 3) == 0:
        print(number, "Fizz")
    elif (number % 5) == 0:
        print(number, "Buzz")