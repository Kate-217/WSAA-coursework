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
    
#The names of the tags for ex.8    
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]
 
 # 4. Modify the program to print out each of the trainscodes.
 # I.e. find the listings and iterate through them 
 # to print each traincode out. Check it works 
 

#objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
#for objTrainPositionsNode in objTrainPositionsNodes:
#    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
#    traincode = traincodenode.firstChild.nodeValue.strip()
#    print (traincode)

# 5. Comment out the print and modify the program 
# so that it prints out the latitudes

objTrainPositionsNodes = doc.getElementsByTagName('objTrainPositions')
for objTrainPositionsNode in objTrainPositionsNodes:
     TrainLatitudenodes = objTrainPositionsNode.getElementsByTagName('TrainLatitude').item(0)
     TrainLatitude = TrainLatitudenodes.firstChild.nodeValue.strip()
     print(TrainLatitude)
     
# 6. Store this data into a CSV.

with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
 
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        
        # get TrainCode
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        if traincodenode and traincodenode.firstChild:
            traincode = traincodenode.firstChild.nodeValue.strip()
            dataList.append(traincode)
        else:
            dataList.append("N/A")  # Placeholder for missing data
        # write data
        train_writer.writerow(dataList)
        
# 8. At the top of the program make an array called retrieveTags that will
# store all the names of the tags we want to retrieve. 

with open('week03_train_all_tags.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
 
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        
        # get all data
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        # write data
        train_writer.writerow(dataList)
        
  
    
    

