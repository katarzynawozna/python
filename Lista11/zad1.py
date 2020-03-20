import urllib.request
import urllib.error

def url_on_server(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        print('Failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print ('Website is working fine')