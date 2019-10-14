# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup

class TextCleaner(object):
    def __init__(self):
        pass
        
    def remove_header(self,text):
         # skip header by [2:]
        replaced_text = '\n'.join(s.strip() for s in text.splitlines()[2:] if s != '') 
        return replaced_text
    
    def clean_text(self,text):
        replaced_text = text.lower()
        replaced_text = re.sub(r'[【】]', ' ', replaced_text)       # 【】の除去
        replaced_text = re.sub(r'[（）()]', ' ', replaced_text)     # （）の除去
        replaced_text = re.sub(r'[{}]', ' ', replaced_text)      # {}の除去
        replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)   # ［］の除去
        replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
        replaced_text = re.sub(r'https?:\/\/.*?[\r\n ]', '', replaced_text)  # URLの除去
        replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
        return replaced_text
    
    def clean_html_tags(self,html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        cleaned_text = soup.get_text()
        cleaned_text = ''.join(cleaned_text.splitlines())
        return cleaned_text
    
    def clean_html_and_js_tags(self,html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        [x.extract() for x in soup.findAll(['script', 'style'])]
        cleaned_text = soup.get_text()
        cleaned_text = ''.join(cleaned_text.splitlines())
        return cleaned_text
    
    def clean_url(self,html_text):
        """
        \S+ matches all non-whitespace characters (the end of the url)
        :param html_text:
        :return:
        """
        cleaned_text = re.sub(r'http\S+', '', html_text)
        return cleaned_text
    
    def clean_code(self,html_text):
        """Qiitaのコードを取り除きます
        :param html_text:
        :return:
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        [x.extract() for x in soup.findAll(class_="code-frame")]
        cleaned_text = soup.get_text()
        cleaned_text = ''.join(cleaned_text.splitlines())
        return cleaned_text
    
    def output(self, text, fpath="output_cleaned_text.txt", enc="utf_8"):
        fileobj = open(fpath, "w",encoding=enc)
        fileobj.write(text)
        fileobj.close()