# Contributing to Autonomio

First I want to thank you A LOT for considering / taking the effort to contribute code to Autonomio. Below you will find some simple and mostly obvious guidelines on how to do it in the most valuable way.

To make sure that you're on the same page, for a a high level overview of the scope, see [Autonomio website](http://autonom.io) or for a a detailed overview of the current functionality, see [Autonomio documentation](http://autonomio.readthedocs.io).

# Table of contents

1. [Ways to Contribute](#ways-to-contribute)

    1.1. [Code](#code)
    
    1.2. [Ideas](#ideas)
    
    1.3. [Testing](#testing)
    
    1.4. [Something Else](#something)
    
    1.5. [Documentation](#documentation)
    
    1.6. [Examples](#examples)

2. [Important Precautions for Code Contributions](#precautions)

    2.1. [Planning](#code)
    
    2.2. [Testing](#ideas)

3. [Reviewing Pull Requests](#review)

## 1. Ways to contribute <a name="ways-to-contribute"></a>

There are several ways programmers, data scientists and others can contribute to Autonomio. 

#### 1.1. Contributing Code <a name="code"></a>

##### 1.1.1. Contribute to Open Issues 

It will be great if you can contribute some code to Autonomio. To do this, the best way is to: 

1) check out the [open issues](https://github.com/autonomio/core-module/issues)
2) join the conversation and share your willingness to contribute 
3) somebody will help you get started / provide more details if needed
4) fork [the current dev](https://github.com/autonomio/core-module/issues#fork-destination-box) branch
5) make your changes to your own fork/repo
6) test, test, test 
7) if it's a new feature, make changes to test_script.py accordingly 
8) make sure that Travis build passes
9) come back and make a pull request

What we really try to avoid, is being this guy...

<img src="https://s-media-cache-ak0.pinimg.com/originals/83/f7/8e/83f78e62feb95acc85d000aaf6350d23.jpg" alt="Drawing" width="300px"/>

#### 1.1.2. Contribute to a New Idea 

Same as above, but start by [creating a new issue](https://github.com/autonomio/core-module/issues/new) to open a discussion on the idea you have for contribution.

### 1.2. Contributing Ideas  <a name="ideas"></a>

In case you don't want to contribute code, but have a feature request or some other idea, that is a great contribution as well and will be much appreciated. You can do it by [creating a new issue](https://github.com/autonomio/core-module/issues/new).

<img src="https://mrwweb.com/wp-content/uploads/2012/05/dilbertMay72012-600x186.gif">

### 1.3. Contributing Testing  <a name="testing"></a>

In case you don't want to contribute code, but have a feature request or some other idea, that is a great contribution as well and will be much appreciated. You can do it by [creating a new issue](https://github.com/autonomio/core-module/issues/new). 

**Testing comes in two forms:** 

#### 1.3.1 actual testing

Just use Autonomio for any open challenge you are working on. Or pick one from [Kaggle](https://www.kaggle.com/competitions).

1) Work with Autonomion in data science challenges
2) Try a lot of different things
3) [Report issues](https://github.com/autonomio/core-module/issues/new) as you may find them

#### 1.3.2 improving code coverage

We're using [Coveralls](https://coveralls.io) for code coverage testing, and even the smallest contributions to this end help a great deal. 

1) Follow the instructions in section 1.1 and 1.3.1
2) Use your own fork to see how the results improve in comparison to [current Master](https://coveralls.io/github/autonomio/core-module)

### 1.4. Contributing Something Else  <a name="something"></a>

Last but not least, if there is something you want to do what was not covered in the above sections, please share more by [creating a new issue](https://github.com/autonomio/core-module/issues/new).


### 1.5. Contributing to Manual / Documentation  <a name="documentation"></a>

We're using [Readthedocs](http://readthedocs.io) for documentation. See the latest [Autonomio documentation build](http://autonomio.readthedocs.io) for a reference of current status. The goal is to have comprehensive documentation, enough so that 100% of the actual practical capability is covered in terms of clear instructions. The documentation is automatically built from changes to [docs/index.rst](https://github.com/autonomio/core-module/tree/master/docs).

To contribute to the Manual, you have two options: 

- The pro way: follow the steps in section 1.1
- A simpler way: follow the steps in section 1.4

<img src="https://stevemiles70.files.wordpress.com/2015/05/dilbertontechnicaldoumentation.png" width="600px">

### 1.6. Contributing Examples  <a name="examples"></a>

One of the most useful ways to contribute is when you use Autononomio for an actual project / challenge, and then write a blog post about your experience with code examples. 

## 2. Important Precautions for Code Contributions <a name="precautions"></a>

### 2.1. Planning the Change <a name="planning"></a>

Before even thinking about making any changes to actual code:

1) Define what is happening now (what needs to be changed)
2) Define what is happening differently (once the code is changed) 
3) Use text search to find which files / functions are affected 
4) Make sure that you understand what each function is doing in relation to the change

### 2.2. Testing the Change <a name="testing"></a>

Never ever, under any circumstances, commit code that is not thoroughly tested:  

1) Run through the code changes and ask yourself if it makes sense 
2) Create a clean environment and install from your fork:

    pip install git+http://your-fork-repo-address.git

3) Perform all the commands where your changes are involved and note them down
4) Change the test_script.py in the repo root with the commands from step 3
5) Make sure that code coverage is not becoming lower
6) Make sure that Travis build is passed 

In terms of code coverage, 100% coverage for your changes (coverage does not drop at all) should be the case always. If you can't do that, then at least explain the possible caveats you've made in your commit details and also in the comments section of the pull request you are making. 

Once you've gone through all these steps, take a short break, come back and ask yourself the question: 

"WHAT COULD GO WRONG?"

### 3. Reviewing Pull Requests <a name="review"></a>

If you've been assigned as a reviewer of a given pull request, unless you've been explicitly asked to do so, **DON'T MERGE** just approve the review and share in the comments what you think. If you don't have any comments, just confirm with a comment that you don't have any. 
