#!/usr/bin/python
import sys
import os
import readline
readline.parse_and_bind('tab: complete')
readline.set_completer_delims(' \t\n')

value1 = raw_input("Please type FULL INPUT path: ")
input_path = value1
if os.path.exists(input_path):
    print("Input path found, here\'s its content: ")
    os.system("ls " + input_path)
else:
    print("Input path is incorrect! Please check and start over!")
    raise SystemExit

choice = raw_input("Do you want to merge all the fastq files? (y)es or (n)o: ")
if choice == "yes" or choice == "y":
    os.chdir(input_path)
    print("Merging...")
    os.system("cat *.fastq > mergedby$USER$(date +%Y%m%d).fastq")
    os.system("ls " + input_path)
    value2 = raw_input("Please choose the merged file: ")
    input_file = value2
elif choice == "no" or choice == "n":
    os.chdir(input_path)
    value2 = raw_input("Please choose stand alone fastq file: ")
    os.chdir(input_path)
    input_file = value2
else:
    print("Please choose (y)es or (n)o")
    raise SystemExit

value3 = raw_input("Please type full OUTPUT path: ")
output_path = value3
if os.path.exists(output_path):
    print("Output path found")
else:
    print("Output path is incorrect! Please check and start over!")
    raise SystemExit

print("Please choose DB")
print("1. hg38")
print("2. hg19")
print("3. mm10")

value4 = raw_input("Enter your choice [1-3] : ")
value4 = int(value4)
if value4 == 1:
    db = str("/shareDB/exceRpt/hg38:/exceRpt_DB/hg38") 
    print("Choosed DB is: hg38 ")
elif value4 == 2:
    db = str("/shareDB/exceRpt/hg19:/exceRpt_DB/hg19") 
    print("Choosed DB is: hg19 ")
elif value4 == 3:
    db = str("/shareDB/exceRpt/mm10:/exceRpt_DB/mm10")
    print("Choosed DB is: mm10 ")
else:
    print("Invalid number.")
    raise SystemExit

os.system("docker " + "run " + "-u " + "$(id -u) " + "-v " + input_path + ":/exceRptInput " + "-v " + output_path + ":/exceRptOutput " + "-v " + db + "-t " + "rkitchen/excerpt " + "INPUT_FILE_PATH=/exceRptInput/" + input_file)
