number = int(input("Enter the number: "))

if number == 1:
    print(number, "Is not a prime number")
elif number > 1:
    for num in range(2, number):
        if (number % num) == 0:
            print(number, "Is not a prime number")
            break
    else:
        print(number, "Is a prime number")