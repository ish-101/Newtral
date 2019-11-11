import bbc_link_to_text
import text_to_sentences
import sentiment_analyzer

text = bbc_link_to_text.bbc_parse("https://www.bbc.com/news/world-us-canada-50323607")
sentences = text_to_sentences.split(text)
analyzed = sentiment_analyzer.anaylze(sentences)

for x in analyzed:
     if not x.isBreak:
          print(str(x.score) + ": " + x.sentence)