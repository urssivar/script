# Kaitag Script

Technical specification for the Kaitag Cyrillic script.

## Overview

The modern Kaitag alphabet, based on the Cyrillic script, was developed in 2024 and revised in 2026. It consists of 27 Russian letters (excluding Щщ, Фф, Ыы, Ээ, Ёё, Юю), 4 extended Cyrillic characters (**Ғғ**, **Ҡҡ**, **Ҳҳ**, **Ӏӏ**), and 12 digraphs (geminates and ejectives). Extended notation includes vowels with acute accents for stress and additional digraphs for non-phonemic sounds.

### Version History

**v1.1 (January 2026)**: Reintroduction of palochka (**Ӏӏ**) as ejective marker, replacing the soft sign approach. This change aligns with Dagestanian orthographic tradition, simplifies learning by giving **Ьь** /h/ and **Ъъ** /ʔ/ single unambiguous readings, and improves visual distinctiveness through palochka's height.

**v1.0 (February 2024)**: Initial release introducing extended Cyrillic characters, uniform consonant series representation, and explicit iotation. Used soft sign (**Ьь**) as dual marker for both /h/ and ejectivity.

### Script Design

1. **Extended Cyrillic characters**: **Ғғ** /ʁ/, **Ҡҡ** /qʰ/, **Ҳҳ** /x/. These established Cyrillic extensions maintain single-letter representation for basic consonants.

2. **Uniform consonant series**: doubling for geminates (**пп**, **тт**, **чч**, **цц**, **кк**, **ҡҡ**) and palochka (**Ӏӏ**) for all ejectives (**пӏ**, **тӏ**, **чӏ**, **цӏ**, **кӏ**, **ҡӏ**) and only for them. This consistently represents six parallel three-way contrasts (aspirated/geminate/ejective).

3. **Repurposed Russian signs** for laryngeal sounds: **Ьь** /h/ and **Ъъ** /ʔ/. In Russian these letters serve as modifiers without representing sounds themselves. Repurposing them reduces the number of special characters needed.

4. **Letter Оо** represents labialization /ʷa/ before **Аа**, while **Вв** marks both /β/ and rare labialization before other vowels. Since labialization overwhelmingly occurs with /a/, this allows simplified orthography: **беркона** /beɾkʰʷana/ "to eat" → **беркне** /beɾkʰne/ (masd.).

5. **Explicit iotation**: **Ее** /e/ and **Яя** /æ/ are always pure vowels; **Йй** /j/ is written explicitly everywhere. This eliminates Russian's context-dependent vowel readings, creating one-to-one sound-letter correspondence.

## Alphabet

42 letters, of which 12 are digraphs:

```
а б в г ғ д е ж з и й к кк кӏ ҡ ҡҡ ҡӏ л м н о п пп пӏ р с т тт тӏ у х ҳ ц цц цӏ ч чч чӏ ш ъ ь я
```

**Collation order:** The alphabet sequence above defines the sorting order. Digraphs are treated as single letters sorting after their base consonant; extended characters follow their base letters (ғ after г, ҡ after к, ҳ after х).

**Letter frequency data:** [letter_frequencies.csv](frequency/data/letter_frequencies.csv)

**Comparison with Soviet Dagestanian orthographies:**

| Kaitag | IPA      | Soviet Dagestanian           |
| ------ | -------- | ---------------------------- |
| а      | /a/      |                              |
| б      | /b/      |                              |
| в      | /β/, /ʷ/ |                              |
| г      | /g/      |                              |
| ғ      | /ʁ/      | гъ                           |
| д      | /d/      |                              |
| е      | /e/      | э (word-initially)           |
| ж      | /ʒ/      |                              |
| з      | /z/      |                              |
| и      | /i/      |                              |
| й      | /j/      | е, я, ю (word-initially)     |
| к      | /kʰ/     |                              |
| кк     | /kː/     |                              |
| кӏ     | /kʼ/     |                              |
| ҡ      | /qʰ/     | хъ, къ                       |
| ҡҡ     | /qː/     | къ, къкъ                     |
| ҡӏ     | /qʼ/     | кь, къ                       |
| л      | /l/      |                              |
| м      | /m/      |                              |
| н      | /n/      |                              |
| о      | /ʷa/     | ва                           |
| п      | /pʰ/     |                              |
| пп     | /pː/     |                              |
| пӏ     | /pʼ/     |                              |
| р      | /ɾ/      |                              |
| с      | /s/      |                              |
| т      | /tʰ/     |                              |
| тт     | /tː/     |                              |
| тӏ     | /tʼ/     |                              |
| у      | /u/      |                              |
| х      | /χ/      |                              |
| ҳ      | /x/      | хь                           |
| ц      | /tsʰ/    |                              |
| цц     | /tsː/    |                              |
| цӏ     | /tsʼ/    |                              |
| ч      | /tʃʰ/    |                              |
| чч     | /tʃː/    |                              |
| чӏ     | /tʃʼ/    |                              |
| ш      | /ʃ/      |                              |
| ъ      | /ʔ/      | гӏ                           |
| ь      | /h/      | гь, хӏ                       |
| я      | /æ/      | гӏя (word-initially), аь, аӏ |

