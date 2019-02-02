#!/bin/bash

MAIN_APP_PATH=""
NGINX_TRAINING_CONF_FILE=""


if [ "$HOSTNAME" = thinkpad ]; then
    MAIN_APP_PATH="/home/sie/__git_projects/stepik/web-programming/trainingapp"
    NGINX_TRAINING_CONF_FILE="$MAIN_APP_PATH/etc/nginx_debug.conf"
else
    if [ "$EUID" -ne 0 ]
        then echo "Please run me as root"
        exit
    fi
    MAIN_APP_PATH="/home/box/web"
    NGINX_TRAINING_CONF_FILE="$MAIN_APP_PATH/etc/nginx_release.conf"
fi

if [ ! -f $NGINX_TRAINING_CONF_FILE ]; then
    echo "$NGINX_TRAINING_CONF_FILE not found! Please create it first!"
    exit
else
    if [ -f /etc/nginx/sites-enabled/test.conf ]; then
        rm -f /etc/nginx/sites-enabled/test.conf
    fi
    ln -s $NGINX_TRAINING_CONF_FILE  /etc/nginx/sites-enabled/test.conf
    /etc/init.d/nginx restart
fi

GUNICORN_TRAINING_CONF_FILE="$MAIN_APP_PATH/etc/hello.py"

if [ ! -f $GUNICORN_TRAINING_CONF_FILE ]; then
    echo "$GUNICORN_TRAINING_CONF_FILE not found! Please create it first!"
    exit
else
    if [ ! -d /etc/gunicorn.d/ ]; then
        mkdir /etc/gunicorn.d
    fi
    ln -s $GUNICORN_TRAINING_CONF_FILE  /etc/gunicorn.d/hello.py
    /etc/init.d/nginx restart
fi

if [ -f /etc/init.d/gunicorn ]; then
    /etc/init.d/gunicorn restart 
fi

if [ -f /etc/init.d/mysql ]; then
    /etc/init.d/mysql restart﻿
fi
