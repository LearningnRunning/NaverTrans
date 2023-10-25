# -*- coding: utf-8 -*-
from collections import namedtuple

_checked = namedtuple('Checked', ['result', 'original', 'version', 'srcLangType', 'tarLangType', 'words', 'time', 'translatedText'])

class Checked(_checked):
    def __new__(cls, result=False, original='', version='', srcLangType='', tarLangType='', words=None, time=0.0, translatedText=''):
        if words is None:
            words = []
        return super(Checked, cls).__new__(
            cls, result, original, version, srcLangType, tarLangType, words, time, translatedText)

    def as_dict(self):
        d = {
            'result': self.result,
            'original': self.original,
            'version': self.version,
            'srcLangType': self.srcLangType,
            'tarLangType': self.tarLangType,
            'words': self.words,
            'time': self.time,
            'translatedText': self.translatedText,
        }
        return d

    def only_checked(self):
        return self.original
