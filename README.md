# Kaitag Script

> Draft of **v1.2**, pending review (tentative finalization 2027). Stable version: [**v1.1**](https://github.com/urssivar/script/tree/v1.1).

The modern Kaitag Cyrillic alphabet was developed in 2024 and updated in 2026. It uses 24 letters from the Russian alphabet, 6 extended Cyrillic letters (**Әә**, **Ғғ**, **Ҡҡ**, **Ҳҳ**, **Һһ**, **Ӏӏ**), and 12 digraphs for geminates and ejectives.

<!--
Alternative longer summary for external references where the full Script Design section isn't available:

The modern Kaitag Cyrillic alphabet was developed in 2024 and updated in 2026. It consists of 24 letters from the Russian alphabet (excluding **Ёё**, **Фф**, **Щщ**, **Ъъ**, **Ыы**, **Ьь**, **Ээ**, **Юю**, **Яя**), 6 extended Cyrillic letters (**Әә**, **Ғғ**, **Ҡҡ**, **Ҳҳ**, **Һһ**, **Ӏӏ**), and 12 digraphs (doubled geminates and ejectives with the palochka). Extended notation covers stress marking, marginal and dialectal sounds, and loanword letters.
-->

_The Universal Declaration of Human Rights, Article 1:_

| Kaitag                                                                                                                                                | IPA                                                                                                                                                                                 | English                                                                                                                                                                    |
| :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Һар мейдам азатдеҳ челле чи һачӏурил це: цада йәрдицци, цада ихтийарцци. Һелттай әҡӏлу ра йәһ ра деччил дилле, цалццил ца уццбе гон бугара биккан це. | haɾ ˈmejdam azatˈdex ˈtʃelle tʃihatʃʼuˈɾil tse: tsaˈda jæɾˈditsːi, tsaˈda iχtiˈjaɾtsːi. helˈtːaj ˈæqʼlu ɾa jæh ɾa ˈdetʃːil ˈdille, ˈtsaltsːil tsa utsːˈbe gʷan buˈgaɾa biˈkːan tse. | All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood. |

## Script Design

1. **Extended Cyrillic**: Each basic phoneme has a dedicated single-letter representation — **ә** /æ/, **ғ** /ʁ/, **ҡ** /q/, **ҳ** /x/, **һ** /h/, **ӏ** /ʔ/.

2. **Uniform series**: Geminates are doubled (**пп**, **тт**, **чч**, **цц**, **кк**, **ҡҡ**) and ejectives take the palochka (**пӏ**, **тӏ**, **чӏ**, **цӏ**, **кӏ**, **ҡӏ**), producing six parallel three-way contrasts (plain/geminate/ejective).

3. **Palochka**: **ӏ** marks ejectives and also stands alone for /ʔ/. The dual role is licensed phonotactically: the glottal stop occurs only after vowels or sonorants, never after stops or affricates. Word-initial /ʔ/ is phonetic and unwritten.

4. **Labialization**: Letter **о** is shorthand for **-ва** /ʷa/ after a consonant — the dominant context and a productive one. Labialization cannot end a syllable, so when the vowel drops in inflection, the labialization drops with it — **беркона** /beɾkʷana/ "to eat" → **беркне** /beɾkne/ (masd.) — and the single-letter encoding tracks this alternation directly. In the rare case before **ә** /æ/ or **е** /e/, labialization is lexicalized and **-в** is used instead: **швел** /ʃʷel/ "five", **ҡвә** /qʷæ/ "oath".

5. **Explicit iotation**: **й** /j/ is always written, and **е** /e/ is always a pure vowel. This removes Russian's context-dependent readings and creates one-to-one sound-letter correspondence: **йулған** /julʁan/ "quilt", **йерга** /jerga/ "turn", **етти** /etːi/ "to you".

## Alphabet

42 letters, of which 12 are digraphs:

```
а ә б в г ғ д е ж з и й к кк кӏ ҡ ҡҡ ҡӏ л м н о п пп пӏ р с т тт тӏ у х ҳ һ ц цц цӏ ч чч чӏ ш ӏ
```

**Collation order**: The alphabet sequence above defines the sorting order. Digraphs are treated as single letters sorting after their base consonant, and extended characters follow their base letters — `ә` after `а`, `ғ` after `г`, `ҡ` after `к`, `ҳ` then `һ` after `х`, with `ӏ` sorting last.

**Letter frequency data**: [letters.csv](corpus/letters.csv)

**Comparison with Soviet Dagestani orthographies**: Empty cells indicate identical representation. Leading hyphens (**-ва**) mark sequences bound to a preceding consonant. An asterisk (\*) marks conventions from the dissertations by Temirbulatova[^1] and Gasanova[^2].

| Kaitag | IPA      | Soviet Dagestani                                                     |
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
| **ҡҡ** | /qː/     | **къ**; **къкъ**\* (intervocalically)                                |
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

**Character frequency data**: [characters.csv](corpus/characters.csv)

**Extended Cyrillic characters**:

| Character | Unicode        | Name                              |
| --------- | -------------- | --------------------------------- |
| Ә ә       | U+04D8, U+04D9 | Cyrillic Letter Schwa             |
| Ғ ғ       | U+0492, U+0493 | Cyrillic Letter Ghe with Stroke   |
| Ҡ ҡ       | U+04A0, U+04A1 | Cyrillic Letter Bashkir Ka        |
| Ҳ ҳ       | U+04B2, U+04B3 | Cyrillic Letter Ha with Descender |
| Һ һ       | U+04BA, U+04BB | Cyrillic Letter Shha              |
| Ӏ ӏ       | U+04C0, U+04CF | Cyrillic Letter Palochka          |

> **Note on Palochka**: Often substituted with digit `1`, Latin `I`/`i`, lowercase `l`, vertical bar `|`, or slash `/` due to absence from standard Russian keyboards — a practice dating to Soviet typewriters. Corpora, dictionaries, and datasets should normalize these to the canonical Unicode characters U+04C0 (capital) and U+04CF (lowercase).

### Extended Notation

Beyond the core alphabet, extended orthographic notation includes:

- **Acute accent** (stress marking): **а́**, **ә́**, **е́**, **и́**, **о́**, **у́**
- **Tense fricatives** (phonemic status uncertain): **сс** /sː/, **хх** /χː/, **ҳҳ** /xː/, **шш** /ʃː/
- **Marginal sounds** (onomatopoeia): **ву** /w/, **гҳ** /ɣ/, **пв** /ɸ/
- **Dialectal sounds**: **гӏ** /ʡ/, **хӏ** /ħ/, **ю** /uˤ/
- **Russian letters** (unassimilated loanwords and proper nouns): **ё**, **ф**, **щ**, **ъ**, **ы**, **ь**, **э**, **ю**, **я**

## Typing

Input methods are based on the standard Russian ЙЦУКЕН layout to minimize disruption to Russian keyboard users' muscle memory. A frequency-optimized layout is deferred until the corpus matures.

**Language identifiers**:

- **English**: Kaitag
- **Russian**: Кайтагский
- **Kaitag**: Хайдаҡӏла
- **ISO 639-3**: `xdq`

### Mobile

Available for **Google Gboard** ([Google Play](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)), **Yandex Keyboard** ([Google Play](https://play.google.com/store/apps/details?id=ru.yandex.androidkeyboard), [App Store](https://apps.apple.com/app/andeks-klaviatura/id1053139327)), and **HeliBoard** ([GitHub](https://github.com/Helium314/HeliBoard/releases/latest)).

#### 3-row

Replaces six of seven excluded Russian letters: `щ` → `ӏ`, `ф` → `ҡ`, `ы` → `һ`, `э` → `ҳ`, `ь` → `ә`, `ю` → `ғ`. `я` keeps its slot as the most frequent of the excluded set. Placement reflects character frequency (see [characters.csv](corpus/characters.csv)).

```
й ц у к е н г ш ӏ з х
ҡ һ в а п р о л д ж ҳ
  я ч с м и т ә б ғ
```

Accented vowels for stress marking and excluded Russian letters are accessible via long-press:

```
у: ю у́
е: э е́ ё
ш: щ
ӏ: ъ
һ: ь
а: я а́
п: ф
о: о́
и: ы и́
ә: ә́
```

#### 4-row

Leaves the Russian ЙЦУКЕН intact and adds new keys above:

```
' ! ? ғ ҡ һ ӏ ә ҳ — "
й ц у к е н г ш щ з х
ф ы в а п р о л д ж э
  я ч с м и т ь б ю
```

_Replace `'` and `"` with `,` and `.` if your keyboard lacks them around the spacebar._

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

The script requires six additional characters compared to standard Russian, plus a combining acute for stress marking. Compose key sequences enter these without switching layouts.

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

- **[Kaitag Dictionary](https://urssivar.com/language/dictionary/)**: 5,000+ lexemes with usage examples, notes, and cross-references ([source](https://github.com/urssivar/dictionary)).
- **[Reference corpus](corpus/monocorpus.txt)**: 33,615 characters extracted from Gasanova[^3].
- **[Unicode exemplar data](https://github.com/googlefonts/lang/blob/main/Lib/gflanguages/data/languages/xdq_Cyrl.textproto)**: Base, auxiliary, marks.

### Tools

- **[Yaziv](https://yaziv.raxys.app/xdq?from=cyr_soviet&to=cyr&text=цакъкъа+г1ябал+къабагъ)**: Transliteration between Kaitag Cyrillic and IPA representations.
  - Current orthography: "Cyrillic"
  - Legacy support: "Cyrillic (2024)", "Soviet Cyrillic"
- **[Google Fonts](https://fonts.google.com/?preview.size=24&lang=xdq_Cyrl)**: Web font service and library.

### References

- **[ParaType](https://paratype.github.io/cyrillic-languages/index.html?lang=Kaitag&group=cyrillic&ui=en&pg=2)**: Cyrillic typography resource.
- **[Ethnologue](https://www.ethnologue.com/language/xdq/)**: Global language database.
- **[Omniglot](https://www.omniglot.com/writing/kaitag.htm)**: Encyclopedia of writing systems and languages.
- **[Minority Languages of Russia](https://minlang.iling-ran.ru/lang/kaytagskiy-yazyk)**: Institute of Linguistics, Russian Academy of Sciences.

## Version History

**v1.2 (May 2026)**: Introduced two extended Cyrillic characters **Әә** and **Һһ** to replace **Яя** and **Ьь**, removing the friction of reading these Russian letters with non-Russian sound values. The palochka **Ӏӏ** also serves as a standalone letter for /ʔ/, replacing **Ъъ**.

**v1.1 (January 2026)**: Adopted the palochka **Ӏӏ** as ejective marker, aligning with North Caucasian orthographic tradition. Added extended notation for stress marking and tense fricatives.

**v1.0 (February 2024)**: Initial release introducing extended Cyrillic characters **Ғғ**, **Ҡҡ**, and **Ҳҳ**, uniform consonant series representation, and explicit iotation. Used soft sign **Ьь** as dual marker for both /h/ and ejectivity.

## License

Licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). For questions or contributions, contact <alkaitagi@outlook.com>. If you use this specification or data in your work, please cite:

> Magomedov, M. (2026). _Kaitag Cyrillic Script_. Retrieved from <https://github.com/urssivar/script>

[^1]: Темирбулатова, С.М. (2006). _Хайдакский диалект даргинского языка_. Диссертация на соискание учёной степени доктора филологических наук. Махачкала.

[^2]: Гасанова, У.У. (2012). _Лексика и словообразование хайдакского диалекта даргинского языка_. Диссертация на соискание учёной степени доктора филологических наук. Махачкала.

[^3]: Гасанова, У.У. (2013). _Хайдакьла хабарти_ (Хайдакские сказки). Махачкала, 152 с. Составитель: Гасанова У.У. Редактор: Сивриди Г.Н.
