#!/usr/bin/env bash
sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

sudo ln -sf /home/box/web/base.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart