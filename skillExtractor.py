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
	
	target.write("<skillManager>\n<skillList>\n")
	for linenum in range(len(book)):
		if(re.match("(IQ|DX|Will|Per|HT)/[Very Easy|Easy|Average|Hard|Very Hard]", book[linenum]) and (not re.search("[;,]",book[linenum]))):
			target.write("<entry>\n")
			name = re.sub("[0-9†\s](?![a-zA-Z])","", book[linenum - 1])
			nameTL = name.split('/')
			target.write("\t<key>\n\t\t" + nameTL[0] + "\n\t</key>\n\t\t")
                        target.write("<value>\n")
                        target.write("<name>" + nameTL[0] + "</name>")
			if len(nameTL) == 1:
                                target.write("<TL>false</TL>")
                        else:
                                target.write("<TL>true</TL>")
			
                        target.write("<attr>\n")
			for char in book[linenum]:
				if char == '/':
					target.write("\n\t</attr>\n")
					target.write("\t<diff>\n\t\t")
				else:
					target.write(char)
			target.write("\t</diff>\n\t")
			
			i = 0
			line = ""
			while (True):
				i += 1
				line += book[linenum + i]
				if(re.match(".*\.", book[linenum + i])):
					i += 1
					break
			defaults = [""]
			line = line.replace("\n", "")
			#line = line.replace("\r", "")
                        #line = line.strip('\n')
			if("None" in line):
                                defaults = ["None"]
			elif("Default:" in line):
                                line = line[9:]
                                line = line.replace(".", "")
                                line = line.replace("-", "")
                                defaults = re.split("([0-9]+)", line)
                        elif("Defaults:" in line):
                                line = line[10:]
                                line = line.replace(",", "")
                                line = line.replace(".", "")
                                line = line.replace("or", "")
                                line = line.replace("-", "")
                                line = line.replace("to", "")
                                defaults = re.split("([0-9]+)", line)
			if not re.match("[a-zA-Z0-9]+", defaults[len(defaults) - 1]):
                                #del defaults[len(defaults) - 1]
                                defaults = defaults[:-1]

                        if len(defaults) > 1:
                                x = 0
                                while x < len(defaults):
                                        target.write("<default>\n<name>" + defaults[x] + "</name>")
                                        try:
                                                target.write("<penalty>" + defaults[x + 1] + "</penalty>\n</default>")
                                        except (IndexError):
                                                target.write("<penalty>" + '0' + "</penalty>\n</default>")
                                        x += 2

			if defaults != []: print(defaults)
			target.write("\n\t<desc>\n")
			
			# TODO: Fix issue with Anthropology and some others
			# TODO: Include prerequisites
				
			while ( linenum + i + 1 < len(book) and ((not re.match("(IQ|DX|Will|Per|HT)/[Very Easy|Easy|Average|Hard|Very Hard]", book[linenum + i + 1])) and (not re.match("see", book[linenum + i + 1])))):
				if(re.search("[a-zA-Z0-9]", book[linenum + i])):		# Prevents weird indentation for </desc>
					target.write("\t\t" + book[linenum + i])
				i += 1
			target.write("</desc>\n\n\n")
                        target.write("</value>\n")
			target.write("</entry>\n")
		elif(re.match("see", book[linenum])):
			target.write("<entry>\n")
			target.write("<key>\n\t\t" + re.sub("[0-9†\s](?![a-zA-Z])","",book[linenum - 1]) + "\n\t</key>\n")
			target.write("<value>")
			target.write("<ref>\n" + "\t\t" + book[linenum] + "\t</ref>\n\n\n")
			target.write("</value>\n")
			target.write("</entry>")


	target.write("</skillList>\n</skillManager>")
target.close()
print("-----Done-----")
