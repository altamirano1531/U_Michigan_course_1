
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = input('Enter count:')
position = input('Enter position:')

times = 0

while(times < int(count)):
    times = times + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[int(position)-1]
    url = tag.get('href', None)
    
print(url)

# #url = input('Enter - ')
# #url = 'http://py4e-data.dr-chuck.net/'
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

