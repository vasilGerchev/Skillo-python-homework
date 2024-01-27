count = 1

sum_of_even = 0
while count < 101:
    count += 1
    if (count % 2) == 0:
        sum_of_even += count
print(f"Sum of all even numbers between 1 and 100 is: {sum_of_even}")
