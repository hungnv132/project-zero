git stash
git pull origin develop
git stash pop

source home/hungnv132/project-zero/env/bin/activate
cd home/hungnv132/project-zero/zero
export DJANGO_SETTINGS_MODULE="zero.settings.production"
python manage.py collectstatic --noinput

sudo service nginx restart
sudo systemctl restart uwsgi.service
