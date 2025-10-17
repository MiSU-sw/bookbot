import sys
from stats import get_num_words
from stats import get_num_chars

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    get_num_words(file)
    print("--------- Character Count -------")
    get_num_chars(file)
    print("============= END ===============")


main()
