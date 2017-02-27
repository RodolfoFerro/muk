#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, webbrowser

# Initialize data by user:
print("{:#^45}".format(' TAKE A BREAK! '))
how_many  = int(input("How many times? "))
how_often = int(input("How often? (In secs, please!)" ))
link_vid  = input("Link to video: ")

# Main:
print("This program started on {}".format(time.ctime()))
for times in range(how_many):
    time.sleep(how_often)
    webbrowser.open(link_vid)
    print("Video opened at {}".format(time.ctime()))
