# -*- coding: utf-8 -*-
from collections import namedtuple

_checked = namedtuple('Checked',
    ['result', 'original', 'version', 'srcLangType', 'tarLangType', 'words', 'time'])

class Checked(_checked):
    def __new__(cls, result=False, original='', version='', srcLangType='', tarLangType='', words=None, time=0.0):
        if words is None:
            words = []
        return super(Checked, cls).__new__(
            cls, result, original, version, srcLangType, tarLangType, words, time)

    def as_dict(self):
        d = {
            'result': self.result,
            'original': self.original,
            'version': self.version,
            'srcLangType': self.srcLangType,
            'tarLangType': self.tarLangType,
            'words': self.words,
            'time': self.time,
        }
        return d

    def only_checked(self):
        return self.original

