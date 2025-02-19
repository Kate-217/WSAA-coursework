import requests
import csv
from xml.dom.minidom import parseString
url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# output to console: 
#print(doc.toprettyxml())

# if I need to store XML
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)
    

