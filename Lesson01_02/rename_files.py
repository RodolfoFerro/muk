#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re

# Set folder path:
path = "/Users/RodolfoFerro/Desktop/MOOC/01/prank/"

def rename_files(path):
    # Get file names from folder:
    file_list = os.listdir(path)
    # print(file_list)

    # For each file, rename file:
    for index, file_name in enumerate(file_list):
        new_name = re.sub("\d", "", file_name)
        os.rename(path + file_name, path + new_name)
        print("\nFile {} \nOld name: {} \nNew name: {}".format(index, file_name, new_name))

rename_files(path)
