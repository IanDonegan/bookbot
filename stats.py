def get_num_words(file_contents):
    #Find the number of words in a string by splitting it and checking the length of the resulting array
    return len(file_contents.split())

def get_character_dict(file_contents):
    # Accepts a string, then counts the number of occurances of each character in it, returning a dictionary
    characters = {}
    for char in file_contents:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def character_dict_to_list(dict):
    # Accepts a dictionary of character counts, and returns a sorted list of dictionaries reperesenting each character
    character_list = []
    for item in dict:
        character_list.append({
            "char": item,
            "num": dict[item]
        })
    character_list.sort(reverse=True, key=lambda item: item["num"])
    return character_list

def print_alpha_report(character_list):
    # Prints the alpha characters to the console
    for item in character_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    return
