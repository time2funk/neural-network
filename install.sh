#!/bin/bash

echo "[ -o- ] Installing requirements"
sudo apt-get install python
sudo pip install -r requirements

echo "[ -o- ] Installing nltk"
python nltk_install.py

echo "[ -o- ] Initialization Word2Vec model"
python init.py

echo "[ -o- ] Finish"