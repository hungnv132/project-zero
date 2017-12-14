git stash
git pull origin develop
git stash pop

sudo service nginx restart
sudo systemctl restart uwsgi.service
