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
        target.write("<advantage><desc>\n")
        linenum = 0
        while linenum < len(book):
       # for linenum in range(len(book)):
                try:
                        if((re.match("[0-9]+\s(point)", book[linenum + 1])
                           and (not re.search("[;\.,]", book[linenum + 1])))
                           or re.match("^[0-9]+(,\s+[0-9]+|\sto\s[0-9]+|\sor\s[0-9]+)+", book[linenum + 1])
                           or re.match("Variable", book[linenum + 1])
                           or re.match("see.*p.\s+[0-9]+[\s\n\r]+", book[linenum + 1])):
                                
                                target.write("\n</desc>\n</advantage>\n")
                                target.write("<advantage>\n")
                                parts = book[linenum].split(" ")
                                title = ""
                                count = 0
                                while count < len(parts) - 1:
                                        title += parts[count] + " "
                                        count += 1
                                        
                                
                                if(re.match("([0-9]+/*)+", parts[len(parts) - 1])):
                                        target.write("<name>" + title + "</name>")
                                        target.write("<nums>" + parts[len(parts) - 1] + "</nums>")
                                else:
                                        if(re.match("[a-zA-Z0-9°/]", book[linenum]) and re.search("[a-zA-Z]", book[linenum])):
                                                target.write("\t<name>\n\t\t" + book[linenum] + "\t</name>\n")
                                        else:
                                                target.write("\t<name>\n\t\t" + re.sub("[\n\r]", "", book[linenum - 1]) + " " + re.sub("[\n\r\s]+", "", book[linenum]) + "\n\t</name>\n")
        
                                target.write("<stat>" + book[linenum + 1] + "</stat>")
                                target.write("<desc>")
                                linenum += 2
                        else:
                                target.write(book[linenum])
                                linenum += 1
                except IndexError:
                        target.write("")
                        linenum += 1

			
	target.write("</desc></advantage>\n")
	target.write("</ADVANTAGES>\n")
target.close()
print("-----Done-----")
