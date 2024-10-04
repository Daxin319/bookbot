# Main program file for BookBot

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_count(file_path)
    num_chars = char_count(text)
    return report(file_path, num_words, num_chars)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def word_count(file_path):
    words = get_book_text(file_path).split()
    return len(words)

def char_count(text):
    lowercase = text.lower()
    chars = {}
    for char in lowercase:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(clean_chars):
    return clean_chars["count"]

def report(file_path, num_words, num_chars):
    clean_chars = []

    for char, count in num_chars.items():
        new_dict = {
            'char' : char,
            'count' : count
        }
        clean_chars.append(new_dict)
    clean_chars.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for item in clean_chars:
        if item['char'].isalpha():
            print(f"The character '{item['char']}' was found {item['count']} times")
    print("--- End Report ---")
    



main()