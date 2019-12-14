#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

name = "dwm"
source = "https://aur.archlinux.org/dwm-git.git"
keep_files = [
    "config.def.h"
]


def pre_build():
    os.system("cp config.def.h config.h")

    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=dwm")
        else:
            print(line)
