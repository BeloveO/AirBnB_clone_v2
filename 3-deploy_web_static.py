#!/usr/bin/python3
"""
Fabric script based on above that creates and
distributes an archive to your web servers
"""


import os
from datetime import datetime
from fabric.api import *
import shlex

env.hosts = ["54.208.117.130", "100.26.222.213"]
env.user = "ubuntu"


@runs_once
def do_pack():
    """Generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')
    path = "versions/web_static_{}.tgz".format(now)

    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(path))
    return path


def do_deploy(archive_path):
    """Distributes a .tgz archive through web servers
    """

    if path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))

        return True

    return False


def deploy():
    archive = do_pack()
    return do_deploy(archive)
