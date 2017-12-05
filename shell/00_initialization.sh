#!/usr/bin/env bash

sudo apt-get update

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

# install some core libraries
sudo apt-get install -y build-essential libssl-dev

# install python 3
sudo apt-get install -y python3 python3-pip python-pip python3-dev
sudo pip install virtualenv

# install mysql server
sudo apt-get install -y mysql-server-5.7 mysql-client-5.7 libmysqlclient-dev

# install nodejs
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs