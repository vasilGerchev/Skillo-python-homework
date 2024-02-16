class Dictionary:
    def __init__(self):
        self.value = None
        self.key = None

    def get_value(self, key):
        return self.key, self.value

    def set_value(self, key, value):
        self.key = key
        self.value = value


word_length = Dictionary()

word_length.set_value('one', 3)


print(word_length.get_value('one'))

