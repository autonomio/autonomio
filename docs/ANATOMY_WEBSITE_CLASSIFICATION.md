# contexor

### A python classifier that provides accurates contextual classifying for any website in seconds. 

## 1. Background 

Researchers commonly can benefit from a capability to classify websites automatically based on prominent content on the site. For example, a researcher may want to scan a large number of sites to identify sites that have a strong affinity with a specific topic ('privacy') or behaviour ('strong language').

Kuubio uses Keras with TensorFlow backend, spaCy, Pandas and Numpy.

## 2. Key Features 

The Kuubio principles is that running state-of-the-art deep learning models should be in 99% of the cases possible from a one line command. Kuubio already makes this possible, and removes some of the remnants of obstacles between researchers and the mythical deep learning method. 

- seamless deep learning pipeline where you can do everything from one command
- automatic conversion of text to word vectors using word2vec 
- state-of-the-art language and topic agnostic NLP 

### 3. How to use? 

The current version of Kuubio deep learning function looks like this. No other code is needed.


    predictions = kuubio(X=[0:300],                   # features
                             Y='ivt',                 # indepedent variable
                             data=sites,              # name of dataframe
                             dims=300,                # number of features
                             epoch=5,                 # no of training cycles
                             flatten=.8,              # conversion to binary
                             layers=5,                # number of layers in the model
                             neuron_first='auto',     # number of neurons on first layer
                             neuron_last=1,           # number of neurons on last layer
                             model='model',           # option to load model
                             loss='binary_crossentropy',  # which model to use
                             save_model=False)        # option to save model


### 3.2. Basic use

The other rule is that the one line command has to run with as little input as x,y and the model should still perform. This is not too hard as Keras has made it sure that various models work out of the box. So the simplest use case is: 

     kuubio('feature','indepedent_var',df)
     
There are a couple of very useful hidden features in inputting X. 

###### 3.2.1 Input a range of columns 

use list for a range of columns: 

     kuubio([0:300],'ind_var',df)

###### 3.2.1 Input column labels

     kuubio(['var1','var2'],'ind_var',df)


### 3.3. Use with Text 

 
    
## 4. Solution 

The solution consist of three primary capabilities: 

1) to capture a representative set of pages from the site
2) to distinguis between sections (e.g. comments) on the page and parse clean text 
3) make prediction for classification 

### 2.1. data capture 

1) domain/s input from user
2) extract urls of prominent pages from landing page
3) extract html from invididual pages

### 2.2. content capture 

- separate the page to sections (e.g. comments, body, ads) 
- separate clean text from other elements in each page section 

### 2.3. classification 

- tokenize text for analysis
- run models 
- output classification 

## 3. User Interactions

There are two kinds of interactions: 

1) configuration
2) regular use 

### 3.1. Configuration 

- create a list of seed sites for the category
- run through test results that prove the model works
- tweak the seed:
 - add or remove words
 - define co-occurance of words
 - define weights for words
 - define proximities 

### 3.2. Regular Use

- input a single site to API
- input a list of sites to API
- get a dictionary/json in return with the classification 

## 4. 3rd-party technology

- Pandas for data wrangling
- Numpy for arrays and maths
- nltk for semantics 
- nightmare.js or some other headless browswer for html extraction
- Beautiful soup for clear text extraction

## 5. System requirements 

The solution is able to perform classification for a single site in less than 5 seconds using an AWS micro instance with GB1 of RAM. 

## 6. Style guide

- PEP8 (at least close)
- no line of code longer than 50 chars
- no function longer than 50 rows 
