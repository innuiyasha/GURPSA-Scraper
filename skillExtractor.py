#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

print("-----Starting .txt Extraction-----")


with open(sys.argv[1]) as f:
	book = f.readlines()

	target = open("Skills.xml", 'w')
	target.truncate()
	
	print("Removing empty lines and page numbers")
	
	for linenum in range(len(book)):
		if(re.search("SKILLS", book[linenum])):
			book[linenum] = ""
		elif(not re.match("[a-zA-Z0-9]+", book[linenum])):
			book[linenum] = ""

	print("Parsing for skills")
	
	target.write("<SKILLS>\n")
	for linenum in range(len(book)):
		if(re.match("(IQ|DX|Will|Per|HT)/[Very Easy|Easy|Average|Hard|Very Hard]", book[linenum]) and (not re.search("[;,]",book[linenum]))):
			target.write("<skill>\n")
			target.write("\t<name>\n\t\t" + re.sub("[0-9†\s](?![a-zA-Z])","", book[linenum - 1]) + "\n\t</name>\n\t\t")
                        target.write("<attr>\n")
			for char in book[linenum]:
				if char == '/':
					target.write("\n\t</attr>\n")
					target.write("\t<diff>\n\t\t")
				else:
					target.write(char)
			target.write("\t</diff>\n\t<default>\n")
			
			i = 0
			while (True):
				i += 1
				target.write("\t\t" + book[linenum + i])
				if(re.match(".*\.", book[linenum + i])):
					i += 1
					break
				
				
				
			
			target.write("\t</default>\n\t<desc>\n")
			
			# TODO: Fix issue with Anthropology and some others
			# TODO: Include prerequisites
				
			while ( linenum + i + 1 < len(book) and ((not re.match("(IQ|DX|Will|Per|HT)/[Very Easy|Easy|Average|Hard|Very Hard]", book[linenum + i + 1])) and (not re.match("see", book[linenum + i + 1])))):
				if(re.search("[a-zA-Z0-9]", book[linenum + i])):		# Prevents weird indentation for </desc>
					target.write("\t\t" + book[linenum + i])
				i += 1
			target.write("\t</desc>\n\n\n")
			target.write("</skill>\n")
		elif(re.match("see", book[linenum])):
			target.write("<skill>\n")
			target.write("\t<name>\n\t\t" + re.sub("[0-9†\s](?![a-zA-Z])","",book[linenum - 1]) + "\n\t</name>\n")
			target.write("\t<ref>\n" + "\t\t" + book[linenum] + "\t</ref>\n\n\n")
			target.write("</skill>\n")


	target.write("</SKILLS>\n")
target.close()
print("-----Done-----")
