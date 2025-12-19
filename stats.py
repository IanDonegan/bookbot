def get_num_words(file_contents):
    return len(file_contents.split())

def get_character_counts(file_contents):
    characters = {}
    for char in file_contents:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters