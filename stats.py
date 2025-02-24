def count_words(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def count_characters(file_contents):
    count_dictionary = {}
    for c in file_contents:
        count_dictionary[c.lower()] = count_dictionary.get(c.lower(), 0) + 1
    return count_dictionary

def sorted_dictionaries(count_dictionary):
    dic_list = []
    def sort_on(dict):
        return dict["num"]
    for char in count_dictionary:
        dic_list.append({char: count_dictionary[char]})


    dic_list.sort(reverse=True, key=sort_on)
    return dic_list

def report_characters(file_contents, dic_list):
    
    alphabet = set(map(chr, range(97, 123)))
    print("--- Begin report of books in books/frankenstein.txt---")
    word_count = count_words(file_contents)
    print(f"Found {word_count} total words")
    print("\n")
    for key in dic_list:
        if key.isalpha():
            #print(f"The '{key}' character was found {dic_list[key]} times")
            print(f"{key}: {dic_list[key]}")
    print("--- End report ---")

