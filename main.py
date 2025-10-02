from stats import word_counter
from stats import char_counter
from stats import making_list_dict
import sys

def get_book_path():
    return "/home/steelthemain/workspace/bookbot/books/frankenstein.txt"

def get_book_text(filepath,):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def formating_list_dict(final_dict):
    for item in final_dict:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")




book_text = get_book_text(get_book_path())
word_count = word_counter(book_text)
char_dict = char_counter(book_text)
final_dict = making_list_dict(char_dict)












print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
formating_list_dict(final_dict)
print("============= END ===============")
print(sys.argv)