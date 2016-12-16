#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re

print("Starting .txt Extraction")

with open(sys.argv[1]) as f:
	book = f.readlines()
	something = ""
	
	output = re.sub(".html", ".txt", sys.argv[1])

	target = open(output, 'w')
	target.truncate()

	for lines in book:
		something = re.sub("(</div>)","\n", lines)
		something = re.sub("(<[a-zA-Z0-9\+\-/\(\)\.,_\":!?=\s{}\[\]']*>)","", something)
		print(something)
		target.write(something)
	target.close()
