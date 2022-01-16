#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright ©️ 2022 cGIfl300 <cgifl300@gmail.com>

import os
# import shutil
from subprocess import call

list_directories = []
to_delete = 0


# shutil.rmtree.avoids_symlink_attacks=True


def walk_in(directory):
    global list_directories
    for it in os.scandir(directory):
        if it.is_dir():
            list_directories.append(it.path)
            walk_in(it)


print("Starting crawling...")
walk_in(".")

print("Removing twins...")
list_directories = list(dict.fromkeys(list_directories))

print("Checking paths to delete...")
for this_dir in list_directories:
    if this_dir[len(this_dir) - 5:] == "\\venv" or this_dir[
                                                   len(this_dir) - 6:] == "\\.idea":
        print(f"Deleting {this_dir}")
        # Doesn't work on Windows
        # shutil.rmtree(dir, ignore_errors=True)

        # Works on Windows
        call(f"del {this_dir} /q /s", shell=True)
        call(f"rmdir {this_dir} /q /s", shell=True)

input("Thank you for waiting, you can close this windows pressing [ENTER]...")
