#!usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import html5lib

url = "php.net"

r  = requests.get(url)

soup=BeautifulSoup(r.content,'html5lib')
#print(soup.prettify())
data_intro=[]
data_content=[]
t1=soup.find('div',attrs={'id':'intro'})
t2=soup.find('div',attrs={'id':'layout'})
for row in t1.find_all('div',attrs={'class':'blurb'}):
        d1={}
        d1['content']=row.p.text
        data_intro.append(d1)
for row in t2.find_all('div',attrs={'class':'newscontent'}):
        d2={}
        d2['url']=row.a['href']
        d2['content']=row.p.text
        data_content.append(d2)
print(data_intro)
