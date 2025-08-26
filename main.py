from stats import get_num_words, get_num_char, sort_char_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

frankenstein_path = "./books/frankenstein.txt"
frankenstein_words = get_num_words(get_book_text(frankenstein_path))
frankenstein_chars =get_num_char(get_book_text(frankenstein_path))
frankenstein_char_list = sort_char_report(frankenstein_chars)

def main():

    print(f"{frankenstein_words} words found in the document")
    print(frankenstein_chars)

main()
