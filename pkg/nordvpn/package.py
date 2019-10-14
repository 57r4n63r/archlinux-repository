#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "nordvpn"
source = "https://aur.archlinux.org/nordvpn-bin.git"

def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=nordvpn")
        else:
            print(line)
