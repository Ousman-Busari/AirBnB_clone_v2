#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import *
import os.path

env.user = "ubuntu"
env.hosts = ["100.25.171.38", "54.237.13.52"]


def do_deploy(archive_path):
    """packs and compressed web_static"""

    if os.path.isfile(archive_path) is False:
        return (False)

    file = archive_path.split("/")[1]
    name = file.split(".")[0]
    root_path = "/data/web_static/releases"

    r = put(archive_path, "/tmp/%s" % file)
    print(r.failed)
    run("mkdir -p %s/%s" % (root_path, name))
    run("tar -xzf /tmp/%s -C %s/%s" %
        (file, root_path, name))
    run("rm /tmp/%s" % file)
    run("mv %s/%s/web_static/* %s/%s/"
        % (root_path, name, root_path, name))
    run("rm -rf %s/%s/web_static/" % (root_path, name))
    run("rm -rf /data/web_static/current")
    r = run("ln -s %s/%s /data/web_static/current" %
            (root_path, name))
    return (r.succeeded)
