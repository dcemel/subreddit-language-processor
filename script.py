import sys
import json
from reddit_client import RedditClient
from language_processor import classify_posts, sort_classified_posts


def display_list(subreddit, food_type):
    '''
    Method invoked from the command line, receives name of a subreddit and name
    of a food_type classification, will invoke the get_subreddit, classify_posts
    and sort_classified_posts methods to print sorted posts data matching the
    corresponding food_type classification
    '''
    client = RedditClient(subreddit)
    subreddit = client.get_subreddit()

    posts = subreddit.get('data').get('children')

    classified_posts = classify_posts(posts, food_type)

    sorted_posts = sort_classified_posts(classified_posts)

    for post in sorted_posts:
        print('##############################################')
        print(food_type)
        print('Relevance Score: {0}'.format(post.get('relevance_score')))
        print('Reddit Score:{0}'.format(post.get('data').get('score')))
        print('Post Title:')
        print(post.get('data').get('title'))
        # print(post.get('data').get('selftext'))
        print(post.get('data').get('permalink'))


display_list(sys.argv[1:][0], sys.argv[1:][1])
