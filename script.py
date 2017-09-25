import sys
from reddit_client import RedditClient
from language_processor import classify_posts


def display_list(subreddit):
    '''
    Method invoked from the command line, receives name of a subreddit and name
    of a food_type classification, will invoke the get_subreddit, classify_posts
    and post_sort methods to return posts data of the food_type classification
    sorted by reddit score
    '''
    client = RedditClient(subreddit)
    subreddit = client.get_subreddit()
    try:
        posts = subreddit['data']['children']

        classified_posts = classify_posts(posts)

        for post in classified_posts:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!')
            print(post['classification'])
            print(post['data']['score'])
            print(post['data']['title'])

    except KeyError as e:
        print('Error accessing the Reddit API')
        print(subreddit['message'])

display_list(sys.argv[1:][0])
