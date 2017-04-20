# coding=utf-8
__author__ = 'Dnsk'
import re
import nltk

class Article:
    """

    """
    def __init__(self, title):
        self.title_main = title
        self.part_list = []

    def display(self):
        for part in self.part_list:
            # just display normal part of the article
            if part.isNormal == 0:
                continue

            print part.title_part

            if part.title_part == 'References':
                for ref in part.ref_list:
                    print ref.content
                continue

            for paragraph in part.paragraph_list:
                for sentence in paragraph.sentence_containing:
                    print sentence.original_sentence.encode('GB18030')
                    print sentence.word_split_list
            print '\n'

    def sentence_word_split(self):
        for part in [normalpart for normalpart in self.part_list if normalpart.isNormal == 1]:
            for paragraph in part.paragraph_list:
                for sentence in paragraph.sentence_containing:
                    sentence.word_split()

class Part:
    """

    """
    def __init__(self):
        self.title_part = ''
        self.index_in_article = 0
        self.paragraph_list = []
        self.ref_list = []
        self.isNormal = 1

class Paragraph:
    """

    """
    def __init__(self):
        self.index_in_part = 0
        # contains sentence instances that in this paragraph
        self.sentence_containing = []

class Sentence:
    """

    """
    def __init__(self):
        self.index_in_paragraph = 0
        self.original_sentence = ''
        self.tf_isf = {}
        self.word_split_list = []

    def sentence_length(self):
        return len(self.tf_isf)

    def word_split(self):
        self.word_split_list = re.split(r'\s+', self.original_sentence)


class Ref:
    """

    """
    def __init__(self):
        self.index_ref = 0
        self.content = ''

if __name__ == '__main__':
    print 'hello there'
