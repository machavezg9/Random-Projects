import urllib2  # works fine with Python 2.7.9 (not 3.4.+)
import json
import time
from datetime import datetime

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
 
p0 = 0
while True:
    print("Ticker\tTime Stamp\t\tClose\tCurrent\tChange\t%Change")
    i, t, l, p = fetchPreMarket("AAPL","NASDAQ")
    if(p!=p0):
        p0 = p
        print("%s\t%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (i, t, l, p, p-l,
                                                 (p/l-1)*100.))
    i, t, l, p = fetchPreMarket("DIS","NYSE")
    if(p!=p0):
        p0 = p
        print("%s\t%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (i, t, l, p, p-l,
                                                 (p/l-1)*100.))
    i, t, l, p = fetchPreMarket("TWLO","NYSE")
    if(p!=p0):
        p0 = p
        print("%s\t%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (i, t, l, p, p-l,
                                                 (p/l-1)*100.))
    i, t, l, p = fetchPreMarket(".INX","INDEXSP")
    if(p!=p0):
        p0 = p
        print("%s\t%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (i, t, l, p, p-l,
                                                 (p/l-1)*100.))
    i, t, l, p = fetchPreMarket(".DJI","INDEXDJX")
    if(p!=p0):
        p0 = p
        print("%s\t%s\t%.2f %.2f %+.2f %+.2f%%" % (i, t, l, p, p-l,
                                                 (p/l-1)*100.))
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(60)
