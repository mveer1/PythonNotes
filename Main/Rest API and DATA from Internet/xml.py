import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url ')
xml= urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml.decode())
counts = tree.findall('.//count')
print('Count:',len(counts))
sum=0
for x in counts:
    sum=sum+int(x.find('count').text)
print('Sum is ',sum)

#holy fuck project
