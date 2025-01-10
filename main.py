book_location = "books/frankenstein.txt"

def count_words(data):
    my_list = data.split();
    #print(len(my_list))
    return len(my_list)

def sort_on(char_tuple):
    return char_tuple[1]

def count_characters(data):
    lowercase_data = data.lower()
    char_num_dict = {}
    for a_char in lowercase_data:
        if a_char in char_num_dict:
            char_num_dict[a_char] += 1
        else:
            char_num_dict[a_char] = 1
    sorted_char_list = []
    for a_char in char_num_dict:
        if a_char.isalpha():
            sorted_char_list.append((a_char, char_num_dict[a_char]))
    sorted_char_list.sort(key=sort_on)
    return sorted_char_list

def print_result(word_count, result):
    print(f"--- Begin report of {book_location} ---")
    print(f"{word_count} words found in the document")
    print("")
    for a_char_tuple in result:
        print(f"The '{a_char_tuple[0]}' character was found {a_char_tuple[1]} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        result = count_characters(file_contents)
        print_result(word_count, result)

main()
