def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"Found {len(file_contents.split())} total words")

main() 