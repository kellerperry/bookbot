from stats import get_num_words, get_num_char, sort_char_report
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def find_book_path():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        return sys.argv[1]

book_path = find_book_path()
book_word_count = get_num_words(get_book_text(book_path))
book_char_count = get_num_char(get_book_text(book_path))
book_char_list = sort_char_report(book_char_count)

report_header = f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {book_word_count} total words
--------- Character Count -------"""

def main():
    print(report_header)

    for dict in book_char_list:
        char = dict["char"]
        num = dict["num"]
        if(char.isalpha()):
           print(f"{char}: {num}")


    print("============= END ===============")

main()
