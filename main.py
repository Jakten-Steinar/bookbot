def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dist = count_char(text)
    sorted_char_dist = sort_char_dist(char_dist)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for char in sorted_char_dist:
        print(f"The '{char}' character was found {sorted_char_dist[char]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)

def count_char(text):
    words = text.split()
    char_dist = {}

    for word in words:
        for char in word:
            c = char.lower()
            if c in char_dist:
                char_dist[c] += 1
            else:
                char_dist.update({c: 1})
    return char_dist

def sort_char_dist(chars):
    sorted_chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    #chars.sort(chars, key=None, reverse=True)
    return sorted_chars



main()