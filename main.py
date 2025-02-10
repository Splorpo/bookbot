def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    print(f"--- Begin Report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print_report(chars_dict)
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#def sort_on(chars_dict):
    #return chars_dict["char"]

def print_report(chars_dict):
    dict_sorted = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    for char in dict_sorted:
        if char.isalpha():
            count = dict_sorted[char]
            print(f"The '{char}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()