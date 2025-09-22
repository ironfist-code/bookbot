def get_book_text(file_path):
    with open(file_path) as f:
        text = (f.read())
    return text

from stats import words_count, count_character, sorted_characters


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    num_words = words_count(text)
    char_count = count_character(text)
    sorted_list = sorted_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
    



if __name__ == "__main__":
    main()

    


