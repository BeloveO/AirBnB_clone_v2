#!/usr/bin/python3


"""
Fabric script that generates .tgz archive from web_static folder contents
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    date = datetime.utcnow()
    dt_string = date.strftime("web_static_%Y%m%d%H%m%S")
    output = "versions/{:}.tgz".format(dt_string)
    local("mkdir -p versions")
    result = local("tar -cvzf {:} web_static".format(output))
    if result.failed:
        return None
    return output
