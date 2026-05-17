# Kaitag Script

Technical specification for the Kaitag Cyrillic script.

> [!IMPORTANT]
> This is a draft of **v1.2**, pending thorough review and approval (tentatively 2027). The current stable version is [**v1.1**](https://github.com/urssivar/script/tree/v1.1).

**Example:**

| Kaitag                                                                                                                                                | IPA                                                                                                                                                                                 | English                                                                                                                                                                    |
| :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Һар мейдам азатдеҳ челле чи һачӏурил це: цада йәрдицци, цада ихтийарцци. Һелттай әҡӏлу ра йәһ ра деччил дилле, цалццил ца уццбе гон бугара биккан це. | haɾ ˈmejdam azatˈdex ˈtʃelle tʃihatʃʼuˈɾil tse: tsaˈda jæɾˈditsːi, tsaˈda iχtiˈjaɾtsːi. helˈtːaj ˈæqʼlu ɾa jæh ɾa ˈdetʃːil ˈdille, ˈtsaltsːil tsa utsːˈbe gʷan buˈgaɾa biˈkːan tse. | All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood. |

## Overview

The modern Kaitag alphabet, based on the Cyrillic script, was developed in 2024 and refined in 2026. It consists of 24 Russian letters (excluding **Ёё**, **Фф**, **Щщ**, **Ъъ**, **Ыы**, **Ьь**, **Ээ**, **Юю**, **Яя**), 6 extended Cyrillic letters (**Әә**, **Ғғ**, **Ҡҡ**, **Ҳҳ**, **Һһ**, **Ӏӏ**), and 12 digraphs (doubled geminates and ejectives with the palochka). Extended notation includes vowels with acute accents for stress and additional digraphs for non-phonemic sounds.

### Script Design

1. **Extended Cyrillic**: **ә** /æ/, **ғ** /ʁ/, **ҡ** /q/, **ҳ** /x/, **һ** /h/, **ӏ** /ʔ/. These established characters maintain single-letter representation for basic phonemes.

2. **Uniform series**: doubling for geminates (**пп**, **тт**, **чч**, **цц**, **кк**, **ҡҡ**) and the palochka for all ejectives (**пӏ**, **тӏ**, **чӏ**, **цӏ**, **кӏ**, **ҡӏ**). This consistently represents six parallel three-way contrasts (plain/geminate/ejective). The palochka can serve this dual role because glottal stop never occurs after the stops and affricates.

3. **Letter о** represents labialization /ʷa/ before **а**, while **в** marks both /β/ and rare labialization before other vowels. Since labialization overwhelmingly occurs with /a/, this allows simplified orthography: **беркона** /beɾkʷana/ "to eat" → **беркне** /beɾkne/ (masd.).

4. **Explicit iotation**: **е** /e/ is always a pure vowel, and **й** /j/ is written explicitly everywhere. This eliminates Russian's context-dependent vowel readings, creating one-to-one sound-letter correspondence.

## Alphabet

42 letters, of which 12 are digraphs:

```
а ә б в г ғ д е ж з и й к кк кӏ ҡ ҡҡ ҡӏ л м н о п пп пӏ р с т тт тӏ у х ҳ һ ц цц цӏ ч чч чӏ ш ӏ
```

**Collation order:** The alphabet sequence above defines the sorting order. Digraphs are treated as single letters sorting after their base consonant; extended characters follow their base letters (`ә` after `а`, `ғ` after `г`, `ҡ` after `к`, `ҳ` then `һ` after `х`, and `ӏ` the last).

**Letter frequency data:** [letters.csv](corpus/letters.csv)

**Comparison with Soviet Dagestanian orthographies.** Asterisk (\*) marks the conventions from the dissertations on Kaitag by Temirbulatova[^1] and Gasanova[^2]:

| Kaitag | IPA      | Soviet Dagestanian                                                   |
| :----- | :------- | :------------------------------------------------------------------- |
| **а**  | /a/      | **а**; **я** (iotated)                                               |
| **ә**  | /æ/      | **я**, **аь**, **аӏ**; **гӏя**\* (word-initially); **я**\* (iotated) |
| **б**  | /b/      |                                                                      |
| **в**  | /β/, /ʷ/ |                                                                      |
| **г**  | /g/      |                                                                      |
| **ғ**  | /ʁ/      | **гъ**                                                               |
| **д**  | /d/      |                                                                      |
| **е**  | /e/      | **е**; **э** (word-initially or after vowels)                        |
| **ж**  | /ʒ/      |                                                                      |
| **з**  | /z/      |                                                                      |
| **и**  | /i/      |                                                                      |
| **й**  | /j/      | **й**; **е**, **я**, **ю** (iotated vowels)                          |
| **к**  | /k/      |                                                                      |
| **кк** | /kː/     |                                                                      |
| **кӏ** | /kʼ/     |                                                                      |
| **ҡ**  | /q/      | **хъ**, **къ**                                                       |
| **ҡҡ** | /qː/     | **къ**; **къкъ**\* (intervocally)                                    |
| **ҡӏ** | /qʼ/     | **кь**, **къ**                                                       |
| **л**  | /l/      |                                                                      |
| **м**  | /m/      |                                                                      |
| **н**  | /n/      |                                                                      |
| **о**  | /ʷa/     | **-ва**                                                              |
| **п**  | /p/      |                                                                      |
| **пп** | /pː/     |                                                                      |
| **пӏ** | /pʼ/     |                                                                      |
| **р**  | /ɾ/      |                                                                      |
| **с**  | /s/      |                                                                      |
| **т**  | /t/      |                                                                      |
| **тт** | /tː/     |                                                                      |
| **тӏ** | /tʼ/     |                                                                      |
| **у**  | /u/      | **у**; **ю** (iotated)                                               |
| **х**  | /χ/      |                                                                      |
| **ҳ**  | /x/      | **хь**                                                               |
| **һ**  | /h/      | **гь**; **хӏ**\* (adjacent to **я**)                                 |
| **ц**  | /ts/     |                                                                      |
| **цц** | /tsː/    |                                                                      |
| **цӏ** | /tsʼ/    |                                                                      |
| **ч**  | /tʃ/     |                                                                      |
| **чч** | /tʃː/    |                                                                      |
| **чӏ** | /tʃʼ/    |                                                                      |
| **ш**  | /ʃ/      |                                                                      |
| **ӏ**  | /ʔ/      | **ъ**; **гӏ**\* (adjacent to **я**)                                  |

### Characters

30 unique characters, of which 6 are from extended Cyrillic:

```
а ә б в г ғ д е ж з и й к ҡ л м н о п р с т у х ҳ һ ц ч ш ӏ
```

**Character frequency data:** [characters.csv](corpus/characters.csv)

**Extended Cyrillic characters:**

| Character | Unicode        | Name                              |
| --------- | -------------- | --------------------------------- |
| Ә ә       | U+04D8, U+04D9 | Cyrillic Letter Schwa              |
| Ғ ғ       | U+0492, U+0493 | Cyrillic Letter Ghe with Stroke   |
| Ҡ ҡ       | U+04A0, U+04A1 | Cyrillic Letter Bashkir Ka        |
| Ҳ ҳ       | U+04B2, U+04B3 | Cyrillic Letter Ha with Descender |
| Һ һ       | U+04BA, U+04BB | Cyrillic Letter Shha              |
| Ӏ ӏ       | U+04C0, U+04CF | Cyrillic Letter Palochka          |

> **Note on Palochka:** Often substituted with digit `1`, Latin `I`/`i`, lowercase `l`, vertical bar `|`, or slash `/` due to absence from standard Russian keyboards. This practice began with Soviet typewriters and continues today. **Corpora, dictionaries, and datasets should normalize these substitutions to the canonical Unicode characters U+04C0 (capital) and U+04CF (lowercase).**

### Extended Notation

Beyond the core alphabet, extended orthographic notation includes:

- **Acute diacritics** (stress marking): **а́**, **ә́**, **е́**, **и́**, **о́**, **у́**
- **Tense fricatives** (phonemic status uncertain): **сс** /sː/, **хх** /χː/, **ҳҳ** /xː/, **шш** /ʃː/
- **Marginal sounds** (onomatopoeia): **ву** /w/, **гҳ** /ɣ/, **пв** /ɸ/
- **Dialectal sounds**: **гӏ** /ʡ/, **хӏ** /ħ/, **ю** /uˤ/
- **Russian letters** (loanwords and proper nouns): **ё**, **ф**, **щ**, **ъ**, **ы**, **ь**, **э**, **ю**, **я**

These elements are not part of the standard alphabet but are used for precise phonetic documentation, pedagogical purposes, and dialectal variation.

## Typing

Input methods are based on the standard Russian ЙЦУКЕН layout to minimize disruption to Russian keyboard users' muscle memory. An optimized Kaitag-specific layout based on character frequency would require a larger text corpus for proper analysis.

**Language identifiers** for keyboard layouts:

- **English**: Kaitag
- **Russian**: кайтагский
- **Kaitag**: Хайдаҡӏла
- **ISO 639-3**: `xdq`

### Mobile

Available for **Google Gboard** ([Google Play](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)), **Yandex Keyboard** ([Google Play](https://play.google.com/store/apps/details?id=ru.yandex.androidkeyboard), [App Store](https://apps.apple.com/app/andeks-klaviatura/id1053139327)), and **HeliBoard** ([GitHub](https://github.com/Helium314/HeliBoard/releases/latest)).

#### 3-row

Replaces **щ**, **ф**, **ы**, **э**, **ь**, **ю** with **ә**, **ӏ**, **һ**, **ҳ**, **ҡ**, **ғ**, keeping **я**. More frequent Kaitag letters occupy more accessible keys.

```
й ц у к е н г ш ә з х
ӏ һ в а п р о л д ж ҳ
  я ч с м и т ҡ б ғ
```

Accented vowels for stress marking and excluded Russian letters are accessible via long-press:

```
у: ю у́
е: э е́ ё
ш: щ
ә: ә́
ӏ: ъ
һ: ь
а: я а́
п: ф
о: о́
и: ы и́
```

#### 4-row

Leaves the Russian ЙЦУКЕН intact and adds new keys above:

```
' ! ? ғ ҡ ӏ һ ә ҳ — "
й ц у к е н г ш щ з х
ф ы в а п р о л д ж э
  я ч с м и т ь б ю
```

> If the keyboard does not place `,` and `.` around the spacebar, replace `'` and `"` in the top row with them.

Accented vowels are accessible via long-press:

```
ә: ә́
у: у́
е: е́ ё
ы: ы́
а: а́
о: о́
э: э́
я: я́
и: и́
ь: ъ
ю: ю́
```

### Desktop

The script requires six additional symbols compared to standard Russian. Compose key sequences can be used to enter these characters without switching keyboard layouts.

Example configuration for [**WinCompose**](https://github.com/samhocevar/wincompose) on Windows:

```
<Multi_key> <А> : "Ә"  # CYRILLIC CAPITAL LETTER SCHWA
<Multi_key> <а> : "ә"  # CYRILLIC SMALL LETTER SCHWA
<Multi_key> <Г> : "Ғ"  # CYRILLIC CAPITAL LETTER GHE WITH STROKE
<Multi_key> <г> : "ғ"  # CYRILLIC SMALL LETTER GHE WITH STROKE
<Multi_key> <К> : "Ҡ"  # CYRILLIC CAPITAL LETTER BASHKIR KA
<Multi_key> <к> : "ҡ"  # CYRILLIC SMALL LETTER BASHKIR KA
<Multi_key> <Х> : "Ҳ"  # CYRILLIC CAPITAL LETTER HA WITH DESCENDER
<Multi_key> <х> : "ҳ"  # CYRILLIC SMALL LETTER HA WITH DESCENDER
<Multi_key> <Ь> : "Һ"  # CYRILLIC CAPITAL LETTER SHHA
<Multi_key> <ь> : "һ"  # CYRILLIC SMALL LETTER SHHA
<Multi_key> <!> : "Ӏ"  # CYRILLIC CAPITAL LETTER PALOCHKA
<Multi_key> <1> : "ӏ"  # CYRILLIC SMALL LETTER PALOCHKA
<Multi_key> <ё> : "́"   # COMBINING ACUTE ACCENT
```

Linux has built-in compose key support. For macOS, [**macos-compose**](https://github.com/Granitosaurus/macos-compose) is available.

## Resources

### Data

- **[Kaitag Dictionary](https://urssivar.com/language/dictionary/)** (5,000+ lexemes, in development) with usage examples, notes, and cross-references ([source](https://github.com/urssivar/dictionary))
- **Reference corpus**: [monocorpus.txt](corpus/monocorpus.txt) (33,615 characters) extracted from Gasanova[^3]
- **Unicode exemplar data** (base, auxiliary, marks): [googlefonts/lang: xdq_Cyrl.textproto](https://github.com/googlefonts/lang/blob/main/Lib/gflanguages/data/languages/xdq_Cyrl.textproto)

### Tools

- **[Yaziv](https://yaziv.raxys.app/xdq?from=cyr_soviet&to=cyr&text=цакъкъа+г1ябал+къабагъ)** text converter: Supports transliteration between Kaitag Cyrillic and IPA representations
  - Current orthography: "Cyrillic"
  - Legacy support: "Cyrillic (2024)", "Soviet Cyrillic"
- **[Google Fonts](https://fonts.google.com/?preview.size=24&lang=xdq_Cyrl)**: Web font service and library

### References

- **[ParaType](https://paratype.github.io/cyrillic-languages/index.html?lang=Kaitag&group=cyrillic&ui=en&pg=2)**: Cyrillic typography resource
- **[Ethnologue](https://www.ethnologue.com/language/xdq/)**: Global language database
- **[Omniglot](https://www.omniglot.com/writing/kaitag.htm)**: Encyclopedia of writing systems and languages
- **[Minority Languages of Russia](https://minlang.iling-ran.ru/lang/kaytagskiy-yazyk)**: Institute of Linguistics, Russian Academy of Sciences

## Version History

**v1.2 (May 2026)**: Introduced two extended Cyrillic characters **Әә** and **Һһ** to replace **Яя** and **Ьь**, removing the mental clash with Russian reading. The palochka **Ӏӏ** additionally serves as a standalone letter for glottal stop /ʔ/ (previously **Ъъ**).

**v1.1 (January 2026)**: Reintroduced the palochka **Ӏӏ** as ejective marker, aligning with Dagestanian orthographic tradition. Added extended notation for stress marking and tense fricatives.

**v1.0 (February 2024)**: Initial release introducing extended Cyrillic characters **Ғғ**, **Ҡҡ**, and **Ҳҳ**, uniform consonant series representation, and explicit iotation. Used soft sign **Ьь** as dual marker for both /h/ and ejectivity.

[^1]: Темирбулатова, С.М. (2006). _Хайдакский диалект даргинского языка_. Диссертация на соискание учёной степени доктора филологических наук. Махачкала.

[^2]: Гасанова, У.У. (2012). _Лексика и словообразование хайдакского диалекта даргинского языка_. Диссертация на соискание учёной степени доктора филологических наук. Махачкала.

[^3]: Гасанова, У.У. (2013). _Хайдакьла хабарти_ (Хайдакские сказки). Махачкала, 152 с. Составитель: Гасанова У.У. Редактор: Сивриди Г.Н.

## License

This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). If you use this specification or data in your work, please cite:

> Magomedov, M. (2026). _Kaitag Cyrillic Script_. Retrieved from https://github.com/urssivar/script

Contact: alkaitagi@outlook.com
