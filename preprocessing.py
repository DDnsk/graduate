# coding=utf-8
__author__ = 'nsk'
import re

from bs4 import BeautifulSoup


def load_file(file_path):
    return open(file_path, 'r')

def process(file_input):
    """
    to extract article and some other message about the article through html format

    including: title, author, highlight(exclusive in papers from ScienceDirect, might be useful in the future), date,
    abstract, keywords, and full text

    :param file_input: file object generated by load_file module
    :return a: dictionary containing what is extracted
    """

    a = {}
    soup = BeautifulSoup(file_input.read(), 'html5lib')
    a['article_title'] = soup.title.string.strip()
    full_text = []
    index = -1
    for item in soup.find_all('div', id=re.compile('frag_(\d)+')):
        for tag_sec in item.find_all():
            if tag_sec.name == 'h2':
                index += 1
                full_text.append({'title': tag_sec.string, 'content': ''})
            if tag_sec.name == 'p':
                full_text[index]['content'] += '''%%%'''
                for tmp in tag_sec.stripped_strings:
                    full_text[index]['content'] += tmp
    for dic in full_text:
        print dic['title']
        print dic['content']



    return a

def write_to_file():
    return

def main():
    file_path = 'article_done/article_0.html'
    process(load_file(file_path))

if __name__ == '__main__':
    main()
