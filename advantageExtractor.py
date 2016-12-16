#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

print("-----Starting .txt Extraction-----")


with open(sys.argv[1]) as f:
	book = f.readlines()

	target = open("advantages.xml", 'w')
	target.truncate()
	
	print("Removing empty lines and page numbers")
	
	for linenum in range(len(book)):
		if(re.search("ADVANTAGES", book[linenum])):
			book[linenum] = ""
		elif(not re.match("[a-zA-Z0-9]+", book[linenum])):
			book[linenum] = ""

	print("Parsing for advantages")
	
	for linenum in range(len(book)):
		if(re.match("[0-9]+\s(point)", book[linenum]) and (not re.search("[;,]",book[linenum]))):
			target.write("<advantage>\n")
			
			if(re.match("[a-zA-Z]", book[linenum - 1])):
				target.write("\t<name>\n\t\t" + book[linenum - 1] + "\n\t</name>\n\t\t")
			else:
				target.write("\t<name>\n\t\t" + book[linenum - 2] + "\n\t</name>\n\t\t")
			
			target.write("</advantage>\n")


target.close()
print("-----Done-----")
