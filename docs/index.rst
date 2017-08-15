=============================
Autonomio v.0.3.2 User Manual
=============================

.. image:: https://travis-ci.org/autonomio/core-module.svg?branch=master
    :target: https://travis-ci.org/autonomio/core-module

.. image:: https://coveralls.io/repos/github/autonomio/core-module/badge.svg?branch=master
    :target: https://coveralls.io/github/autonomio/core-module?branch=master


.. image:: https://gemnasium.com/badges/github.com/mikkokotila/core-module.svg
    :target: https://gemnasium.com/github.com/mikkokotila/core-module


This document covers in detail functionality of Autonomio. If you're looking for a high level overview of the capabilities, you might find [Autonomio_Overview]_ more useful. 

Autonomio is very easy to use and it's highly recommended to memorize the namespace which is just 3 commands and less than 30 arguments combined. Yet you have an infinite number of network configurations available. To have 100% control over Autonomio's powerful features, you just have to know three commands. 

To train (and save) model::

    train()
    
To test (and load) model::

    test()
    
To load a dataset::

    data()

------------
INSTALLATION
------------ 

At the moment, the simplest way is to install with pip from the repo directly.

For installing the **development version** (latest):: 

    pip install git+https://github.com/autonomio/core-module.git

------------------------
TYPES OF NEURAL NETWORKS
------------------------

Currently Autonomio is focused on providing a very high level abstraction layer to training of 'dense' neural networks, and then using the trained models to make predictions in any environment that you see fit. Dense layers are suited for a wide range of data science problems.

-----------
DATA INPUTS
-----------

The expected input dataformat is a Pandas dataframe. Generally speaking, deep learning is at its strongest in solving classification problems, where the outcome variable is either binary categorical (0 or 1) or multi categorical. It's recommended to convert continuous and ranged variables to categoricals first. 

BINARY (default)
---------------

- X can be text, int, or floating point 
- Y can be an int, or floating point

The default settings are optimized for making a 1 or 0 prediction and for example in the case of predicting sentiment from tweets, Autonomio gives 85% accuracy without any parameter setting for classifying tweets that rank in the most negative 20% according to NLTK Vader sentiment analysis. 


CATEGORICAL
-----------

- X can be text, integer 
- Y can be an integer or text
- output layer neurons must match number of categories
- change activation_out to something that works with categoricals

It's not a good idea to have too many categories, maybe 10 is pushing it in most cases. 

-----
TRAIN
-----

The absolute minimum use case using an Autonomio dataset is:: 

    from autonomio.commands import *
    %matplotlib inline
    train('text','neg',data('random_tweets'))
    
Using this example and NLTK's sentiment analyzer as an input for the ground truth, Autonomio yields 85% prediction result out of the box with with nothing but:: 

    train('text','neg',data('random_tweets'))
    
There are multiple ways you can input 'x' with single input::

    train('text' ,'neg', data) # a single column where data is string

    train(5, 'neg', data) # a single column by index

    train(['quality_score'], 'neg', data) # a single column by label
    
And few more ways where you input a list for 'x'::

    train([1,5], 'neg', data) # a range of column index

    train(['quality_score', 'reach_score'], 'neg', data) # set of column labels

    train([1,2,4,6,18], 'neg', data) # a list of column index

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

You can add the shape in the model(the way how layers are distributed)::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,verbose=1, shape='brick')

To validate the result to check the test accuracy you may use the validation::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,validation=True)

The True for validation puts the half of the data to be trained, the other - tested.

You can also define which part of the data will be validated::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,validation=.4)

To be sure about the results which you have got you can use double check::

    train('text','neg',data('random_tweets'),epoch=20,flatten=.3,double_check=True)


TRAIN ARGUMENTS
---------------

Even though it's possible to use Autonomio mostly with few arguments, there are a total 13 arguments that can be used to improving model accuracy::

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
                verbose=0,
                shape='funnel',
                double_check=False,
                validation=False):

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
| loss              | string [Keras_Losses]_  | 'binary_crossentropy'   |
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
| shape             | string                  | 'funnel'                |
+-------------------+-------------------------+-------------------------+
| double_check      | True or False           | False                   |
+-------------------+-------------------------+-------------------------+
| validation        | True,False,float(0 to 1)| False                   |
+-------------------+-------------------------+-------------------------+

------
SHAPES
------


Funnel
------

Funnel is the shape, which is set by default. It roughly looks like an upside-dowm pyramind, so that the first layer is defined as neuron_max, and the next layers are sligtly decreased compared to previous ones.::


  \          /
   \        /
    \      /
     \    /
      |  |



