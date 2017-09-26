from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from training_data import training_recipes

cl = NaiveBayesClassifier(training_recipes)

def classify_posts(posts, food_type):
    '''
    Classify a list of subreddit post data and return a list of posts
    where the highest tally of food classification matches food type with
    the class_score
    '''
    classified_posts = []
    for post in posts:
        title = post.get('data').get('title').lower()
        content_text = post.get('data').get('selftext').lower()
        title_blob = TextBlob(title, classifier=cl)
        content_blob = TextBlob(content_text, classifier=cl)

        classifications = {
            'meat': 0,
            'vegetable': 0,
            'dessert': 0,
            'seafood': 0,
        }

        # Classify the post title and keep tally for the food type
        classifications[title_blob.classify()] += 1

        # Classify each sentence of the post content and keep tally
        for sentence in content_blob.sentences:
            classifications[sentence.classify()] += 1

        # Add the post with the tally for the corresponding classification
        # to the return list if the highest food classification tally is the
        # selected food_type
        if max(classifications, key=classifications.get) == food_type:
            post['class_score'] = classifications.get(food_type)
            classified_posts.append(post)

    return classified_posts
