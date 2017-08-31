<img src="./docs/autonomio_logo_new.png"  width="250">

[![Build Status](https://travis-ci.org/autonomio/core-module.svg?branch=master)](https://travis-ci.org/autonomio/core-module)  [![Coverage Status](https://coveralls.io/repos/github/autonomio/core-module/badge.svg?branch=master)](https://coveralls.io/github/autonomio/core-module?branch=master) [![Dependency Status](https://gemnasium.com/badges/github.com/mikkokotila/core-module.svg)](https://gemnasium.com/github.com/mikkokotila/core-module) [![PEP8](https://img.shields.io/badge/code%20style-pep8-blue.svg)](https://www.python.org/dev/peps/pep-0008/)

Autonomio provides a very high level abstraction layer for rapidly testing research ideas and instantly creating neural network based decision making models. Autonomio is built on top of Keras, using Tensorflow as a backend and spaCy for word vectorization. Autonomio brings deep learning and state-of-the-art linguistic processing accessible to anyone with basic computer skills. This document focus on an overview of Autonomio's capabilities.

If you want something higher level [visit the website](https://mikkokotila.github.io/slate/#introduction).

## Getting Started

The simplest way is to install with pip from the repo directly.

    pip install git+https://github.com/autonomio/core-module.git

## User Documentation

You can find a comprehensive user documentation with code examples [here](https://mikkokotila.github.io/slate/#introduction).

## Contribution Guidelines

Contributions are most welcome, read more [here](https://github.com/autonomio/core-module/blob/master/CONTRIBUTING.md).

## Examples

- data transformation [link](https://nbviewer.jupyter.org/github/autonomio/core-module/blob/dev/notebooks/autonomio_data_preparation.ipynb)

*(more examples coming soon / dated 31st of July, 2017)*

## Key Features

- intuitive single-command user interface
- hyper parameter grid search
- comprehensive automated data transformation
- optimized for Jupyter notebook use
- NN shape selection and other unique configurations
- create MLP, LSTM and Regression models
- seamlessly integrates word2vec with Keras deep learning
- interactive plots specifically designed for deep learning model evaluation

For most use cases successfully running a neural network works out of the box with zero configuration yielding a model that can be used to predict outcomes later.

## Out-of-the-box use cases

Autonomio is the only deep learning workbench 100% focused on data science applications as opposed to perception problems (e.g. image detection), and have been used in a wide range of industrial and academic use cases.

- Sentiment analysis
- Social media account classification
- Spam detection
- Website classification
- Fraud detection
- Employee satisfaction evaluation
- Popular Kaggle challenges (e.g. Titanic)

## One line use examples

### Training a model

First take care of the imports:

    from autonomio.commands import train, predictor
    %matplotlib inline

Then train the model:

    train(x, y, data)

Training an LSTM model is even simpler:

    train(x,model='lstm')

### Making a prediction

    predictor(data, saved_model_name)  

## Visualization

### Standard Training Output

![mlp and regression training result](http://i.imgur.com/5GSwiJu.png)

### LSTM Training output

![lstm training output](http://i.imgur.com/gjpDCfm.png)

### Hyperscan Output

![4 dimensional hyperscan result](http://i.imgur.com/g4L25sm.png)


### Tested Systems

Autonomio have been tested in several Mac OSX and Ubuntu environments (both server and desktop). Travis builds use Ubuntu Precise.

#### Minimum Hardware

You need a machine with at least 4gb of memory if you want to do text processing, and othewrise 2gb is totally fine and 1gb might be ok. Actually very low spec AWS instance runs Autonomio just fine.

#### Recommended setup

For research and production environments we recommend one server with at least 4gb memory as a 'work station' and a separate instance with high-end CUDA supported GPU. The GPU instance costs roughly $1 per hour, and can be shut down when not used. As setting up the GPU station from ground can be a bit of a headache, we recommend using the [AWS Machine Learning AMI](https://aws.amazon.com/marketplace/pp/B01M0AXXQB) to get setup quickly.

### Dependencies

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

[mpld3](http://mpld3.github.io/)

Major credits to all the contributors to these amazing packages. Autonomio would definitely not be possible without them.
