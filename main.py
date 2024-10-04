# Main program file for BookBot

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = word_count(file_path)
    print(f"{num_words} words found in the document")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def word_count(file_path):
    words = get_book_text(file_path).split()
    return len(words)


main()