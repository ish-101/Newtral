# HOW TO USE
# print(cnn_link_to_text.parse("https://www.cnn.com/2019/11/09/politics/whistleblower-ukraine-attorney-gop-witness-requests-trump-impeachment-inquiry/index.html"))

import requests
from bs4 import BeautifulSoup

PARSER = "html.parser"

def cnn_parse(url):
    request = requests.get(url=url)
    doc = request.text
    soup_doc = BeautifulSoup(doc, PARSER)
    paragraphs = soup_doc.find('div', {"itemprop": "articleBody"})
    string = ""
    for paragraph in paragraphs:
        string += paragraph.text + "\n"
    return string