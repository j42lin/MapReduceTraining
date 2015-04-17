#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter=' ')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    for line in reader:
        if len(line) == 8:
            link = line[5]
            hit = 1
            writer.writerow([link, hit])
            #print "\"{0}\"\t{1}".format(link, hit)
            

test_text = """10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 9157"""

if __name__ == "__main__":
    #import StringIO
    #sys.stdin = StringIO.StringIO(test_text)
    mapper()
    #sys.stdin = sys.__stdin__
