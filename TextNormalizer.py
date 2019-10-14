# -*- coding: utf-8 -*-

import re
import unicodedata

import nltk
from nltk.corpus import wordnet


class TextNormalizer(object):

    def normalize(self, text):
        normalized_text = self.normalize_unicode(text)
        normalized_text = self.normalize_number(normalized_text)
        normalized_text = self.lower_text(normalized_text)
        return normalized_text
    
    def lower_text(self, text):
        return text.lower()
    
    def normalize_unicode(self, text, form='NFKC'):
        normalized_text = unicodedata.normalize(form, text)
        return normalized_text
    
    def lemmatize_term(self, term, pos=None):
        if pos is None:
            synsets = wordnet.synsets(term)
            if not synsets:
                return term
            pos = synsets[0].pos()
            if pos == wordnet.ADJ_SAT:
                pos = wordnet.ADJ
        return nltk.WordNetLemmatizer().lemmatize(term, pos=pos)
    
    def normalize_number(self, text):
        # 連続した数字を0で置換 全角数字も/dだとマッチする
        replaced_text = re.sub(r'\d+', '0', text)
        return replaced_text
    
    def output(self, words, fpath="output_normalized_words.txt", enc="utf_8"):
        fileobj = open(fpath, "w",encoding=enc)
        for w in words:
            fileobj.write(w)
            fileobj.write(",")
        fileobj.close()