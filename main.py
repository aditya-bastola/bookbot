def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        print (f"The file contains {num_words} words.")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

main()
