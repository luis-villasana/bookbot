from stats import get_num_words, get_character_count, get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(path, word_count, sorted_list):
    print("")
    
    
    pass

def main():
    frankenstein_book_path = "books/frankenstein.txt"
    frankenstein_book_text = get_book_text(frankenstein_book_path)
    frankenstein_word_count = get_num_words(frankenstein_book_text)
    character_count = get_character_count(frankenstein_book_text)
    
    # print(f"{frankenstein_word_count} words found in the document")
    # print(character_count)
    # print(get_sorted_list(character_count))

main()