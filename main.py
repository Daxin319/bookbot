# Main program file for BookBot

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    return

main()