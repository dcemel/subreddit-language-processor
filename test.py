import pytest
import httpretty
from requests import exceptions
from reddit_client import RedditClient
from language_processor import classify_posts, sort_classified_posts


def test_get_subreddit_success():
    '''Will request and return the JSON results for a given subreddit'''
    httpretty.enable()
    httpretty.register_uri(
        httpretty.GET,
        'https://www.reddit.com/r/a_test_subreddit.json?limit=100',
        body='{"test_response": "test results content"}'
    )

    reddit_client = RedditClient('a_test_subreddit')
    subreddit_response = reddit_client.get_subreddit()

    assert subreddit_response == {"test_response": "test results content"}


def test_get_subreddit_error_status():
    '''Will raise an HTTPError if the GET request returns an error status'''
    httpretty.enable()
    httpretty.register_uri(
        httpretty.GET,
        'https://www.reddit.com/r/a_test_error_subreddit.json?limit=100',
        status=429
    )

    reddit_client = RedditClient('a_test_error_subreddit')

    with pytest.raises(exceptions.HTTPError):
        subreddit_response = reddit_client.get_subreddit()


def test_classify_posts():
    posts = [
        {'data': {
            'title': 'green bean and mushroom medley',
            'selftext': 'sweet and sour brussel sprouts'
        }},
        {'data': {
            'title': 'butter tilapia',
            'selftext': 'shrimp quesadilla'
        }},
    ]

    expected = [{
        'data': {
            'title': 'green bean and mushroom medley',
            'selftext': 'sweet and sour brussel sprouts',
        },
        'relevance_score': 2
    }]

    assert classify_posts(posts, 'vegetable') == expected


def test_sort_classified_posts():
    unsorted_posts = [
        {'data': {'score': 50}, 'relevance_score': 2},
        {'data': {'score': 1},'relevance_score': 20},
        {'data': {'score': 10}, 'relevance_score': 2},
        {'data': {'score': 1}, 'relevance_score': 5},
    ]

    expected = [
        {'data': {'score': 10}, 'relevance_score': 2},
        {'data': {'score': 50}, 'relevance_score': 2},
        {'data': {'score': 1}, 'relevance_score': 5},
        {'data': {'score': 1},'relevance_score': 20},
    ]

    assert sort_classified_posts(unsorted_posts) == expected
