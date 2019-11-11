#Source for NLTK: http://www.nltk.org/howto/sentiment.html
#Source for TextBlob: https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
#Source for classes: https://www.w3schools.com/python/python_classes.asp
#Source for lists: https://www.daniweb.com/programming/software-development/code/216631/a-list-of-class-objects-python

#Stuff imported to prevent errors
import nltk
nltk.downloader.download('vader_lexicon')
nltk.download('punkt')

#Import TextBlob
from textblob import TextBlob

import sentence_info

def anaylze(sentences):

    data = []

    #For each sentence
    for sentence in sentences:

        #Check if break
        if (sentence.isBreak == False):
            #Get TextBlob data
            testimonial = TextBlob(sentence.sentence)
            #Get subjectivity score
            sentence.score = testimonial.sentiment.subjectivity

    return sentences