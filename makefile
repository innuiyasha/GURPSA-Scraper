skills:
	python notriangles.py Skills.html
	python skillExtractor.py Skills.txt

advantages:
	python notriangles.py Advantages.html
	python advantageExtractor.py Advantages.txt

all:
	python notriangles.py Advantages.html
	python notriangles.py Skills.html
	python advantageExtractor.py Advantages.txt
	python skillExtractor.py Skills.txt

clean:
	rm Advantages.txt
	rm Skills.txt
	rm Advantages.xml
	rm Skills.xml

