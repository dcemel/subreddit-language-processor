from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from training_data import training_recipes

cl = NaiveBayesClassifier(training_recipes)

def classify_posts(posts, food_type):
    classified_posts = []
    for post in posts:
        title = post['data']['title'].lower()
        blob = TextBlob(title, classifier=cl)
        # print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        # print blob
        # print blob.classify()
        # print post['data']['score']
        post['classification'] = blob.classify()
        classified_posts.append(post)
        # print '##################################'

    return classified_posts
