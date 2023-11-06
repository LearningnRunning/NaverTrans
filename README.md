# NaverTrans

translator is a python package that uses the translation function of the Naver search bar. Please refrain from excessive use. 


## Installation

To install the NaverTrans library, you can use pip:

```bash
pip install navertrans
```

or

```bash
git clone https://github.com/LearningnRunning/NaverTrans.git

python setup.py install
```

## List of languages ​​available for translation

|language|language code|period separator|
|-------|--------|----------|
|Korean | 'ko'|.|
|English | 'en'|.|
|Russian | 'ru'|.|
|Portuguese | 'pt'|.|
|Japanese | 'ja'|。|
|Italian | 'it'|.|
|Vietnamese | 'vi'|.|
|Thai | 'th'|ครับ|
|Spanish | 'es'|.|
|French | 'fr'|.|
|Hindi | 'hi'|.|
|German | 'de'|.|
|Simplified Chinese | 'zh-CN' (中文 (简体))|。|
|Traditional Chinese | 'zh-TW' (中文 (繁體))|。|

You can use these language codes when specifying the source and destination languages for translation in your NaverTrans project.

## An example of using the navertrans library
```
from navertrans import navertrans

src_txt = 'Please give a round of applause to NAVER.'
result = navertrans.translate(src_txt, src_lan="en", tar_lan= "ko")

print(result)  # Output: '네이버에게 박수 부탁드립니다.'
```

In this example, src_txt contains the text you want to translate, and the translate function is called with the default source ('en') and target ('ko') languages. The translated text is stored in the result variable, and it is printed to the console.

## Referenced Repository
- [py-hanspell](https://github.com/ssut/py-hanspell) - A useful repository for [A Python package that checks and corrects the spelling of Korean characters.].

## License
navertrans is provided under the CC BY-NC 4.0 license. 

### Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)

Choose this license if you want to permit others to **_share_** (mirror) your mod content, providing that they credit you and don't use your work for commercial purposes.

You can view additional details on [this page](https://creativecommons.org/licenses/by-nc-nd/4.0/), which you should link to in your readme.

### Usage Guidelines
This library is built upon Naver Translator.

All copyright and responsibility for all results and data belong to NAVER Corp. The developer assumes no responsibility for any part of the library used for commercial purposes. Please be aware that the CC BY-NC 4.0 license restricts commercial usage, and you should respect the terms of this license.