### Characters

31 unique characters, of which 4 are from extended Cyrillic:

```
а б в г ғ д е ж з и й к ҡ л м н о п р с т у х ҳ ц ч ш ъ ь я ӏ
```

**Character frequency data:** [character_frequencies.csv](frequency/data/character_frequencies.csv)

**Extended Cyrillic characters:**

| Character | Unicode        | Name                              |
| --------- | -------------- | --------------------------------- |
| Ғ ғ       | U+0492, U+0493 | Cyrillic Letter Ghe with Stroke   |
| Ҡ ҡ       | U+04A0, U+04A1 | Cyrillic Letter Bashkir Ka        |
| Ҳ ҳ       | U+04B2, U+04B3 | Cyrillic Letter Ha with Descender |
| Ӏ ӏ       | U+04C0, U+04CF | Cyrillic Letter Palochka          |

> **Note on Palochka:** Often substituted with digit `1`, Latin `I`/`i`, lowercase `l`, vertical bar `|`, or slash `/` due to absence from standard Russian keyboards. This practice began with Soviet typewriters and continues today. **Corpora, dictionaries, and datasets should normalize these substitutions to the canonical Unicode characters U+04C0 (capital) and U+04CF (lowercase).**

### Extended Notation

Beyond the core alphabet, extended orthographic notation includes:

- **Acute diacritics** for stress marking: **а́**, **е́**, **и́**, **о́**, **у́**, **я́**
- **Tense fricatives** (phonemic status uncertain): **сс** /sː/, **шш** /ʃː/, **хх** /χː/, **ҳҳ** /xː/
- **Marginal/dialectal sounds**: **ву** /w/, **гх** /ɣ/, **ьв** /ɸ/ (onomatopoeia); **гъ** /ʡ/, **хъ** /ħ/ (peripheral dialects)

These elements are not part of the standard alphabet but are used for precise phonetic documentation, pedagogical purposes, and dialectal variation.

## Typing

Input methods are based on the standard Russian ЙЦУКЕН layout to minimize disruption to Russian keyboard users' muscle memory. An optimized Kaitag-specific layout based on character frequency would require a larger text corpus for proper analysis.

### Mobile

The layout replaces five keys for the excluded Russian letters **Щ**, **Ф**, **Ы**, **Э**, **Ю** with **Ҡ**, **Ҳ**, **Ғ**, **Ъ**, **Ӏ** respectively. These characters are positioned by frequency, with more frequent ones closer to the center.

```
й ц у к е н г ш ҡ з х
ҳ ғ в а п р о л д ж ъ
  я ч с м и т ь б ӏ
```

Accented vowels for stress marking and excluded Russian letters are accessible via long-press:

```
у: ю у́
е: э е́ ё
ш: щ
а: а́
п: ф
о: о́
я: я́
и: ы и́
```

Available for **Google Gboard** ([Google Play](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)), **Yandex Keyboard** ([Google Play](https://play.google.com/store/apps/details?id=ru.yandex.androidkeyboard), [AppStore](https://apps.apple.com/app/andeks-klaviatura/id1053139327)), and **HeliBoard** ([GitHub](https://github.com/Helium314/HeliBoard)).

### Desktop

The script requires only four additional symbols compared to standard Russian. Compose key sequences can be used to enter these characters without switching keyboard layouts.

Example configuration for [**WinCompose**](https://github.com/samhocevar/wincompose) on Windows:

```
<Multi_key> <Г> : "Ғ"  # CYRILLIC CAPITAL LETTER GHE WITH STROKE
<Multi_key> <г> : "ғ"  # CYRILLIC SMALL LETTER GHE WITH STROKE
<Multi_key> <К> : "Ҡ"  # CYRILLIC CAPITAL LETTER BASHKIR KA
<Multi_key> <к> : "ҡ"  # CYRILLIC SMALL LETTER BASHKIR KA
<Multi_key> <Х> : "Ҳ"  # CYRILLIC CAPITAL LETTER HA WITH DESCENDER
<Multi_key> <х> : "ҳ"  # CYRILLIC SMALL LETTER HA WITH DESCENDER
<Multi_key> <!> : "Ӏ"  # CYRILLIC CAPITAL LETTER PALOCHKA
<Multi_key> <1> : "ӏ"  # CYRILLIC SMALL LETTER PALOCHKA
```

Linux has built-in compose key support. For macOS, [**macos-compose**](https://github.com/Granitosaurus/macos-compose) is available.

## License

This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). If you use this specification or data in your work, please cite:

> Magomedov, M. (2026). _Kaitag Cyrillic Orthography v1.1_. Retrieved from https://github.com/alkaitagi/urssivar/script

Contact: alkaitagi@outlook.com
