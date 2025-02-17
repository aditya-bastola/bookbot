def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        print (f"The file contains {num_words} words.")
        result = count_characters( file_contents)
       # print(result)
        print_report(result, num_words)

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    my_dict = {}
    file_contents = file_contents.lower()
    for char in file_contents:
        my_dict [char] = my_dict.get(char,0) + 1 #.get is safe, if (char) is not present in the dict then it will return the default value that you set, or 'None' if you don't set a default value
    return my_dict

def print_report(my_dict, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print (f"{num_words} words found in the document")
    sorted_my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_my_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

   
          


main()
