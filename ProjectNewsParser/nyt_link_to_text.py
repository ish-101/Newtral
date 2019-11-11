# HOW TO USE
# print(nyt_link_to_text.parse("https://www.nytimes.com/2019/11/09/world/berlin-wall-photos-30-year-anniversary.html"))

import requests
from bs4 import BeautifulSoup

PARSER = "html.parser"

def nyt_parse(url):
    request = requests.get(url=url)
    doc = request.text
    soup_doc = BeautifulSoup(doc, PARSER)
    paragraphs = soup_doc.find('section', {"itemprop": "articleBody"}).find_all('p')
    string = ""
    for paragraph in paragraphs:
        string += paragraph.text + "\n"
    return string