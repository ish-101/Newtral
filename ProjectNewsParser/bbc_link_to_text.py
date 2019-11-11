# HOW TO USE
# import bbc_link_to_text
# print(bbc_link_to_text.parse("https://www.bbc.com/news/world-us-canada-50323607"))

import requests
from bs4 import BeautifulSoup

PARSER = "html.parser"

def bbc_parse(url):
    request = requests.get(url=url)
    doc = request.text
    soup_doc = BeautifulSoup(doc, PARSER)
    paragraphs = soup_doc.find('div', {"property": "articleBody"}).find_all("p")
    string = ""
    for paragraph in paragraphs:
        string += paragraph.text + "\n"
    return string
