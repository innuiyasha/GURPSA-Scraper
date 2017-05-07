#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

print("-----Starting .txt Extraction-----")


with open(sys.argv[1]) as f:
	book = f.readlines()

	target = open("Advantages.xml", 'w')
	target.truncate()
	
	print("Removing empty lines and page numbers")
	
	for linenum in range(len(book)):
		if(re.search("ADVANTAGES", book[linenum])):
			book[linenum] = ""
		elif(not re.match("[a-zA-Z0-9]+", book[linenum])):
			book[linenum] = ""

	print("Parsing for advantages")
	target.write("<ADVANTAGES>\n")
	for linenum in range(len(book)):
		if(re.match("[0-9]+\s(point)", book[linenum]) and (not re.search("[;\.,]", book[linenum]))):
			target.write("<advantage>\n")
			
			if(re.match("[a-zA-Z0-9°/]", book[linenum - 1]) and re.search("[a-zA-Z]", book[linenum - 1])):
				target.write("\t<name>\n\t\t" + book[linenum - 1] + "\t</name>\n")
			else:
				target.write("\t<name>\n\t\t" + re.sub("[\n\r]", "", book[linenum - 2]) + " " + re.sub("[\n\r\s]+", "", book[linenum - 1]) + "\n\t</name>\n")
			
			target.write("</advantage>\n")
		elif(re.match("^[0-9]+(,\s+[0-9]+|\sto\s[0-9]+|\sor\s[0-9]+)+", book[linenum])):
			target.write("<advantage>\n")
			
			if(not re.match("[0-9]", book[linenum - 1]) and re.search("[a-zA-Z]", book[linenum - 1])):
				target.write("\t<name>\n\t\t" + book[linenum - 1] + "\t</name>\n")
			else:
				target.write("\t<name>\n\t\t" + re.sub("[\n\r]", "", book[linenum - 2]) + " " + re.sub("[\n\r\s]+", "", book[linenum - 1]) + "\n\t</name>\n")
			
			target.write("</advantage>\n")
		elif(re.match("Variable", book[linenum])):
			target.write("<advantage>\n")
			
			if(re.match("[a-zA-Z0-9°]", book[linenum - 1]) and re.search("[a-zA-Z]", book[linenum - 1])):
				target.write("\t<name>\n\t\t" + book[linenum - 1] + "\t</name>\n")
			else:
				target.write("\t<name>\n\t\t" + re.sub("[\n\r]", "", book[linenum - 2]) + " " + re.sub("[\n\r\s]+", "", book[linenum - 1]) + "\n\t</name>\n")
			
			target.write("</advantage>\n")
		elif(re.match("see.*p.\s+[0-9]+[\s\n\r]+", book[linenum])):
                        target.write("<advantage>\n")
			
			if(re.match("[a-zA-Z0-9°]", book[linenum - 1])):
				target.write("\t<name>\n\t\t" + book[linenum - 1] + "\t</name>\n")
			else:
				target.write("\t<name>\n\t\t" + re.sub("[\n\r]", "", book[linenum - 2]) + " " + re.sub("[\n\r\s]+", "", book[linenum - 1]) + "\n\t</name>\n")
			
			target.write("</advantage>\n")
			

	target.write("</ADVANTAGES>\n")
target.close()
print("-----Done-----")
