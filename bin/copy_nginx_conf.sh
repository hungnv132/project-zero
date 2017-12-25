#!/usr/bin/env bash

sites_available=/etc/nginx/sites-available
sites_enabled=/etc/nginx/sites-enabled
project=/home/ubuntu/project-zero

sudo rm $sites_available/nginx_zero
sudo rm $sites_enabled/nginx_zero
sudo cp $project/config/nginx_zero $sites_available
sudo ln -s $sites_available/nginx_zero $sites_enabled