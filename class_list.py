# coding=utf-8
__author__ = 'Dnsk'

class paragraph():
    """

    """
    title_of_part = ''
    part_index = 0
    index_in_part = 0

    # contains sentence instances that in this paragraph
    sentence_containing = []

class sentence():
    """

    """
    index_in_paragraph = 0
    original_sentence = ''
    tf_isf = {}
    def sentence_length(self):
        return len(self.tf_isf)

if __name__ == '__main__':
    para_1 = paragraph()
    para_1.title_of_part = 'Introduction'
    sen_1 = sentence()
    sen_1.original_sentence = 'Hello World!'
    sen_2 = sentence()
    sen_2.original_sentence = 'Hello World2'
    para_1.sentence_containing.append(sen_1)
    para_1.sentence_containing.append(sen_2)
    print para_1.sentence_containing[0].original_sentence
    print para_1.sentence_containing[1].original_sentence