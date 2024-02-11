words_ls = ['one', 'one', 'one', 'two', 'three', 'three']
words_one_str = "one", "one", "one", "two"
words_two_str = 'one one one two'


def get_frequency(words):
    frequency = {}
    for word in words:
        if frequency.get(word) is not None:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


print(get_frequency(words_ls))
print(get_frequency(words_one_str))
print(get_frequency(words_two_str.split(' ')))
