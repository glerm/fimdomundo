# -*- coding: utf-8 -*-

from BeautifulSoup import *
import urllib2

#abrindo do site############################################
#l=("http://www.sincronariodapaz.org/altera/CalculoKin/crono1B.php?dianterior=24&diaposterior=&mesf=12&anof=2012")
#page = urllib2.urlopen(l)
#soup = BeautifulSoup(page)


#teste local
soup = BeautifulSoup(open("teste.html"))

##################### metodo pra subtituir tags
#while True: 
#    td = soup.find('td')
#    if not td:
#        break
#    td.name = 'div'



t = soup.find("table")

#dat = [ map(str, row.findAll("td")) for row in t.findAll("tr") ]
#print dat[0][0]

imgs=[]
txt=[]

for ana in soup.findAll('img'):
	imgs.append("http://sincronariodapaz.org/altera/CalculoKin" +(ana["src"][1:]))


for img in soup.findAll('img'):
	table = img.findParents('table')[0]



stable = table



for e in stable.findAll('img'):
        e.extract()

table = stable("td")
t1=table[1]("font")[0]

t1.find("font").extract()
t1.find("b").extract()

print "<meta charset=\"UTF-8\">\n"
print imgs
print t1.prettify()
print "\n------------------------\n"
print table[2]
#print table[3]
#print tt

#print soup.prettify()
