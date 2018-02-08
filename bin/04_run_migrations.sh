ENV_FOLDER="env"

export DJANGO_SETTINGS_MOUDLE="zero.settings.development"
source ./$ENV_FOLDER/bin/activate
cd ./zero
python manage.py migrate
