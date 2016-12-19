#!/usr/bin/env python
import sys
import os
import readline
readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n')

location = raw_input("Please enter search location: ")
if os.path.exists(location):
	print("Please choose search type:")
	print("1. search for a file")
	print("2. search for a string")
	choose = raw_input("your choice: ")
	choose = int(choose)	
	if choose == 1:
		my_file = raw_input("enter file name: ")
		os.system("find "+location+" -name "+my_file)
	elif choose == 2:
		my_string = raw_input("enter string to search: ")
		os.system("grep -rnw "+location+" -e "+my_string)		 
else:
    print("Nothing found! Please check file or string name.")
