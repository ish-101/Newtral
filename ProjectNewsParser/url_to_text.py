#HOW TO USE
#print(link_to_base_url(https://www.bbc.com/news/world-us-canada-50323607))
from urllib.parse import urlparse
from bbc_link_to_text import bbc_parse
from cnn_link_to_text import cnn_parse
from fox_link_to_text import fox_parse
from nyt_link_to_text import nyt_parse

def get_text(url): # takes in news article URL, returns text from the article
    base_url = (urlparse(url)[1]) # parses news article URL, saves base URL

    if base_url == "www.bbc.com": # calls different web parsers depending on news website
        return bbc_parse(url)
    if base_url == "www.cnn.com":
        return cnn_parse(url)
    if base_url == "www.foxnews.com":
        return fox_parse(url)
    if base_url == "www.nytimes.com":
        return nyt_parse(url)