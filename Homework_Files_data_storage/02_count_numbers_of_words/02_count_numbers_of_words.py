with open('words.txt', 'r') as word:
    word_count = word.read()
    print(f"The text for counting is: {word_count}")
    word = word_count.split()
    word_count = len(word)
    print("The number of words is: ", word_count)


