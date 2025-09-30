def word_counter(book_text):
    words = book_text.split()
    count = 0
    for word in words:
        count += 1
    return count


def char_counter(book_text):
    characters_dict = {}
    for char in book_text.lower():
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return(characters_dict)


def sort_on(items):
    return items["num"]

def making_list_dict(char_dict):
    char_dict = [{"char": name, "num": num} for name, num in char_dict.items() if name.isalpha()]
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict


