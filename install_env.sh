#!/bin/sh
# install python
apt-get -y install python-pip python-dev python-virtualenv build-essential
# install python packages
pip install ipython[notebook] numpy scipy pandas matplotlib scikit-learn
