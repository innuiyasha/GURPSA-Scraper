This scraper extracts information from a pdf excerpt of 'GURPS - 4th Edition Basic Character Set.' I then convert it into html with the below site, then scrape that for information. This generates a flawed XML file which then must be checked over by hand due to the simple fact that patterns are not perfectly followed by the authors aswell as small errors throughout the conversion process. This XML is then used in the GURPS repo to serve as a storage medium for skills and advantages.




The scrapper uses the html5 file generated from "www.zamzar.com/convert/pdf-to-txt/"

Then run "python notriangles.py <filename>" on that html file

Then use either "<advantageExtractor.py | skillExtractor.py> <filename>"
