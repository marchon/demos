# UrlLib.py
import urllib3

http = urllib3.PoolManager()


'''
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

print data
'''