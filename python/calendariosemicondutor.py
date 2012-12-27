from BeautifulSoup import *
import urllib2

l=("http://www.sincronariodapaz.org/altera/CalculoKin/crono1B.php?dianterior=24&diaposterior=&mesf=12&anof=2012")
 
page = urllib2.urlopen(l)
soup = BeautifulSoup(page)
t = soup.find("table")

#dat = [ map(str, row.findAll("td")) for row in t.findAll("tr") ]


#print dat[0][0]

imgs=[]

for ana in soup.findAll('img'):
	imgs.append("http://sincronariodapaz.org/altera/CalculoKin" +(ana["src"][1:]))


print imgs

#print soup.prettify()
