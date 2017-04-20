# graduate
Project for graduation design


Structure of the Article instance.
  Article
    Part1
      Paragraph1
        Sentence1
        Sentence2
      Paragraph2
        Sentence1
        Sentence2
        Sentence3
    Part2
      ...


Class design in detail

  There are 5 classes: Article, Part, Paragraph, Sentence, Ref.

  Article(class)
    attributes
      title_main: string, the title of the article
      part_list: list, parts(classes) in the article
    methods
      __init__(): nothing to say
      display(): print contents in this class, for debuging
      sentence_word_split(): split sentences(with 'original sentence'attr) into words, storing in the Sentence.word_split_list
  
  Part(class)
    attributes
      title_part: string, the title of the part(eg. 'Introduction', 'Background')
      index_in_article: int, index of the part in the article
      paragraph_list: list, paragraphs in this part
      ref_list: list, references in certain part
      isNormal: int, 1 for normal part(eg. Introduction), 0 for otherwise(eg. References or Keyword)
    methods
      __init__(): nothing to say
  
  Paragraph(class)
    attributes
      index_in_part: int, index of the paragraph in this part
      sentence_containing: list, sentences in this paragraph
    methods
      __init__(): nothing to say
  
  Sentence(class)
    attributes
      index_in_paragraph: int, index of the sentence in this paragraph
      original_sentence: string, sentence without any further process
      tf_isf: dict, tf*isf for this sentence
      word_split_list: list, words in this sentence
    methods
      sentence_length(): return int, the length of this sentence
      word_split(): split word, saving resules to word_split_list
  
  Ref(class)
    attributes
      index_ref: int, index of reference
      content: string, content of the piece of reference
    methods
      __init__(): nothing to say
    ***further process: extract more information from the content, such as author, year and source 
    
      
      
