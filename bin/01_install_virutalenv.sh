#!/usr/bin/env bash
ENV_FOLDER="env"

if [ -d "$ENV_FOLDER" ]; then
    echo "[== ERROR ==]: Folder 'env' is existed."
    echo "***** Select below actions:"
    echo "*** 1. Remove 'env' and create a new"
    echo "*** 2. Exit."

    read choice

    if [ $choice == 2 ]; then
        exit 1
    elif [ $choice == 1 ]; then
        sudo rm -r $ENV_FOLDER
    fi

fi

PYTHON_PATH=$(which python3)
virtualenv -p $PYTHON_PATH $ENV_FOLDER

echo "[== INFO ==]: Created Virtual Envvironment 'env'!!!!"