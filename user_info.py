#!/usr/bin/env python

import os

# Gives user's home directory
userhome = os.path.expanduser('~')          
print("User's home Dir: " + userhome)

# Gives username by splitting path based on OS
user = str(os.path.split(userhome)[-1])
print("Username: " + user)

# Gives user's running processes
print("Here's your running processes: ")
os.system("ps"+ " -u "+user)
