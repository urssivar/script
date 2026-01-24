# Kaitag Script

## Alphabet

Letters (42):

> а б в г ғ д е ж з и й к кк кӏ ҡ ҡҡ ҡӏ л м н о п пп пӏ р с т тт тӏ у х ҳ ц цц цӏ ч чч чӏ ш ъ ь я

Characters (31):

> а б в г ғ д е ж з и й к ҡ л м н о п р с т у х ҳ ц ч ш ъ ь я ӏ

## Input

The current input methods are based on the standard Russian ЙЦУКЕН and aim to do the least amout of disruption to the muscle memory of Russian keyboard users. In the future with larger corpus a special Kaitag layout could be developed that fully takes into account the character frequences and other metrics.

## Mobile Input

The layout replaces five keys for the excluded Russian letters **Щ**, **Ф**, **Ы**, **Э**, **Ю** with the characters **Ҡ**, **Ҳ**, **Ғ**, **Ъ**, **Ӏ**. The characters are placed according to their frequencies, with the more frequent ones brought closer to the center.

```
й ц у к е н г ш ҡ з х
ҳ ғ в а п р о л д ж ъ
  я ч с м и т ь б ӏ
```

The accented vowels for stress and the excluded Russian letters are available via long-press:

- у: ю у́
- е: э е́ ё
- ш: щ
- а: а́
- п: ф
- о: о́
- я: я́
- и: ы и́

Implemented in **Google Gboard** ([Google Play](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin)), **Yandex Keyboard** ([Google Play](https://play.google.com/store/apps/details?id=ru.yandex.androidkeyboard), [AppStore](https://apps.apple.com/app/andeks-klaviatura/id1053139327)), and [**Heliboard**](https://github.com/Helium314/HeliBoard).

## Desktop Input

With only four addintional symbols compared to the standard Russian set, the compose input seems more convenient than whole layout switching.

The config for [**WinCompose**](https://github.com/samhocevar/wincompose) on Windows:

```
<Multi_key> <Г> : "Ғ"
<Multi_key> <г> : "ғ"
<Multi_key> <К> : "Ҡ"
<Multi_key> <к> : "ҡ"
<Multi_key> <Х> : "Ҳ"
<Multi_key> <х> : "ҳ"
<Multi_key> <!> : "Ӏ"
<Multi_key> <1> : "ӏ"
```

Linux has this functionality built-in and for MacOS [**macos-compose**](https://github.com/Granitosaurus/macos-compose) is available.

## Naming

- Rus: кайтагский
- Eng: Kaitag
- Xdq: Хайдаҡӏла
