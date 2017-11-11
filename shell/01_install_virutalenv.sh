#!/usr/bin/env bash
ENV="env"

if [ -d "$ENV" ]; then
    echo "[== ERROR ==]: Folder 'env' is existed."
    echo "***** Select below actions:"
    echo "*** 1. Remove 'env' and create a new"
    echo "*** 2. Exit."

    read choice

    if [ $choice == 2 ]; then
        exit 1
    elif [ $choice == 1 ]; then
        sudo rm -r $ENV
    fi

fi

PYTHON_PATH=$(which python3)
virtualenv -p $PYTHON_PATH $ENV

echo "[== INFO ==]: Success!!!!"