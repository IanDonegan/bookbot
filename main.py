from stats import get_num_words, get_character_counts

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"Found {get_num_words(file_contents)} total words")
    print(get_character_counts(file_contents))

main() 