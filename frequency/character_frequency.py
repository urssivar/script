#!/usr/bin/env python3

import csv
from collections import Counter

CHARS = (
    'а', 'б', 'в', 'г', 'ғ', 'д', 'е', 'ж', 'з', 'и',
    'й', 'к', 'ҡ', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
    'т', 'у', 'х', 'ҳ', 'ц', 'ч', 'ш', 'ъ', 'ь', 'я',
    'ӏ'
)


if __name__ == '__main__':
    with open('data/monocorpus.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    text_chars = [c for c in text if c in CHARS]
    char_counts = Counter(text_chars)

    total = sum(char_counts.values())
    char_data = [
        (char, count, round((count / total) * 100, 2))
        for char, count in sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    ]

    with open('data/character_frequencies.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['character', 'frequency', 'percentage'])
        writer.writerows(char_data)

    print(f"{total} characters analyzed, {len(char_counts)} unique. Written to data/character_frequencies.csv")
