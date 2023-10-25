# NAVER-translator

translator is a python package that uses the translation function of the Naver search bar. Please refrain from excessive use. 


## Installation

To install the NAVER-Translator library, you can use pip:

```bash
pip install navertrans
```

or

```bash
git clone 
```

## List of languages ​​available for translation

|language|language code|
|-------|--------|
|Russian | 'ru'|
|Portuguese | 'pt'|
|Japanese | 'ja'|
|Italian | 'it'|
|Vietnamese | 'vi'|
|Thai | 'th'|
|Spanish | 'es'|
|French | 'fr'|
|Hindi | 'hi'|
|German | 'de'|
|Simplified Chinese | 'zh-CN' (中文 (简体))|
|Traditional Chinese | 'zh-TW' (中文 (繁體))|

You can use these language codes when specifying the source and destination languages for translation in your NAVER-Translator project.

### 예시
'''
from navertrans import navertrans

src_txt = 'Please give a round of applause to NAVER.'
result = navertrans.translate(src_txt, src_lan="en", tar_lan= "ko")

print(result)  # Output: '네이버에게 박수 부탁드립니다.'
'''

In this example, src_txt contains the text you want to translate, and the translate function is called with the default source ('en') and target ('ko') languages. The translated text is stored in the result variable, and it is printed to the console.