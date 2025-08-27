def get_num_words(book_file):
    total_words = book_file.split()
    num_words = 0
    for word in total_words:
        num_words += 1
    return num_words

def get_num_char(book_file):
    total_chars = list(book_file.lower())
    char_dic = {}
    for char in total_chars:
        if(char not in char_dic):
            char_dic[char] = 0
        char_dic[char] +=1
    return char_dic

def sort_on(char_nums):
    return char_nums["num"]

def sort_char_report(char_counts):
    pretty_char_list = []

    for char in char_counts:
        char_num = char_counts[char]
        new_char_dict = {"char": char, "num": char_num}
        pretty_char_list.append(new_char_dict)

    pretty_char_list.sort(reverse=True, key=sort_on)

    print(pretty_char_list)

    return pretty_char_list
