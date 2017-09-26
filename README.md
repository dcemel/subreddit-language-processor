# Subreddit Language Processor

Retrieves, enriches, and sorts a given subreddit's posts data using the Naive Bayes algorithm to classify content.

## Getting Started

Install the python requirements:

`$pip install -r requirements.txt`

Download the textblob corpora libraries:

`$python -m textblob.download_corpora`

Configure the machine learning training data set in training_data.py

Invoke the command link script with arguments:

`$python script.py {name of subreddit} {name of classification}`

Examples:

`$python script.py Cooking vegetable`

`$python script.py recipes seafood`

`$python script.py Foodie dessert`

## Run the tests

`pytest test.py -vv`
