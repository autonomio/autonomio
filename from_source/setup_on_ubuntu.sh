#!/bin/bash

sudo apt-get update -y
sudo apt-get install git -y
sudo apt-get update -y
sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip -y
sudo apt-get install python-dev -y
sudo apt-get install python-pip -y

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

sudo pip install jupyter
sudo pip install jupyter --upgrade

sudo python -m spacy download en

jupyter notebook
