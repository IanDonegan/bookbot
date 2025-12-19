from stats import get_num_words, get_character_dict, character_dict_to_list, print_alpha_report

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"Found {get_num_words(file_contents)} total words")
    character_dict = get_character_dict(file_contents)
    character_list = character_dict_to_list(character_dict)
    print_alpha_report(character_list)

main() 