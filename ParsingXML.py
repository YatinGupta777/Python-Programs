
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
ans = 0
for i in counts:
    ans += int(i.text)
    
print (ans)    