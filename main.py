from news_extract import *
from news_nlp import *
from news_scrape import *
import time

# Welcome Messages and Introduction
print("Welkom. \nIn enkele seconden heb je toegang tot de laatste artikelen "
      "in de technology section van de New York Times. \nVerder zul je ook te weten komen, of het "
      "artikel positief of negatief is, en in hoevere de schrijver een vooroordeel heeft.")
print()

# Getting the user input; adding an element of personalization!
name = input("Voer je naam in om te starten: ")

# Console Display
print("Welkom " + name + "! \nJe zult nu toegang hebben tot de laatste artikelen van de New York Times...")
print("Hyperlinks van artikelen extraheren...")
time.sleep(2)
print("Hyperlinks van artikelen extraheren...")
print()
time.sleep(2)

# Gets all the latest URL's from the NY Times Technology Section. (see news_extract.py for more detail)
content_string = get_content_string(my_url)
starts, ends = find_occurrences(content_string)
url_list = get_all_urls(starts, ends, content_string)

# Gets the article summary and performs sentiment analysis on the chosen URL.
# For more information on how this works, visit news_scrape.py and news_nlp.py!
for url in url_list:
    print("Article URL: " + str(url))
    article_summary = summarize_article(url)
    find_sentiment(article_summary)
    print("------------------------------------------------")
    time.sleep(7)  # Allows user to get through all the text.

    # Closing Messages
print()
print("De artikelen zijn succesvol geëxtraheerd!")
print("In totaal hebben we " + str(len(url_list)) + " different articles!")
print("Bedankt voor je deelname, " + name + "!")


