import sys
from stats import count_words, report_characters, count_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    file_contents = f.read()
    #print(file_contents)

def main():


    count_dic = count_characters(file_contents)
    report_characters(file_contents,count_dic)

main()