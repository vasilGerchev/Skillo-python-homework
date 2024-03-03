def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    if len(string1) != len(string2):
        return False

    char_count = {}
    for char in string1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    for count in char_count.values():
        if count != 0:
            return False

    return True


print(are_anagrams('listen', 'silent'))
print(are_anagrams('bob', 'obb'))
print(are_anagrams('asd', 'fgh'))
print(are_anagrams('Bob', 'OBB'))
print(are_anagrams('obb', 'bobb'))
