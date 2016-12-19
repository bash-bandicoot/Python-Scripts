#!/usr/bin/env python 
import sys
import os
import readline
readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n')
 
path = raw_input("Please input dir path: ")

if os.path.isdir(path): 
	print path + " is a directory"
else:
	os.path.isfile(path)
	print path + " is a file"
