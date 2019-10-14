#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

name = "dwm"
source = "https://aur.archlinux.org/dwm-git.git"
keep_files = [
    "config.h",
    "dwm.patch"
]


def pre_build():
    os.system("patch < dwm.patch")
