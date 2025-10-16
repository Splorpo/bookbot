import sys
from stats import get_num_words
from stats import get_chars_dict

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    if len(sys.argv < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
4.1423-spark_trial
    print(f"--- Begin Report of {book_path} ---")
    print(f"Found {num_words} total words")
    print()
    print_report(chars_dict)

def print_report(chars_dict):
    dict_sorted = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    for char in dict_sorted:
        if char.isalpha():
            count = dict_sorted[char]
            print(f"The '{char}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
