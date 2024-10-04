# Main program file for BookBot

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_count(file_path)
    num_chars = char_count(text)
    print(num_chars)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def word_count(file_path):
    words = get_book_text(file_path).split()
    return len(words)

def char_count(text):
    lowercase = text.lower()
    chars = {}
    for char in text:
        if char not in chars:
            chars[f."{char}"] = 1
        else:
            chars[f."{char}"] += 1
    return chars

main()