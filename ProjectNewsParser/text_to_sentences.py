# HOW TO USE
# import text_to_sentences
# sentences = text_to_sentences.split(text)

import nltk.text
from sentence_info import sentence_info

nltk.download('punkt')


def split(text):
    array = []
    paragraphs = nltk.line_tokenize(text=text)
    for paragraph in paragraphs:
        sentences = nltk.sent_tokenize(text=paragraph)
        for sentence in sentences:
            array.append(sentence_info(sentence, False, 0))
        array.append(sentence_info("", True, 0))
    return array
