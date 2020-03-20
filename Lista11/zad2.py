import urllib.response
import urllib.request

x = urllib.request.urlopen('http://tiny.cc/180wiz').geturl()
print(x)