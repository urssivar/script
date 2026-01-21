#!/usr/bin/env python3

import csv
from collections import Counter

LETTERS = (
    'а', 'б', 'в', 'г', 'ғ', 'д', 'е', 'ж', 'з', 'и',
    'й', 'к', 'кк', 'кӏ', 'ҡ', 'ҡҡ', 'ҡӏ', 'л', 'м', 'н',
    'о', 'п', 'пп', 'пӏ', 'р', 'с', 'т', 'тт', 'тӏ', 'у',
    'х', 'ҳ', 'ц', 'цц', 'цӏ', 'ч', 'чч', 'чӏ', 'ш', 'ъ',
    'ь', 'я'
)

# Sort letters by length descending for greedy matching
LETTERS_SORTED = sorted(LETTERS, key=len, reverse=True)


if __name__ == '__main__':
    # Tokenize using greedy longest-match algorithm
    with open('data/monocorpus.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    letters = []
    i = 0
    while i < len(text):
        if text[i].isspace():
            i += 1
            continue

        matched = False
        for letter in LETTERS_SORTED:
            if text[i:i+len(letter)] == letter:
                letters.append(letter)
                i += len(letter)
                matched = True
                break

        if not matched:
            i += 1

    letter_counts = Counter(letters)

    total = sum(letter_counts.values())
    letter_data = [
        (letter, count, round((count / total) * 100, 2))
        for letter, count in sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    ]

    with open('data/letter_frequencies.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['letter', 'frequency', 'percentage'])
        writer.writerows(letter_data)

    print(f"{total} letters analyzed, {len(letter_counts)} unique. Written to data/letter_frequencies.csv")
