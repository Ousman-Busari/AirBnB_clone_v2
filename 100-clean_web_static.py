#!/usr/bin/python3
"""
deletes out-of-date archives, using the function do_clean
"""
import os
from fabric.api import *

env.user = "ubuntu"
env.hosts = ["100.25.171.38", "54.237.13.52"]


def do_clean(number):
    """Deletes out-of-date archive

    Args:
        number(int): The number of archives to keep.

    If number is 0 or 1, keep the most recent archive.
    If number is 2, keep the two most recent archives, and so on
    """

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]

    with lcd("versions"):
        [local("rm {}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf {}".format(a)) for a in archives]
