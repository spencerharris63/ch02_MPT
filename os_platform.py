#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 22:40:26 2024

@author: spencerharris
"""

import os
import pathlib
import platform

myfolder = pathlib.Path.cwd()
print(myfolder)
myfile = myfolder.joinpath("files").joinpath("example.txt")
print(myfile)
if myfile.exists():
    print("File exists!")
else:
    print("File does not exist.")
    
print("Current working directory:", os.getcwd())

