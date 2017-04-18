<img src="./docs/autonomio_logo_new.png"  width="250">

Autonomio provides a very high level abstraction layer on top of Keras, using Tensorflow as a backend and spaCy for word vectorization. Autonomio brings deep learning and state-of-the-art linguistic processing accessible to anyone with basic computer skills. 

## Key Features

- intuitive single-command neural network training
- training command accepts as little as 'x' and 'y' as inputs 
- 'x' can be text, continues or categorial data
- 15 optional configurations from a single command
- seamlessly integrates word2vec with keras deep learning
- interactive plots specifically designed for deep learning

For most use cases succesfully running a state-of-the-art AI works out of the box in less than 60 seconds to first trained model.

## Deep learning in two simple commands (first time use)

Open a jupyter notebook (or python console) and type: 

    python -m spacy download en

and then:

    from autonomio.commands import *
    %matplotlib inline
    
    train(x,y,data,labels)
    
Even if 'x' is unstructured/text, this command will yield a functional neural network trained to predict the 'y' variable. 'y' can be continuous, categorical or binary. The model can be saved and then used to predict other data without training:

    test(x,data)
    
This will yield a pandas dataframe with the values and whichever label you ware connecting the value with.     

## Slightly more involving use

To train a neural network, and then use it for making a prediction on a different dataset is almost as easy as the first example. This time let's also introduce some of the command parameters available for 'train' function. 

    train('text','quality_score',
          tweets.head(3000),
          epoch=10,
          dropout=.5,
          flatten=.3,
          save_model=True,
          verbose=0)

Instead of the default 5 epochs, we're setting epoch to 10 and increase dropout rate between layers to 50%. Also instead of using the default flattening (transforming y feature to 0 and 1), we take only the bottom 30% in the *inter quartile range*. 

## Standard training output

![test result output](http://i.imgur.com/i4MkYmo.png)


## Dependencies 

#### Data Manipulation

[Numpy](http://www.numpy.org/)

[Pandas](http://pandas.pydata.org/)

#### Word Processing

[spaCy](https://spacy.io/)

#### Deep Learning

[Keras](http://keras.io)

[Tensorflow](https://www.tensorflow.org/)

#### Visualization

[Matplotlib](http://matplotlib.org/)

[Seaborn](http://seaborn.pydata.org/)

[mpld3](http://mpld3.github.io/)


## background 

Up until today most of linguistic technologies, not to mention deep learning, have not been accessible in the way that they would allow seamless workflow that supports the need of even less computer savvy researchers. Yet the modern researcher can benefit significantly from unlocking the value in unstructured data, and there are by some estimates 9 times more of unstructured data than structured. Autonomio combines two cutting edge AI technologies - word vectorizing and deep learning - in to one intuitive tool researchers from wide range of backgrounds can benefit from.

## performance

Because of the excellent out-of-the-box neural network performance provided by Keras, Autonomio users get state-of-the-art prediction capability with minimal setting configuration. Autonomio has been tested extensively and consistently provides in a single line of code the same result that you would get from Keras with 10 lines of code. Using real data involving bilions of dollars in advertising spend, we've proven autonomio to be cabably of yielding outstanding results in previously unsolved problems such as better than human classifier result for niche website category classification.

## user experience

Artificial Intelligence and the signals intelligence method should be accessible to all researchers. Autonomio allows total non-programmers in most cases to easily create advanced neural networks without any data preparation through an easy to memorize single command interface. Autonomio has two commands:

    train(x,y,data)

and

    test(x,data)
    
An example of Autonomio's usability factor is how x can be ustructured data, as is the case in an increasing number of challenges research phase in the digital age. 

## Language processing

Autonomio uses a novel way of processing unstructured data, 

1) pre-process text 
2) use spaCy to vectorize the text 
3) create 300 invididual features from the vector
4) use the features as a signal in a Keras model 


### Language support

Autonomio's vectorizing engine spaCy supports currently 13 languages: 

- English
- German
- Chinese
- Spanish
- Italian
- French
- Portuguese
- Dutch
- Swedish
- Finnish
- Hungarian
- Bengali
- Hebrew

NOTE: the spacy language libraries have to be downloaded each separately.

[Read spaCy's language page](https://spacy.io/docs/api/language-models)


### Adding new languages 

spaCy makes it reletively streamlined to create support for any language and the challenge can (and should be) approached iteratively. 
