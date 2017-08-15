#!/bin/bash

sudo brew update -y
sudo brew install git -y
sudo brew update -y
sudo brew install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip -y
sudo brew install python-dev -y
sudo brew install python-pip -y

wget https://github.com/autonomio/core-module/archive/master.zip -O autonomio.zip
unzip autonomio.zip
mv core-module-master autonomio
cd autonomio 

virtualenv -p /usr/bin/Python2.7 autonomio
source autonomio/bin/activate

sudo pip install --upgrade pip
sudo pip install numpy
sudo pip install numpy --upgrade
sudo pip install pandas
sudo pip install pandas --upgrade 
sudo pip install spacy
sudo pip install spacy --upgrade
sudo pip install tensorflow
sudo pip install tensorflow --upgrade
sudo pip install keras
sudo pip install keras --upgrade 
sudo pip install matplotlib
sudo pip install matplotlib --upgrade
sudo pip install seaborn
sudo pip install seaborn --upgrade 
sudo pip install mpld3
sudo pip install mpld3 --upgrade
sudo pip install h5py
sudo pip install h5py --upgrade -q
sudo pip install jinja2
sudo pip install jinja2 --upgrade -q
sudo pip install jupyter
sudo pip install jupyter --upgrade

sudo python -m spacy download en

wget https://github.com/autonomio/core-module/archive/master.zip -O autonomio.zip
unzip autonomio.zip
mv core-module-master autonomio
cd autonomio 
ls -lhtr
jupyter notebook
