def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents

def count_words(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def count_characters(file_contents):
    count_dictionary = {}
    for c in file_contents:
        count_dictionary[c.lower()] = count_dictionary.get(c.lower(), 0) + 1
    return count_dictionary

def report_characters(count_dictionary):
    alphabet = set(map(chr, range(97, 123)))
    print("--- Begin report of books in books/frankenstein.txt---")
    word_count = count_words(main())
    print(f"{word_count} words found in the document")
    print("\n")
    for char in count_dictionary:
        if char in alphabet:
            print(f"The '{char}' character was found {count_dictionary[char]} times")
    print("--- End report ---")

count_dic = count_characters(main())
report_characters(count_dic)