def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    letter_count = count_characters(text)
    print(text)
    print(words)
    print(letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(text):
    words = text.split()
    letters = {}
    for word in words:
        for character in word:
            lower_char = character.lower()
            if lower_char in letters:
                letters[f'{lower_char}'] += 1
            else:
                letters[f'{lower_char}'] = 1
    return letters

main()