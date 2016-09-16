import urllib2  # works fine with Python 2.7.9 (not 3.4.+)
import json
import time
from datetime import datetime

d = {'AAPL' : 'NYSE', 'DIS' : 'NYSE'}

def fetchPreMarket(symbol, exchange):
    link = "http://finance.google.com/finance/info?client=ig&q="
    url = link+"%s:%s" % (exchange, symbol)
    u = urllib2.urlopen(url)
    content = u.read()
    data = json.loads(content[3:])
    info = data[0]
    i = str(info["t"])              # ticker name
    t = str(info["lt"])             # time stamp
    l = float(info["pcls_fix"])     # close price (previous trading day)
    p = float(info["l_fix"])            # stock price in pre-market (after-hours)
    return (i,t,l,p)

#p0 = 0

print len(d)

##def f(dictionary):
##    for key, value in dictionary.iteritems():
##        p0 = 0
##        while True:
##            i, t, l, p = fetchPreMarket(key,value)
##            if(p!=p0):
##                p0 = p
##                print("%s\t%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (i, t, l, p, p-l, (p/l-1)*100.))
##        #print (key, value)
##
##f(d)
