def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def main():
    word_or_phrase = input("Enter a word or phrase: ")
    if is_palindrome(word_or_phrase):
        print(f"'{word_or_phrase}' is a palindrome.")
    else:
        print(f"'{word_or_phrase}' is not a palindrome.")


if __name__ == "__main__":
    main()