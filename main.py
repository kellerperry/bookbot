from stats import get_num_words, get_num_char, sort_char_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

frankenstein_path = "books/frankenstein.txt"
frankenstein_words = get_num_words(get_book_text(frankenstein_path))
frankenstein_chars = get_num_char(get_book_text(frankenstein_path))
frankenstein_char_list = sort_char_report(frankenstein_chars)

report_header = f"""
============ BOOKBOT ============
Analyzing book found at {frankenstein_path}...
----------- Word Count ----------
Found {frankenstein_words} total words
--------- Character Count -------"""

def main():
    print(report_header)

    for dict in frankenstein_char_list:
        char = dict["char"]
        num = dict["num"]
        if(char.isalpha()):
           print(f"{char}: {num}")


    print("============= END ===============")

main()
