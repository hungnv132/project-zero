git stash
git pull origin develop
git stash pop

cd zero
export DJANGO_SETTINGS_MODULE="zero.settings.production"
python manage.py collectstatic --noinput

sudo service nginx restart
sudo systemctl restart uwsgi.service
