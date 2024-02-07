def find_element(element, input_list):
    for i in input_list:
        if i == element:
            return True
    return False


element_to_find = int(input("Enter the number: "))
check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = find_element(element_to_find, check_list)

if result:
    print(f"The number {element_to_find} is already exist in list")

else:
    print(f"The number {element_to_find} is not exist in list")


def increment_by_number(y):
    if y == 3:
        return y
    elif y != 3:
        return False


print("The number is:", increment_by_number(3))
