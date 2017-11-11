#!/usr/bin/env bash

username='root'

sudo mysql -u${username} -p -e \
    "
     CREATE DATABASE IF NOT EXISTS zero_db;
     CREATE USER IF NOT EXISTS'admin'@'%' IDENTIFIED BY '123456';
     GRANT ALL PRIVILEGES ON zero_db.* TO 'admin'@'%' WITH GRANT OPTION;
     SHOW DATABASES;
     "



