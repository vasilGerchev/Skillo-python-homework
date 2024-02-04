def simple_calculator(number_a, number_b, operator):
    if operator == "+":
        return number_a + number_b
    elif operator == "-":
        return number_a - number_b
    elif operator == "*":
        return number_a * number_b
    elif operator == "/":
        return number_a / number_b


first_number = int(input())
second_number = int(input())

result_add = simple_calculator(first_number, second_number, "+")
result_subtraction = simple_calculator(first_number, second_number, "-")
result_multiplication = simple_calculator(first_number, second_number, "*")
result_division = simple_calculator(first_number, second_number, "/")


print("Addition", result_add)
print("Subtraction", result_subtraction)
print("Multiplication", result_multiplication)
print("Division", result_division)
