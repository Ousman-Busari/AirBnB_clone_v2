#!/usr/bin/python3
""" generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo,
using the function do_pack
"""
from fabric.api import *
from datetime import datetime
import os.path


env.user = "ubuntu"
env.hosts = ["100.25.171.38", "54.237.13.52"]


def do_pack():
    """packs and compressed web_static"""
    local("mkdir -p versions")

    arch = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf %s web_static/" % arch)

    if (result.succeeded):
        return (arch)
    return (None)


def do_deploy(archive_path):
    """deploys, extracts, and decompressed archived web_static"""

    if os.path.isfile(archive_path) is False:
        return (False)

    file = archive_path.split("/")[1]
    name = file.split(".")[0]
    root_path = "/data/web_static/releases"

    put(archive_path, "/tmp/%s" % file)
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


def deploy():
    """packs and deploys web_static"""

    archived_path = do_pack()
    return(do_deploy(archived_path))
