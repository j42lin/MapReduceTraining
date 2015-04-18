#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    #writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    maxHitRate = 0
    hitRate = 0
    linkWithMaxHit = None
    oldKey = None

    for line in reader:
        if len(line) == 2:
            thisKey, thisHitRate = line
            if oldKey and oldKey != thisKey:
                #writer.writerow([oldKey, hitRate])
                print "{0}\t{1}".format(oldKey, hitRate)
                if maxHitRate < hitRate:
                    maxHitRate = hitRate
                    linkWithMaxHit = oldKey
                hitRate = 0

            oldKey = thisKey
            hitRate += int(thisHitRate)
            
    if oldKey != None:
        #writer.writerow([oldKey, hitRate])
        print "{0}\t{1}".format(oldKey, hitRate)
        if maxHitRate < hitRate:
            maxHitRate = hitRate
            linkWithMaxHit = oldKey       

    #writer.writerow([linkWithMaxHit, maxHitRate])
    print "{0}\t{1}".format(linkWithMaxHit, maxHitRate)
            

test_text = """"GET / HTTP/1.1"\t1
"GET /favicon.ico HTTP/1.1"\t2"""

if __name__ == "__main__":
    #import StringIO
    #sys.stdin = StringIO.StringIO(test_text)
    mapper()
    #sys.stdin = sys.__stdin__
