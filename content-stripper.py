#http://bigghostnahmean.blogspot.co.uk/

import sys
import os
import urllib2
import HTMLParser
from bs4 import BeautifulSoup
import networkx as nx

ROOT_URL = sys.argv[1]

OUT = ROOT_URL[7:].replace('/', '-').replace('.','-') + 'raw.txt'
print OUT

hdrs = { 'User-Agent': "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11" }

#First create the Request object, using the headers argument to change the UserAgent.
req = urllib2.Request(ROOT_URL, headers = hdrs)
#use the Request Object to fetch the page.

try:
    page = urllib2.urlopen(req)
except urllib2.URLError:
    print "Failed to fetch " + ROOT_URL

try:
    soup = BeautifulSoup(page)
except HTMLParser.HTMLParseError:
    print 'Failed to parse ' + item

p_tags = []

#for p in soup.find_all('p'):
 #   print p.get_text()

paras = soup.find_all('p')

for p in paras:
    copy = p.get_text()
    copy = copy.encode("iso-8859-1", "ignore")
    #print type(copy)
    p_tags.append(copy)

finalText = ' '.join(p_tags)
text_file = open(OUT, "w")
text_file.write(finalText)
text_file.close()