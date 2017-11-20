#!/usr/bin/env bash

username='root'

sudo mysql -u${username} -p -e \
    "DROP DATABASE IF EXISTS zero_db;
     CREATE DATABASE zero_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;;
     CREATE USER IF NOT EXISTS'admin'@'%' IDENTIFIED BY '123456';
     GRANT ALL PRIVILEGES ON zero_db.* TO 'admin'@'%' WITH GRANT OPTION;
     SHOW DATABASES;
     "



