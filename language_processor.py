from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from training_data import training_recipes

cl = NaiveBayesClassifier(training_recipes)

def classify_posts(posts, food_type):
    '''
    Filters a list of posts based on matching relevant food type
    classification and enriches the data by adding the expected
    relevance_score
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

        # Classify the post title and keep tally for
        # food classification relevance
        classifications[title_blob.classify()] += 1

        # Classify each sentence of the post content and keep tally
        # food classification relevance
        for sentence in content_blob.sentences:
            classifications[sentence.classify()] += 1

        # Add the post with the tally for the corresponding classification
        # to the result list if the highest food classification relevance
        # is the selected food_type
        if max(classifications, key=classifications.get) == food_type:
            post['relevance_score'] = classifications.get(food_type)
            classified_posts.append(post)

    return classified_posts


def sort_classified_posts(posts):
    '''
    Sorts classified posts by food classification relevance score and
    then reddit score
    '''
    less = []
    pivot_list = []
    more = []
    if len(posts) <= 1:
        return posts
    else:
        pivot = posts[0]
        for post in posts:
            if post.get('relevance_score') < pivot.get('relevance_score'):
                less.append(post)
            elif post.get('relevance_score') > pivot.get('relevance_score'):
                more.append(post)
            elif post.get('data').get('score') < pivot.get('data').get('score'):
                less.append(post)
            elif post.get('data').get('score') > pivot.get('data').get('score'):
                more.append(post)
            else:
                pivot_list.append(post)
        less = sort_classified_posts(less)
        more = sort_classified_posts(more)
        # Ascending
        return less + pivot_list + more
        # Descending
        # return more + pivot_list + less
