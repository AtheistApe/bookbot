def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    print_report(text)

def get_text(file):
    with open(file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
    
def count_characters(text):
    characters = text.lower()
    char_dict = {}
    for char in characters:
        if char in char_dict:
            char_dict[char] += 1
        else: char_dict[char] = 1
    return char_dict

def print_report(text):
    num_words = count_words(text)
    char_dict = count_characters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the text\n")
    for char in char_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {char_dict[char]} times")
    print("--- End Report ---")

main()