# file: /etc/init/uwsgi.conf
description  "UWSGI Server"

project=/home/hungnv132/project-zero

start on runlevel [2345]
stop on runlevel [!2345]
respawn
exec $project/env/bin/uwsgi --ini $project/config/uwsgi_zero.ini