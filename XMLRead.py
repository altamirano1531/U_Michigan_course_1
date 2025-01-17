import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


serviceurl = 'http://py4e-data.dr-chuck.net/comments_588170.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
tot = 0

for res in results:
    #N = res.find('name').text
    C = res.find('count').text
    tot = tot + int(C)

print('Count:', len(results))
print('Sum:', tot)
