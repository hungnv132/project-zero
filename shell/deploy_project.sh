pkill -f uwsgi -9
git stash
git pull origin develop
git pop

sudo service nginx restart
sudo service uwsgi restart