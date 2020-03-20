import urllib.request
import urllib.response


def geturl(url):
    u = urllib.parse.urlsplit(url)
    if url[-1] == '/':
        name = 'index.html'
    else:
        name = u.netloc.split('.')[0] + '.html'

    html = urllib.request.urlopen(url)
    htmlText = str(html.readlines())

    f = open(name, 'w')
    f.write(htmlText)
    f.close()
    

geturl('http://instagram.com/')

