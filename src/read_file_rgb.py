#!/usr/bin/env python3

import sys
import os
import colorama
import termcolor

colorama.init(autoreset = True)

# -------------------------- INFO --------------------------

def basic():
	global proceed
	proceed = False
	print("Learning GitHub Actions v1.6 ( github.com/ivan-sincek/learning-gitHub-actions )")
	print("")
	print("Usage:   python3 read_file_rgb.py -f file     -c color")
	print("Example: python3 read_file_rgb.py -f test.txt -c red")

def advanced():
	basic()
	print("")
	print("DESCRIPTION")
	print("    Output file's content in RGB")
	print("FILE")
	print("    File to read")
	print("    -f <file> - test.txt | etc.")
	print("COLOR")
	print("    Output color")
	print("    -c <color> - red | green | blue")

# -------------------- VALIDATION BEGIN --------------------

# my own validation algorithm

proceed = True

def print_error(msg):
	print(("ERROR: {0}").format(msg))

def error(msg, help = False):
	global proceed
	proceed = False
	print_error(msg)
	if help:
		print("Use -h for basic and --help for advanced info")

args = {"file": None, "color": None}

def validate(key, value):
	global args
	value = value.strip()
	if len(value) > 0:
		if key == "-f" and args["file"] is None:
			args["file"] = value
			if not os.path.isfile(args["file"]):
				error("File does not exists")
			elif not os.access(args["file"], os.R_OK):
				error("File does not have read permission")
			elif not os.stat(args["file"]).st_size > 0:
				error("File is empty")
		elif key == "-c" and args["color"] is None:
			args["color"] = value.lower()
			if args["color"] not in ["red", "green", "blue"]:
				error("Output color must be either 'red', 'green', or 'blue'")

def check(argc, args):
	count = 0
	for key in args:
		if args[key] is not None:
			count += 1
	return argc - count == argc / 2

argc = len(sys.argv) - 1

if argc == 0:
	advanced()
elif argc == 1:
	if sys.argv[1] == "-h":
		basic()
	elif sys.argv[1] == "--help":
		advanced()
	else:
		error("Incorrect usage", True)
elif argc % 2 == 0 and argc <= len(args) * 2:
	for i in range(1, argc, 2):
		validate(sys.argv[i], sys.argv[i + 1])
	if args["file"] is None or args["color"] is None or not check(argc, args):
		error("Missing a mandatory option (-f, -c)", True)
else:
	error("Incorrect usage", True)

# --------------------- VALIDATION END ---------------------

# ----------------------- TASK BEGIN -----------------------

def color_output(file, color):
	termcolor.cprint(open(file, "r").read(), color)

if proceed:
	print("########################################################################")
	print("#                                                                      #")
	print("#                     Learning GitHub Actions v1.7                     #")
	print("#                                        by Ivan Sincek                #")
	print("#                                                                      #")
	print("# Output file's content in RGB.                                        #")
	print("# GitHub repository at github.com/ivan-sincek/learning-gitHub-actions. #")
	print("#                                                                      #")
	print("########################################################################")
	color_output(args["file"], args["color"])

# ------------------------ TASK END ------------------------
