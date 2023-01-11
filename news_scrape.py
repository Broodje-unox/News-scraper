from newspaper import Article
import nltk


# Summarizes the article and provides valuable information regarding the article metadata, including images and
# attributions.
def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()
    # Punkt is a sentence tokenizer which is useful for extracting and detecting text.
    article.download('punkt')
    article.nlp()

    # Gets the author or authors of the article
    author_string = "Author(s): "
    for author in article.authors:
        author_string += author  # adds all authors (if more than 1) to the author string.
    print(author_string)

    # Gets the publish date of the article
    date = article.publish_date

    # strftime() converts a tuple or struct_time representing a time to a string as specified by the format argument.
    # Here, it is used to mark the month, day, and year of the date in a readable format.
    date = article.publish_date
    print("publish Date " + str(date.strftime("%m/%d/%Y")))

    # Gets the top image of the article
    print("Top Image Url: " + str(article.top_image))

    # Gets the article images
    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image
    print(image_string)

    # Gets the article summary
    print("Een Beknopte Samenvatting")
    print("------------------------------------")
    print(article.summary)

    return article.summary

summarize_article('https://nos.nl/artikel/2459417-australische-kardinaal-pell-wiens-naam-verbonden-bleef-aan-misbruikschandaal-overleden')



