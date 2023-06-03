#!/usr/bin/env python3

import click
import os
import subprocess


def _walk_dir(dir):
    """walk through directory and returns true if we find a directory labelled .git, otherwise return false

    :param dir: directory to scan
    :type dir: str
    """

    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isdir(dir) is True:
            if os.path.basename(filename) == ".git":
                return True
    return False

def _run_git_commands(dir):
    """Runs the following commandas in order on the repo given

    :param dir: directory path to work on
    :type dir: str
    """
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])

@click.command()
@click.option("-d", "--dir", default=".", type=str, help="target path to scan")
def run(dir):
    is_git = _walk_dir(dir)
    if is_git:
        _run_git_commands(dir)


if __name__ == "__main__":
    run()
