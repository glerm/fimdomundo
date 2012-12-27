from BeautifulSoup import *
import urllib2

l=("http://www.sincronariodapaz.org/altera/CalculoKin/crono1B.php?dianterior=24&diaposterior=&mesf=12&anof=2012")
 
page = urllib2.urlopen(l)
soup = BeautifulSoup(page)

print soup
