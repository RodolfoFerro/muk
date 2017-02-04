#!/usr/bin/python
# -*- coding: utf_8 -*-

# We import the time library
import time

# Define an initial age:
age = 13

# While age is less than 17...
while age < 17:
    print("SHE:\t I'm {} years old.".format(age))
    print("HE:\t I still don't love your innocence.")
    age += 1        # age = age + 1
    time.sleep(2)   # This will wait 3 seconds
    print()


print("SHE:\t Now, I'm {} years old.".format(age))
print("HE:\t Now:")
print("\t   - I love your innocence.")
print("\t   - I love your mistakes.")
print("\t   - I'm your first boyfriend.")
print("\t   - I'm your first love.")
print()
