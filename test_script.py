import os   # this is for travis only
import matplotlib as mpl # this is for travis only
from autonomio.commands import data, train

if os.environ.get('DISPLAY','') == '': # this is for travis only
    print('no display found. Using non-interactive Agg backend') # this is for travis only
    mpl.use('Agg') # this is for travis only

tweets = data('random_tweets')
tr = train('text','neg',tweets.head(5000))
