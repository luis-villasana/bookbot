def get_num_words(book_text):
    # turn book_text argument into list and then get length of list
    word_count = len(book_text.split())
    return word_count

def get_character_count(book_text):
    character_count = {}
    for c in book_text:
        c_lower = c.lower()
        if (c_lower in character_count):
            character_count[c_lower] += 1
        else:
            character_count[c_lower] = 1
    
    return character_count

def sort_on(dict):
    return dict["num"]

def get_sorted_list(dic):
    list_of_dict = []
    for key in dic:
        if key.isalpha():
            list_of_dict.append( {"char": key, "num": dic[key]} )
    
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict



