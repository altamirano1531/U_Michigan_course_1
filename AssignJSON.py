import urllib.request, urllib.parse, urllib.error
import json
import ssl


#serviceurl = input('Enter URL:')

serviceurl = 'http://py4e-data.dr-chuck.net/comments_588171.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', serviceurl)
uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

total = 0
count = 0
for item in js['comments']:
    total = total + int(item['count'])   
    count = count + 1

print('Count', count)
print('Sum', total)


