import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags=soup('a')
list1=list()
rep=int(input('Enter how many times do you have to repeat '))
posstr=input('Enter the position to look for ')
pos=int(posstr)
for i in list(range(rep)):
    c=0
    for tag in tags:
        c+=1
        if c==pos:
            newurl=tag.get('href',None)
            newhtml=urllib.request.urlopen(newurl, context=ctx).read()
            newsoup=BeautifulSoup(newhtml, 'html.parser')
            newtags=newsoup('a')
            tags=newtags
            list1=tag.get('href', None).split('_')
            fname=list1[2].split('.')
print(fname[0])

#find a better way to collect the name than using split
