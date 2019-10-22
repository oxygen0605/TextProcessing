# -*- coding: utf-8 -*-
import os
import urllib.request
from collections import Counter
import re
from gensim import corpora

class StopwordRemover(object):
    def __init__(self):
        self.stopwords_dic = set()
        self.stopwords_text = set()
        self.common_words = set()
        self.rare_words = set()

    def get_stopwords_in_files(self):
        """
         get
        """
        return self.stopwords_dic

    def get_stopwords_in_text(self):
        """
        """
        return self.stopwords_text

    def maybe_download(self, path):
        """
         Download the file from `url` and save it locally under `file_name`
        """
        url = 'http://svn.sourceforge.jp/svnroot/slothlib/ \
        CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
        if os.path.exists(path):
            print('File already exists.')
        else:
            print('Downloading...')
            urllib.request.urlretrieve(url, path)

    def create_dictionary(self, texts):
        """
        """
        dictionary = corpora.Dictionary(texts)
        return dictionary

    def remove_stopwords(self, words):
        """
        """
        words = [word for word in words if word not in self.stopwords_dic]
        words = [word for word in words if word not in self.stopwords_text]
        return words

    def remove_noisewords(self, words):
        """
        """
        words = [re.sub(r'[ !"#$%&\'\(\)=~|\-^\`+*;:\<\>?_\,\\.\/縲彎', '', word) for word in words]
        words = [word for word in words if word not in ""]
        return words

    def most_common(self, docs, n=100):
        """
        """
        fdist = Counter()
        for doc in docs:
            for word in doc:
                fdist[word] += 1
        self.common_words = {word for word, freq in fdist.most_common(n)}
        print('{}/{}'.format(n, len(fdist)))
        return self.common_words

    def find_stopwords(self, docs, n=100, min_freq=1):
        """
        """
        fdist = Counter()
        for doc in docs:
            for word in doc:
                fdist[word] += 1
        self.common_words = {word for word, freq in fdist.most_common(n)}
        self.rare_words = {word for word, freq in fdist.items() if freq <= min_freq}
        self.stopwords_text = self.common_words.union(self.rare_words)
        print('{}/{}'.format(len(self.stopwords_text), len(fdist)))

    def load_stopword_file(self, fpath, enc='utf-8'):
        """
        """
        fileobj = open(fpath, "r", encoding=enc)
        stopwords_str = fileobj.read()
        fileobj.close()

        stopwords_list = stopwords_str.splitlines()
        for st in stopwords_list:
            self.stopwords_dic.add(st)

    def output(self, words, fpath="output_words_removed_stopwords.txt", enc="utf_8"):
        """
        """
        fileobj = open(fpath, "w", encoding=enc)
        for w in words:
            fileobj.write(w)
            fileobj.write(",")
        fileobj.close()


if __name__ == "__main__":
    st = StopwordRemover()
    st.load_stopword_file("./slothlib/stopwords.txt")
    st.load_stopword_file("./slothlib/stopwords_extend.txt")