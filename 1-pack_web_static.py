#!/usr/bin/python3


"""
Fabric script that generates .tgz archive from web_static folder contents
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    now = datetime.now()
    dt_string = now.strftime("web_static_%Y%m%d%H%m%S")
    output_file = "versions/{:}.tgz".format(dt_string)
    local("mkdir -p versions")
    result = local("tar -cvzf {:} web_static".format(output_file))
    if result.failed:
        return None
    return output_file
