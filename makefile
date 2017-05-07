all:
	python notriangles.py Advantages.html
	python notriangles.py Skills.html
	python advantageExtractor.py Advantages.txt
	python skillExtractor.py Skills.txt

skills:
	python notriangles.py Skills.html
	python skillExtractor.py Skills.txt

advantages:
	python notriangles.py Advantages.html
	python advantageExtractor.py Advantages.txt

clean:
	rm Advantages.txt Skills.txt Advantages.xml Skills.xml

