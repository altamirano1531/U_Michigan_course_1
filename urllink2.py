
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = ' http://py4e-data.dr-chuck.net/comments_588168.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    #print(tag)
    line = tag.decode().strip()
    val = re.findall('[0-9]+', line)  
    total = total + int(val[0])
print(total)
