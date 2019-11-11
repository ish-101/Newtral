from storage_data import storage_data
from url_to_text import get_text
import storage
import text_to_sentences
import sentiment_analyzer

articles = ["https://www.bbc.com/news/world-us-canada-50323607", # array of article urls to populate database
            "https://www.bbc.com/news/world-europe-50013048",
            "https://www.bbc.com/news/world-europe-50361886",
            "https://www.bbc.com/news/world-asia-50359435",
            "https://www.bbc.com/news/business-50342714",
            "https://www.cnn.com/2019/11/07/opinions/pence-trump-ukraine-scandal-scapegoat-dantonio/index.html",
            "https://www.cnn.com/2019/11/08/politics/michael-bloomberg-analysis/index.html",
            "https://www.cnn.com/2019/10/14/business/target-cutting-hours-wage-increase/index.html",
            "https://www.cnn.com/2019/11/08/tech/facebook-whistleblower-name/index.html",
            "https://www.foxnews.com/opinion/david-bossie-trump-impeachment-witch-hunt-must-end-whistleblower-lawyer-is-trump-hater-who-forecast-coup",
            "https://www.foxnews.com/media/doug-schoen-michael-bloomberg-substantive",
            "https://www.foxnews.com/us/missing-california-hiker-found-dead-at-top-glacier-weeks-before-wife-gives-birth",
            "https://www.foxnews.com/world/berlin-wall-east-germans-stasi-answers",
            "https://www.foxnews.com/politics/aoc-bloomberg-purchase-election",
            "https://www.nytimes.com/2019/11/09/world/berlin-wall-photos-30-year-anniversary.html",
            "https://www.nytimes.com/2019/11/09/upshot/bloomberg-new-york-prosperity-inequality.html",
            "https://www.nytimes.com/2019/11/09/us/a-slave-rebellion-rises-again.html",
            "https://www.nytimes.com/2019/09/28/opinion/sunday/millennial-dining-car-amtrak.html",
            "https://www.nytimes.com/2019/11/09/science/seals-distemper.html"]

for url in articles:
    article = get_text(url) # change to array of article texts
    sentences = text_to_sentences.split(article) # split article into individual sentences
    analyzed = sentiment_analyzer.anaylze(sentences) # analyze each sentence

    analyzed[:] = [x.__dict__ for x in analyzed]
    db_obj = storage_data(url=url, sentences=analyzed).__dict__
    storage.store(url=url, db_obj=db_obj)

print("Boom! I'm done.")