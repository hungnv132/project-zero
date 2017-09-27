ENV="env"

sudo apt-get install python-pip python-dev build-essential -y
sudo apt-get install python3
sudo pip install virtualenv

if [ -d "$ENV" ]; then
    echo "[== ERROR ==]: Folder 'env' is existed."
    echo "***** Select below actions:"
    echo "*** 1. Remove 'env' and create a new"
    echo "*** 2. Exit."

    read select

    if [ $select == 2 ]; then
        exit 1
    elif [ $select == 1 ]; then
        sudo rm -r $ENV
    fi

fi

PYTHON_PATH=$(which python3)
virtualenv -p $PYTHON_PATH $ENV

echo "[== INFO ==]: Success!!!!"