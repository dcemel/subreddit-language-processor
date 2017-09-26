import sys
import json
from reddit_client import RedditClient
from language_processor import classify_posts


def display_list(subreddit, food_type):
    '''
    Method invoked from the command line, receives name of a subreddit and name
    of a food_type classification, will invoke the get_subreddit, classify_posts
    and post_sort methods to return posts data of the food_type classification
    sorted by reddit score
    '''
    client = RedditClient(subreddit)
    subreddit = client.get_subreddit()

    posts = subreddit.get('data').get('children')

    classified_posts = classify_posts(posts, food_type)

    for post in classified_posts:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(food_type)
        print(post.get('class_score'))
        print(post.get('data').get('score'))
        print(post.get('data').get('title'))
        print(post.get('data').get('selftext'))

    print('TOTAL POSTS:')
    print(len(posts))

    print('TOTAL CLASS POSTS:')
    print(len(classified_posts))
    # else:
    #     print(subreddit.get('message'))

display_list(sys.argv[1:][0], sys.argv[1:][1])
