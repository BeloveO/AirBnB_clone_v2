#!/usr/bin/python3


"""
Fabric script that generates .tgz archive from web_static folder contents
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    try:
        d = datetime.now()
        now = d.strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static".format(now))
    except FileNotFoundError:
        return None
