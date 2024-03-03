def check_prime_number(nuber):
    nuber = numbers
    if numbers == 1:
        return numbers, "Is not a prime number"
    elif numbers > 1:
        for num in range(2, numbers):
            if (numbers % num) == 0:
                return numbers, "Is not a prime number"
            else:
                return numbers, "Is a prime number"


numbers = int(input("Enter the number: "))
print(check_prime_number(numbers))
