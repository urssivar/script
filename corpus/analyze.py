#!/usr/bin/env python3

import csv
from collections import Counter

LETTERS = (
    'а', 'ә', 'б', 'в', 'г', 'ғ', 'д',
    'е', 'ж', 'з', 'и', 'й', 'к', 'кк',
    'кӏ', 'ҡ', 'ҡҡ', 'ҡӏ', 'л', 'м', 'н',
    'о', 'п', 'пп', 'пӏ', 'р', 'с', 'т',
    'тт', 'тӏ', 'у', 'х', 'ҳ', 'һ', 'ц',
    'цц', 'цӏ', 'ч', 'чч', 'чӏ', 'ш', 'ӏ'
)

CHARS = tuple(l for l in LETTERS if len(l) == 1)


if __name__ == '__main__':
    with open('monocorpus.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    char_counts = Counter(c for c in text if c in CHARS)
    total_chars = sum(char_counts.values())
    with open('characters.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['character', 'frequency', 'percentage'])
        writer.writerows(
            (char, count, round((count / total_chars) * 100, 2))
            for char, count in sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
        )
    print(f"{total_chars} characters analyzed, {len(char_counts)} unique. Written to characters.csv")

    letters_sorted = sorted(LETTERS, key=len, reverse=True)
    letters, i = [], 0
    while i < len(text):
        for letter in letters_sorted:
            if text[i:i+len(letter)] == letter:
                letters.append(letter)
                i += len(letter)
                break
        else:
            i += 1

    letter_counts = Counter(letters)
    total_letters = sum(letter_counts.values())
    with open('letters.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['letter', 'frequency', 'percentage'])
        writer.writerows(
            (letter, count, round((count / total_letters) * 100, 2))
            for letter, count in sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
        )
    print(f"{total_letters} letters analyzed, {len(letter_counts)} unique. Written to letters.csv")
