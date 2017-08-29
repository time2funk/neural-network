#!/bin/bash

echo "[ -o- ] Installing requirements"
sudo apt-get install -y python3 python3-dev
sudo pip3 install -r requirements

echo "[ -o- ] Installing nltk libs"
python3 nltk_install.py

echo "[ -o- ] Finish"