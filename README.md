# Autonomio: human pattern recognition 

Autonomio provides a very high level abstraction layer on top of Keras, using Tensorflow as a backend and spaCy for word vectorization. Autonomio brings deep learning and state-of-the-art linguistic processing accessible to anyone with basic computer skills. 


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
