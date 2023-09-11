#!/usr/bin/python3


"""
Fabric script based on above that distributes an archive to your web servers
"""
import os
from datetime import datetime
from fabric.api import *
import shlex


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    archive_list = archive_path.split("/")
    archive_filename = archive_list[-1]
    filename_list = archive_filename.split(".")
    filename_noext = filename_list[0]
    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    result = run('mkdir -p /data/web_static/releases/{:}/'.format(
        filename_noext))
    if result.failed:
        return False
    result = run('tar -xzf /tmp/{:} -C /data/web_static/releases/{:}/'.format(
        archive_filename, filename_noext))
    if result.failed:
        return False
    result = run('rm /tmp/{:}'.format(archive_filename))
    if result.failed:
        return False
    result = run('mv /data/web_static/releases/{:}/web_static/* \
                 /data/web_static/releases/{:}/'.format(
                     filename_noext, filename_noext))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/{:}/web_static".format(
        filename_noext))
    if result.failed:
        return False
    result = run('rm -rf /data/web_static/current')
    if result.failed:
        return False
    result = run(
        'ln -s /data/web_static/releases/{:}/ /data/web_static/current'.format(
            filename_noext))
    if result.failed:
        return False
    return True
