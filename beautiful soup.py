from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_136889.html'
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#RETRIEVE ALL SPAN TAGS

tags = soup('span')
sum = 0
for tag in tags:
    x = tag.text
    sum = sum + int(x)
    
print("Sum..", sum)    