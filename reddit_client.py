import requests


class RedditClient:

    def __init__(self, subreddit):
        self.subreddit = subreddit

    def get_subreddit(self):
        '''Returns JSON results for the instance's subreddit GET request'''

        subreddit_url = 'https://www.reddit.com/r/{0}.json?limit=100'.format(self.subreddit)
        response = requests.get(subreddit_url)
        response.raise_for_status()
        return response.json()
