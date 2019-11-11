# HOW TO USE
# print(fox_link_to_text.parse("https://www.foxnews.com/politics/trump-brushes-off-witch-hunt-impeachment-probe"))

import requests
from bs4 import BeautifulSoup

PARSER = "html.parser"

def fox_parse(url):
    request = requests.get(url=url)
    doc = request.text
    soup_doc = BeautifulSoup(doc, PARSER)
    paragraphs = soup_doc.find('div', {"class": "article-body"}).find_all('p')
    string = ""
    for paragraph in paragraphs:
        string += paragraph.text + "\n"
    return string
