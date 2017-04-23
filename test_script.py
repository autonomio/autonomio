from autonomio.commands import data, train
tweets = data('random_tweets')
tr = train('text','neg',tweets.head(5000))
