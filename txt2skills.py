#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

print("Starting .txt Extraction")




page = [[]]
pIndex = 0

c0 = ""
c1 = ""
c2 = ""


master = ""
fullPages = []


count = 0


with open(sys.argv[1]) as f:
	book = f.readlines()
	

	for linenum in range(len(book)):
		if len(book[linenum]) == 2:		# Pages are seperated by 3 newlines
			if count == 2:
				pIndex += 1
				page.append([])	
				count = 0
			else:
				count += 1
		else:
			page[pIndex].append(book[linenum])

for content in page:
	for linenum in range(len(content)):
		content[linenum] = re.sub("\r\n", "", content[linenum])
		if linenum != 0:
			offset = 0
			for letternum in range(len(content[linenum])):
				if letternum == 0 and content[linenum][letternum] == " " and content[linenum][letternum + 2] != " ":
					offset = 1
				elif letternum < 44:
					c0 += content[linenum][letternum]
				elif letternum < 88:
					c1 += content[linenum][letternum]
				elif letternum >= 88:
					c2 += content[linenum][letternum]
			c0 += " "
			c1 += " "
			c2 += " "
	fullPages.append(c0 + c1 + c2)

	i = len(fullPages) - 1
	
	# Fix issues such as "Traits you must pos- sess before"
	fullPages[i] = re.sub( "(?<=[a-z])\-[\s]+", "", fullPages[i] )

	# Seperate Skills
	fullPages[i] = re.sub( "([\s]+|^)(?=([a-zA-Z]*[\s][a-zA-Z/†]+)[\s]+(IQ|DX|Will|Per|HT)/)", "<>", fullPages[i] )

	# Remove superfluous whitespace
	fullPages[i] = re.sub( '\s+', ' ', fullPages[i] ).strip()

	# Introduce newlines between skills
	fullPages[i] = re.sub( "<>", "\n\n", fullPages[i] )

	# Remove spaces at start of some skill names
	fullPages[i] = re.sub( "(?<=\n)[\s]+", "\n", fullPages[i] )
	
	master += fullPages[i]
	c0 = c1 = c2 = ""


print("Writing to file...")


target = open("output.txt", 'w')
target.truncate()


for page in fullPages:
	target.write(page)

target.close()

	 


#print(fullPages[int(sys.argv[2])] + fullPages[int(sys.argv[2]) + 1] + fullPages[int(sys.argv[2]) + 2] + fullPages[int(sys.argv[2]) + 3])
print("Done")
