# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:19:55 2018
@author: oxygen0605
"""

import TextCleaner
import Tokenizer
import TextNormalizer
import StopwordRemover

if __name__ == "__main__":
    fileobj = open("sample.html", "r",encoding="utf_8")
    text = fileobj.read()
    fileobj.close()
    
    #形態素解析をしやすくするためのクリーニング
    tcleaner = TextCleaner.TextCleaner()
    text = tcleaner.remove_header(text)
    text = tcleaner.clean_html_and_js_tags(text)
    text = tcleaner.clean_url(text)
    text = tcleaner.clean_code(text)
    text = tcleaner.clean_text(text)
    tcleaner.output(text)
    
    tokenizer = Tokenizer.JanomeTokenizer()
    words = tokenizer.wakati(text)
    #words = tokenizer.filter_by_pos(text, pos=('名詞'))
    tokenizer.output(words)
    
    #MeCab
    #tokenizer = Tokenizer.MeCabTokenizer()
    #words = tokenizer.wakati(text)
    #words = tokenizer.filter_by_pos(text, pos=('名詞'))
    #tokenizer.output(words)
    
    tnormalizer = TextNormalizer.TextNormalizer()
    nwords = []
    for w in words:  
        nw = tnormalizer.normalize(w)
        nw = tnormalizer.lemmatize_term(nw,pos='v')    
        nwords.append(nw)
    tnormalizer.output(nwords)
    
    stw_remover = StopwordRemover.StopwordRemover()
    stw_remover.load_stopword_file("./slothlib/stopwords.txt")
    stw_remover.load_stopword_file("./slothlib/stopwords_extend.txt")
    stw_remover.find_stopwords(nwords)
    stwords = stw_remover.remove_stopwords(nwords)
    stwords = stw_remover.remove_noisewords(stwords)
    
    stw_remover.output(stwords)
    