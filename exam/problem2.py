def release_numbers(word: str) -> int:
    new_word = ""
    for i in word:
        if i.isalpha():
            new_word += ' '
            continue
        new_word += i

    return len(set([i[-1] if i[0] == '0' else i for i in new_word.split()]))


word = "a123bc34d8ef34"
print(release_numbers(word))
