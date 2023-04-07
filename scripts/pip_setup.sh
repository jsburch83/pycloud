#!/bin/sh

# Download pip install script
wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py
# Install pip from script
python3 get-pip.py
# remove install script
rm ./get-pip.py 
