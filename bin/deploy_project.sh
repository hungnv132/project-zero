git stash
git pull origin develop
git stash pop

source /home/ubuntu/project-zero/env/bin/activate
cd /home/ubuntu/project-zero/zero
export DJANGO_SETTINGS_MODULE="zero.settings.production"

pip install -r ../requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

sudo service nginx restart
sudo systemctl restart uwsgi.service
