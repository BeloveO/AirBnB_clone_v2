#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
printf "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i '/listen 80 default_server;/a location  /hbnb_static { alias /data/web_static/current; autoindex off; }' /etc/nginx/sites-available/default
service nginx restart
