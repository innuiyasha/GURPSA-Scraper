import sys
import re

print("Starting .txt Extraction")

with open(sys.argv[1]) as f:
	book = f.readlines()
	something = ""
	
	target = open("target.txt", 'w')
	target.truncate()

	for lines in book:
		something = re.sub("(</div>)","\n",something)
		something = re.sub("(<[a-zA-Z0-9\+\-/\(\)\.,_\":!?=\s{}\[\]']*>)","", something)
		print(something)
		target.write(something)
	target.close()
