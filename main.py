import time
import urllib.request as request
from xml.dom.minidom import parseString
url = 'https://eyes.nasa.gov/dsn/data/dsn.xml'

r = int(time.time() / 5)
response = request.urlopen(url)
xmldoc=parseString(response.read())
print(xmldoc)
targets = xmldoc.getElementsByTagName("target")
print(targets)
for target in targets:
    name = target.getAttribute("name")
    print(name)
