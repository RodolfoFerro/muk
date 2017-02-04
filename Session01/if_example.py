#!/usr/bin/python
# -*- coding: utf_8 -*-

# We ask for age and convert it to an integer using int()
age = int(input("How old are you? "))

# If you're <18
if age < 18 and age > 0:
    print("You are not legal, yet.")

# If you're 18+
elif age >= 18:
    print("You're and old person.")

# Else (negative numbers)
else:
    print("You can't have that age!")
