def countWords(book):
    return len(book.split())


def countCharacters(text):
    characters = {}
    for char in text.lower():
        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def readBook(path):
    with open(path, "r") as book:
        return book.read()


def clearDictOfSpecialChar(dicts):
    cleared_dictionary = {}
    aplha = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for key in dicts:
        if key in aplha:
            cleared_dictionary[key] = dicts[key]

    return cleared_dictionary


def main():
    word_count = 0
    book_to_inspect = "books/frankenstein.txt"
    read_book = readBook(book_to_inspect)
    word_count = countWords(read_book)

    characters_in_book = countCharacters(read_book)

    characters_in_book = clearDictOfSpecialChar(characters_in_book)
    sorted_count_of_characters = sorted(
        characters_in_book.items(), key=lambda x: x[1], reverse=True
    )
    sorted_count_of_characters = dict(sorted_count_of_characters)

    print(f"--- Begin report of {book_to_inspect} ---")
    print()
    print(f"{word_count} words was found in the document")
    for spec in sorted_count_of_characters:
        print(f"The '{spec}' character was found {
              sorted_count_of_characters.get(spec)} times")
    print("--- End Of Report ---")


main()
