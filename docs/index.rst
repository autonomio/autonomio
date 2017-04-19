========
SOMECODE
========

SOMECODE is a research platform for serious observation and analysis of Twitter data. SOMECODE brings together 9 years of unbroken continuity in developing social media research tools. Previous tools and processes developed by the contributor team are in daily use by many FORTUNE100 companies and major advertising agencies. SOMECODE is the solution we always wanted to build, but due to the kinds of restraints commercial entities have, never got to. ::

    pip install somecode

All you need to have is Python 2.7 and the somecode installation will take care of all the dependencies. 


-----
TRAIN
-----

The absolute minimum use case using an Autonomio dataset is:: 

    from autonomio.commands import *
    %matplotlib inline
    train('text','neg',data('random_tweets'))



+-------------------+-------------------------+-------------------------+
|                   |                         |                         |
| ARGUMENT          | REQUIRED INPUT          | DEFAULT                 |
+===================+=========================+=========================+
| X                 | string, int, float      | NA                      |
+-------------------+-------------------------+-------------------------+
| Y                 | int,float,categorical   | NA                      |
+-------------------+-------------------------+-------------------------+
| data              | data object             | NA                      |
+-------------------+-------------------------+-------------------------+
| epoch             | int                     | 5                       |
+-------------------+-------------------------+-------------------------+
| flatten           | string, float           | 'mean'                  |
+-------------------+-------------------------+-------------------------+
| dropout           | float                   | .2                      |
+-------------------+-------------------------+-------------------------+
| layers            | int (2 through 5        | 3                       |
+-------------------+-------------------------+-------------------------+
| model             | int                     | 'train' (OBSOLETE)      |
+-------------------+-------------------------+-------------------------+
| loss              | int                     | 'binary_crossentropy'   |
+-------------------+-------------------------+-------------------------+
| save_model        | string, int, float      | False                   |
+-------------------+-------------------------+-------------------------+
| neuron_first      | int,float,categorical   | 300                     |
+-------------------+-------------------------+-------------------------+
| neuron_last       | data object             | 1                       |
+-------------------+-------------------------+-------------------------+
| batch_size        | int                     | 10                      |
+-------------------+-------------------------+-------------------------+
| verbose           | 0,1,2                   | 0                       |
+-------------------+-------------------------+-------------------------+


Note that the network shape is roughly an upside-down pyramind. To change this you would want to change the code in train_new.py.




def train(X,Y,data,
			dims=300,
			epoch=5,
			flatten='mean',
       		dropout=.2,
       		layers=3,
       		model='train',
       		loss='binary_crossentropy',
       		save_model=False,
       		neuron_first='auto',
       		neuron_last=1,
       		batch_size=10,
       		verbose=0):


----
TEST
----


----
DATA
----

    'election_in_twitter'      
     Dataset consisting of 10 minute samples of 80 million tweets
    
    'sites_category_and_vec'   
     4,000 sites with word vectors and 5 categories
    
    'programmatic_ad_fraud'    
     Data from both buy and sell side and over 10 other sources
    
    'parties_and_employment'   
     9 years of monthly poll and unemployment numbers 
    
    'random_tweets'            
     20,000 tweets main intended for 
