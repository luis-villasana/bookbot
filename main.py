from stats import get_num_words, get_character_count, get_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dic in sorted_list:
        print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")

def main():
    if (len(sys.argv) == 2):
        frankenstein_book_text = get_book_text(sys.argv[1])
        frankenstein_word_count = get_num_words(frankenstein_book_text)
        character_count = get_character_count(frankenstein_book_text)
        sorted_list = get_sorted_list(character_count)

        print_report(sys.argv[1], frankenstein_word_count, sorted_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()