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
 
 # 4. Modify the program to print out each of the trainscodes.
 # I.e. find the listings and iterate through them 
 # to print each traincode out. Check it works 
 
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    print (traincode)
    
    

