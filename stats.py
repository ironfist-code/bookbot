def words_count(text):
    return len(text.split())

#count all the characters:
def count_character(text):
    counts = {}
    text = text.lower()
    for character in text:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts

#takes the charcter dictionary and sorts it:
def sorted_characters(counts):
    result = []
    for char, num in counts.items():
        if char.isalpha():
            result.append({"char": char, "num": num})

    def sort_on(item):
        return item["num"]

    result.sort(reverse=True, key=sort_on)
    return result
