def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        print (f"The file contains {num_words} words.")
        result = count_characters( file_contents)
        print(result)

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    my_dict = {}
    file_contents = file_contents.lower()
    for char in file_contents:
        my_dict [char] = my_dict.get(char,0) + 1
    return my_dict
   
          


main()
