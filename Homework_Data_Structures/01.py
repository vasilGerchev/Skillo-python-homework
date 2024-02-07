def hash_list(my_list):
    return hash(tuple(my_list))


my_list = (1, 5, 7, 7, 8)
hashed_value = hash_list(my_list)
print("Hashed value:", hashed_value)
