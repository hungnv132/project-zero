source ./env/bin/activate
cd ./zero
export DJANGO_SETTINGS_MODULE='zero.settings.development'
python manage.py runserver 0.0.0.0:8080