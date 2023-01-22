#!/usr/bin/python3
""" generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo,
using the function do_pack
"""
from fabric.api import *
from datetime import datetime

def do_pack():
    local("mkdir -p versions")

    arch = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local("sudo tar -cvzf %s web_static/" % arch)

    if (result.succeeded):
        return (arch)
    return (None)
