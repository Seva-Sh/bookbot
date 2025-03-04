import sys
from stats import words_count
from stats import chars_count
from stats import chars_sort

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        key = list(char.keys())[0]
        if key.isalpha():
            print(f"{key}: {char[key]}")
    print("============= END ===============")
        


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    count = chars_count(get_book_text(book_path))
    words = words_count(get_book_text(book_path))
    # print(f"{words} words found in the document")
    # print(count)
    # print(chars_sort(count))
    print_report(book_path, words, chars_sort(count))

main()