Long Funnel
-----------

Long Funnel shape can be applied by defining shape as 'long_funnel'. First half of the layers have the value of neuron_max, and then they have the shape similar to Funnel shape - decreasing to the last layer.::


 |          |
 |          |
 |          |
  \        /
   \      /
    \    /
     |  |


Rhombus
-------

Rhobmus can be called by definind shape as 'rhombus'. The first layer equals to 1 and the next layers slightly increase till the middle one which equals to the value of neuron_max. Next layers are the previous ones goin in the reversed order.::

     +   +
     /   \
    /     \
   /       \
  /         \
  \         /
   \       /
    \     /
     \   /
     |   |


Diamond
-------

Defining shape as 'diamond' we will obtain the shape of the 'opened rhombus', where everything is similar to the Rhombus shape, but layers start from the larger number instead of 1. ::

    +     + 
   /       \
  /         \
  \         /   
   \       /
    \     /
     \   /
     |   |


Hexagon
-------


Hexagon, which we get by calling 'hexagon' for shape, starts with 1 as the first layer and increases till the neuron_max value. Then some next layers will have maximum value untill it starts to decrease till the last layer. ::

     +  +
    /    \
   /      \
  /        \
 |          |
 |          |
 |          |
  \        /
   \      /
    \    /
     |  |


Brick
-----


All the layers have neuron_max value. Called by shape='brick'. ::


   |             |
   |             |
   |             |
   |             |
    ----     ----
        |   |


Triangle
--------

This shape, which is called by defining shape as 'triangle' starts with 1 and increases till the last input layer, which is neuron_max. ::


         + +
        /   \
       /     \
      /       \
     /         \
    /           \  
    ----      ----
        |    |

Stairs
------

You can apply it defining shape as 'stairs'. If number of layers more than four, then each two layers will have the same value, then it decreases.If the number of layers is smaller than four, then the value decreases every single layer. ::

   +                      +
   |                      |
    ---                ---
       |             |
        ---       ---
           |     |


----
TEST
----
Once you've trained a model with train(), you can use it easily on any dataset::


   test('text',data,'handle','model.json')
    
Or if you want to see an interactive scatter plot visualization with new y variable::

   test('text',data,'handle','model.json',y_scatter='influence_score')
   
Whatever y_scatter is set as, will be set as the y-axis for the scatter plot. 

To yield the scatter plot, you have to call it specifically::

   test_result = test('text',data,'handle','model.json',y_scatter='influence_score')
   test_result[1]


TEST ARGUMENTS
--------------

The only difference between the two modes of test() is if a scatter plot is called::   
       
    def test(X,data,labels,saved_model,y_scatter=False)
     
+-------------------+-------------------------+-------------------------+
|                   |                         |                         |
| ARGUMENT          | REQUIRED INPUT          | DEFAULT                 |
+===================+=========================+=========================+
| X                 | variable/s in dataframe | NA                      |
+-------------------+-------------------------+-------------------------+
| data              | pandas dataframe        | NA                      |
+-------------------+-------------------------+-------------------------+
| labels            | variable/s in dataframe | NA                      |
+-------------------+-------------------------+-------------------------+
| saved_model       | filename                | 5                       |
+-------------------+-------------------------+-------------------------+
| y_scatter         | variable in dataframe   | 'mean'                  |
+-------------------+-------------------------+-------------------------+ 

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
| name              | dataset or filename     | NA                      |
+-------------------+-------------------------+-------------------------+
| mode              | string ('file')         | NA                      |
+-------------------+-------------------------+-------------------------+

---------------
TROUBLESHOOTING
---------------

One of the most common errors you get working with Keras is related with your output layer::

    ValueError: Error when checking model target: expected dense_22 to have shape (None, 2) but got array with shape (1000, 

This means that your neuron_last does not match the number of categories in 'y'. Usually you would only see this with in cases where you have an output other than 1 or 0, or when you do have that but for some reason changed neuron_last to something else than 1 from train().

You could have a very similar error message from Keras if your dims is not same as the number of features::

    ValueError: Error when checking model input: expected dense_1_input to have shape (None, 300) but got array with shape (1000, 1)
    
NOTE: Your dims number must be exactly the same as the number of features in your mode ('x') except with series of text as an input where the default setting 300 is correct. 

If your dims (input layer) is smaller than output layer (neuron_last)::

    ValueError: Input arrays should have the same number of samples as target arrays. Found 100 input samples and 1 target samples.


-----     
LINKS
-----

.. [Keras_Losses] https://keras.io/losses/
.. [Autonomio_Overview] https://github.com/botlabio/autonomio/blob/master/README.md
