import time
import urllib.request as request
from xml.dom.minidom import parseString

def isVgrOnline():
    url = 'https://eyes.nasa.gov/dsn/data/dsn.xml'
    response = request.urlopen(url)
    xmldoc=parseString(response.read())
    #print(xmldoc)
    targets = xmldoc.getElementsByTagName("target")
    #print(targets)
    ret=False
    for target in targets:
        name = target.getAttribute("name")
        if name=="VGR1" or name=="VGR2":
            ret=True
    return ret

print("Is Vgr Online : "+str(isVgrOnline()))

