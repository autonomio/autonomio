# Contributing to Autonomio

First I want to thank you A LOT for considering / taking the effort to contribute code to Autonomio. Below you will find some simple and mostly obvious guidelines on how to do it in the most valuable way.

To make sure that you're on the same page (with rest of the commnity), for a a high level overview of the scope, see [Autonomio website](http://autonom.io) or for a a detailed overview of the current functionality, see [Autonomio documentation](http://autonomio.readthedocs.io).


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

    2.3. [Documentation](#docs_for_review)

3. [Reviewing Pull Requests](#review)

4. [Specific Guidelines for Github](#github)

## 1. Ways to contribute <a name="ways-to-contribute"></a>

There are several ways programmers, data scientists and others can contribute to Autonomio.

#### 1.1. Contributing Code <a name="code"></a>

##### 1.1.0. Note on Philosophy and Style

**AUTONOMIO DEV PHILOSOPHY**

- Doing is more interesting than achieving
- Having fun is more important than being productive
- Code coverage can, and needs to be 100%
- User docs are more important than new features
- Testing is more important than building  
- Creating great stuff takes long time

**CODING STYLE GUIDELINES**

We follow pep8. Because [reading docs](http://legacy.python.org/dev/peps/pep-0008/) and particulary [style guides](http://legacy.python.org/dev/peps/pep-0008/) more or less suck, we use Atom and the amazing Linter plugin so we don't have to.

**MORE STYLE GUIDELINES**

We also make the best effort in moving towards following pep20:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one-- and preferably only one --obvious way to do it.
- Although that way may not be obvious at first unless you're Dutch.
- Now is better than never.
- Although never is often better than right now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let's do more of those!

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

### 2.3. Documentation standards <a name="docs_for_review"></a>

Because Autonomio is to sombased on creating a very high level abstraction, and a lot of "magic" takes place without the user knowing about it, it's very important that we are elaborate in our documentation. This needs to take place to the extent that users like the one who made the following comment are happy:

> Strong documentation and tutorials, with an emphasis on data prep. Don't abstract things at the cost of understanding what is going on behind the hood. I want to know how it all works, and what is being done to my data - I just don't want to have to code every step.

This is the kind of situation we are trying to create; a lot of mundane but hard or time consuming to do things are taken care of on behalf of the user, but if the user so desires, he or she can get a full (and clear!) picture of what's being done.

In order to pass code review (required for merging pull requests), together with your code in the same pull request you must provide the following updates to the documentation [docs/index.rst](https://github.com/mikkokotila/core-module/blob/master/docs/index.rst).

1) What does it do (a high level overview)
  1.1) some use examples
2) What data input is requires
  2.1) some use examples
3) What it outputs
4) What parameters are there (a high level overview)
  4.1) What options each parameter has
  4.2) What is the function of each parameter option

In short summary, the goal is that the user can completely understand 100% of the functioning of the features. If something is done so that the user can’t see it when they are running the commands, we have to explain exactly and thoroughly what kind of automations are taking place.

### 3. Reviewing Pull Requests <a name="review"></a>

If you've been assigned as a reviewer of a given pull request, unless you've been explicitly asked to do so, **DON'T MERGE** just approve the review and share in the comments what you think. If you don't have any comments, just confirm with a comment that you don't have any. While this is kind of obvious, don't start reviewing before you can see all the tests have passed ;)

### 4. General points on using Github  <a name="github"></a>

1) First things first, make sure you understand [this](https://guides.github.com/introduction/flow/index.html) 100%
2) Also make sure that you clearly understand everything that is said [here](https://blog.hartleybrody.com/git-small-teams/)
3) Working on your local machine, only have one folder (the git remote)
4) Load it as module with:

    import sys
    return sys.path.insert(0, '/home/autonomio/dev/core-module')

5) Frequently fetch origin to make sure you get latest changes from other people
6) Don’t work in separate forks, but in branches
7) Keep commits as small as possible
8) Make clear commit messages (explain what you actually are changing)
9) Unless working on something completely new on a separate brach, never start new day without fetching origin

For Mac users Github desktop is pretty fantastic. For Linux users the GUIs are not so fantastic. Atom looks like a good cross-platform option.
