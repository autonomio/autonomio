=============================
Autonomio v.0.1.1 User Manual
=============================

This document covers in detail every function of Autonomio. If you're looking for a high level overview of the capabilities, you might find [Autonomio_Overview]_ more useful. 

Autonomio is very easy to use and it's highly recommended to memorize the namespace which is less just 3 commands and less than 20 arguments combined. That's right, to have 100% control over Autonomio's powerful features, you just have to know three commands. 

- train (trains a model) 
- test (performs a test using a trained model)
- data (loads ready datasets)

-----
TRAIN
-----

The absolute minimum use case using an Autonomio dataset is:: 

    from autonomio.commands import *
    %matplotlib inline
    train('text','neg',data('random_tweets'))
    
Using this example and NLTK's sentiment analyzer as an input for the ground truth, Autonomio yields 85% prediction result out of the box with with nothing but:: 

    train('text','neg',data('random_tweets'))

A slightly more involving example may include changing the number of epochs::

    train('text','neg',data('random_tweets'),epoch=20)
    
For flattening the options are 'mean', 'median', 'none' and IQR. IQR is invoked by inputting a float::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3)
    
Dropout is one of the most important aspects of neural network::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,dropout=.5)
    
You might want to change the number of layers in the network:: 

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,dropouts=.5,layers=4)

Or change the loss of the model:: 

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,dropouts=.5,layers=4,loss='kullback_leibler_divergence')

For a complete list of supported losses see [Keras_Losses]_ 

If you want to save the model, be mindful of using .json ending::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,save_model='model.json')

Control the neuron size by setting the number of neurons on the input layer:: 

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,neuron_first=50)

Sometimes changing the batch size can improve the model significantly::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,batch_size=15)

By default verbosity from Keras is at mimimum, and you may want the live mode for training:: 

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,verbose=1)



TRAIN ARGUMENTS
---------------

Even though it's possible to use Autonomio mostly with few arguments, there are a total 11 arguments that can be used to improving model accuracy. 

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
| save_model        | string,                 | False                   |
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


----
TEST
----


----
DATA
----

Dataset consisting of 10 minute samples of 80 million tweets::

    data('election_in_twitter')

4,000 ad funded websites with word vectors and 5 categories::
   
    data('sites_category_and_vec')   

Data from both buy and sell side and over 10 other sources::
    
    data('programmatic_ad_fraud')    
    
9 years of monthly poll and unemployment numbers:: 
    
    data('parties_and_employment')   
  
120,000 tweets with sentiment classification from NLTK::
    
    data('tweet_sentiment')
    
20,000 random tweets::

    data('random_tweets')            
    
DATA ARGUMENTS
---------------

The data command is provided for both convinience, and to give the user access to unique deep learning datasets. In addition to allowing access to Autonomio datasets, the function also supports importing from csv, json, and excel. The data importing function is for most cases we face, but is not intended as a replacement to pandas read functions::

    def data(name,mode='default')

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

     
     
LINKS
-----

.. [Keras_Losses] https://keras.io/losses/
.. [Autonomio_Overview] https://github.com/botlabio/autonomio/blob/master/README.md
