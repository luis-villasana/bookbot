from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    frankenstein_book_path = "books/frankenstein.txt"
    frankenstein_book_text = get_book_text(frankenstein_book_path)

    frankenstein_word_count = get_num_words(frankenstein_book_text)
    print(f"{frankenstein_word_count} words found in the document")

main()