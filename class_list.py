# coding=utf-8
__author__ = 'Dnsk'

class Article:
    """

    """
    def __init__(self, title):
        self.title_main = title
        self.part_list = []

class Part:
    """

    """
    def __init__(self):
        self.title_part = ''
        self.index_in_article = 0
        self.paragraph_list = []


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

    def sentence_length(self):
        return len(self.tf_isf)


if __name__ == '__main__':
    para_1 = Paragraph()
    para_1.title_of_part = 'Introduction'
    sen_1 = Sentence()
    sen_1.original_sentence = 'Hello World!'
    sen_2 = Sentence()
    sen_2.original_sentence = 'Hello World2'
    para_1.sentence_containing.append(sen_1)
    para_1.sentence_containing.append(sen_2)
    print para_1.sentence_containing[0].original_sentence
    print para_1.sentence_containing[1].original_sentence
