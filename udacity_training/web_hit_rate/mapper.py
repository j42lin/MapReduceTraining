#!/usr/bin/python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter=' ')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    urlPrefix = "http://the-associates.co.uk"
    wwwUrlPrefix = "http://www.the-associates.co.uk"
    regexPattern = "^{0}|{1}".format(wwwUrlPrefix, urlPrefix)
    dbExportLink = "/database/export.php"
    for line in reader:
        if len(line) == 8:
            httpData = line[5]
            httpDataTuple = httpData.split(" ")
            if len(httpDataTuple) < 3:
                continue
            rawLink = httpDataTuple[1]

            #db export workaround
            if rawLink[:len(dbExportLink)] == dbExportLink:
                rawLink = dbExportLink
            
            if rawLink == urlPrefix or rawLink == wwwUrlPrefix:
                rawLink += '/'

            link = re.sub(regexPattern, "", rawLink);

            writer.writerow([link, 1])
            #print "\"{0}\"\t{1}".format(link, 1)
            

test_text = """10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 9157
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET http://www.the-associates.co.uk HTTP/1.1" 200 9157
10.224.104.45 - associates [21/Jan/2011:04:04:52 -0800] "GET /database/export.php?c%5B%5D=firstname&c%5B%5D=lastname&c%5B%5D=publication&c%5B%5D=email&c%5B%5D=email2&person%5B%5D=465&person%5B%5D=89&person%5B%5D=179&person%5B%5D=77&person%5B%5D=325&person%5B%5D=473&person%5B%5D=511&person%5B%5D=355&person%5B%5D=602&person%5B%5D=299&person%5B%5D=36&person%5B%5D=86&person%5B%5D=508&person%5B%5D=342&person%5B%5D=169&person%5B%5D=556&person%5B%5D=588&person%5B%5D=128&person%5B%5D=381&person%5B%5D=191&person%5B%5D=504&person%5B%5D=315&person%5B%5D=321&person%5B%5D=114&person%5B%5D=20&person%5B%5D=208&person%5B%5D=577&person%5B%5D=183&person%5B%5D=148&person%5B%5D=346&person%5B%5D=123&person%5B%5D=415&person%5B%5D=247&person%5B%5D=219&person%5B%5D=387&person%5B%5D=561&person%5B%5D=397&person%5B%5D=599&person%5B%5D=244&person%5B%5D=356&person%5B%5D=362&person%5B%5D=249&person%5B%5D=318&person%5B%5D=295&person%5B%5D=580&person%5B%5D=590&person%5B%5D=319&person%5B%5D=65&person%5B%5D=594&person%5B%5D=477&person%5B%5D=250&person%5B%5D=554&person%5B%5D=576&person%5B%5D=115&person%5B%5D=375&person%5B%5D=486&person%5B%5D=73&person%5B%5D=75&person%5B%5D=111&person%5B%5D=510&person%5B%5D=543&person%5B%5D=185&person%5B%5D=328&person%5B%5D=569&person%5B%5D=140&person%5B%5D=585&person%5B%5D=173&person%5B%5D=598&person%5B%5D=433&person%5B%5D=429&person%5B%5D=487&person%5B%5D=431&person%5B%5D=161&person%5B%5D=203&person%5B%5D=303&person%5B%5D=274&person%5B%5D=553&person%5B%5D=232&person%5B%5D=485&person%5B%5D=88&person%5B%5D=130&person%5B%5D=574&person%5B%5D=34&person%5B%5D=364&person%5B%5D=170&person%5B%5D=290&person%5B%5D=555&person%5B%5D=79&person%5B%5D=210&person%5B%5D=410&person%5B%5D=246&person%5B%5D=509&person%5B%5D=499&person%5B%5D=327&person%5B%5D=488&person%5B%5D=72&person%5B%5D=528&person%5B%5D=430&person%5B%5D=309&person%5B%5D=312&person%5B%5D=258&person%5B%5D=396&person%5B%5D=529&person%5B%5D=589&person%5B%5D=268&person%5B%5D=451&person%5B%5D=224&person%5B%5D=113&person%5B%5D=251&person%5B%5D=58&person%5B%5D=322&person%5B%5D=37&person%5B%5D=527&person%5B%5D=164&person%5B%5D=80&person%5B%5D=606&person%5B%5D=68&person%5B%5D=443&person%5B%5D=587&person%5B%5D=242&person%5B%5D=288&person%5B%5D=50&person%5B%5D=253&person%5B%5D=350&person%5B%5D=565&person%5B%5D=336&person%5B%5D=372&person%5B%5D=302&person%5B%5D=76&person%5B%5D=524&person%5B%5D=213&person%5B%5D=496&person%5B%5D=62&person%5B%5D=343&person%5B%5D=426&person%5B%5D=110&person%5B%5D=158&person%5B%5D=551&person%5B%5D=157&person%5B%5D=417&person%5B%5D=199&person%5B%5D=283&person%5B%5D=611&person%5B%5D=500&person%5B%5D=176&person%5B%5D=305&person%5B%5D=188&person%5B%5D=502&person%5B%5D=39&person%5B%5D=83&person%5B%5D=550&person%5B%5D=293&person%5B%5D=493&person%5B%5D=195&person%5B%5D=248&person%5B%5D=109&person%5B%5D=610&person%5B%5D=498&person%5B%5D=591&person%5B%5D=54&person%5B%5D=541&person%5B%5D=187&person%5B%5D=59&person%5B%5D=162&person%5B%5D=201&person%5B%5D=218&person%5B%5D=469&person%5B%5D=538&person%5B%5D=3&person%5B%5D=172&person%5B%5D=560&person%5B%5D=304&person%5B%5D=271&person%5B%5D=152&person%5B%5D=464&person%5B%5D=233&person%5B%5D=81&person%5B%5D=353&person%5B%5D=544&person%5B%5D=492&person%5B%5D=536&person%5B%5D=287&person%5B%5D=90&person%5B%5D=13&person%5B%5D=373&person%5B%5D=280&person%5B%5D=609&person%5B%5D=432&person%5B%5D=460&person%5B%5D=334&person%5B%5D=241&person%5B%5D=193&person%5B%5D=494&person%5B%5D=386&person%5B%5D=209&person%5B%5D=189&person%5B%5D=584&person%5B%5D=467&person%5B%5D=240&person%5B%5D=107&person%5B%5D=44&person%5B%5D=87&person%5B%5D=298&person%5B%5D=63&person%5B%5D=177&person%5B%5D=313&person%5B%5D=314&person%5B%5D=579&person%5B%5D=402&person%5B%5D=600&person%5B%5D=35&person%5B%5D=517&person%5B%5D=351&person%5B%5D=67&person%5B%5D=586&person%5B%5D=200&person%5B%5D=144&person%5B%5D=497&person%5B%5D=281&person%5B%5D=361&person%5B%5D=393&person%5B%5D=132&person%5B%5D=284&person%5B%5D=225&person%5B%5D=450&person%5B%5D=481&person%5B%5D=272&person%5B%5D=4&person%5B%5D=507&person%5B%5D=228&person%5B%5D=206&person%5B%5D=573&person%5B%5D=378&person%5B%5D=458&person%5B%5D=359&person%5B%5D=134&person%5B%5D=234&person%5B%5D=159&person%5B%5D=568&person%5B%5D=149&person%5B%5D=345&person%5B%5D=243&person%5B%5D=332&person%5B%5D=192&person%5B%5D=341&person%5B%5D=301&person%5B%5D=597&person%5B%5D=603&person%5B%5D=474&person%5B%5D=61&person%5B%5D=405&person%5B%5D=408&person%5B%5D=175&person%5B%5D=279&person%5B%5D=82&person%5B%5D=167&person%5B%5D=340&person%5B%5D=259&person%5B%5D=438&person%5B%5D=437&person%5B%5D=245&person%5B%5D=434&person%5B%5D=335&person%5B%5D=552&person%5B%5D=205&person%5B%5D=513&person%5B%5D=389&person%5B%5D=277&person%5B%5D=40&person%5B%5D=435&person%5B%5D=333&person%5B%5D=420&person%5B%5D=231&person%5B%5D=116&person%5B%5D=360&person%5B%5D=416&person%5B%5D=237&person%5B%5D=407&person%5B%5D=230&person%5B%5D=181&person%5B%5D=112&person%5B%5D=326&person%5B%5D=70&person%5B%5D=141&person%5B%5D=212&person%5B%5D=220&person%5B%5D=154&person%5B%5D=129&person%5B%5D=289&person%5B%5D=186&person%5B%5D=51&person%5B%5D=255&person%5B%5D=595&person%5B%5D=409&person%5B%5D=484&person%5B%5D=607&person%5B%5D=503&person%5B%5D=155&person%5B%5D=202&person%5B%5D=392&person%5B%5D=165&person%5B%5D=223&person%5B%5D=221&person%5B%5D=338&person%5B%5D=229&person%5B%5D=197&person%5B%5D=601&person%5B%5D=593&person%5B%5D=506&person%5B%5D=273&person%5B%5D=446&person%5B%5D=608&person%5B%5D=604&person%5B%5D=525&person%5B%5D=532&person%5B%5D=596&person%5B%5D=156&person%5B%5D=470&person%5B%5D=605&person%5B%5D=204&person%5B%5D=131&person%5B%5D=14&person%5B%5D=374&person%5B%5D=291&person%5B%5D=423&person%5B%5D=347&person%5B%5D=254&person%5B%5D=391&person%5B%5D=56&person%5B%5D=42&person%5B%5D=285&person%5B%5D=238&person%5B%5D=125&person%5B%5D=566&person%5B%5D=171&person%5B%5D=236&person%5B%5D=198&person%5B%5D=121&person%5B%5D=480&person%5B%5D=138&person%5B%5D=466&person%5B%5D=118&person%5B%5D=211&person%5B%5D=363&person%5B%5D=215&person%5B%5D=49&person%5B%5D=383&person%5B%5D=286&person%5B%5D=32&person%5B%5D=136&person%5B%5D=126&person%5B%5D=505&person%5B%5D=84&person%5B%5D=489&person%5B%5D=133&person%5B%5D=447&person%5B%5D=108&person%5B%5D=25&person%5B%5D=419&person%5B%5D=117&person%5B%5D=448&person%5B%5D=482&person%5B%5D=292&person%5B%5D=453&person%5B%5D=495&person%5B%5D=421&person%5B%5D=483&person%5B%5D=592&person%5B%5D=395&person%5B%5D=207&person%5B%5D=337&person%5B%5D=572&person%5B%5D=540&person%5B%5D=239&person%5B%5D=441&person%5B%5D=442 HTTP/1.1" 200 23975
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET http://the-associates.co.uk HTTP/1.1" 200 9157
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /images/filmpics/0000/1667/MARANTEU-2d.jpg HTTP/1.1" 200 9157
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /images/filmpics/0000/1669/MARANTEU-3d_thumb.jpg HTTP/1.1" 200 9157
10.216.113.172 - - [19/Mar/2010:04:10:55 -0700] "GET /images/filmpics/0000/1667/MARANTEU-2d_thumb.jpg HTTP/1.1" 304 -
10.216.113.172 - - [19/Mar/2010:04:10:55 -0700] "GET /images/filmpics/0000/1669/MARANTEU-3d_thumb.jpg HTTP/1.1" 200 74011
10.216.113.172 - - [19/Mar/2010:04:10:55 -0700] "GET /images/filmmediablock/289/MARANTEU-3d.jpg HTTP/1.1" 200 382510
"""

if __name__ == "__main__":
    #import StringIO
    #sys.stdin = StringIO.StringIO(test_text)
    mapper()
    #sys.stdin = sys.__stdin__
