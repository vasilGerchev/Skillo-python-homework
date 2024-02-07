def even_number_check(nl):
    sun_even_num = 0
    for even_number in number_list:
        if even_number % 2 == 0:
            sun_even_num += even_number
    return sun_even_num


number_list = list(range(1, 5))

print(even_number_check(number_list))
