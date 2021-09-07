# imports
import csv, json
import xml.etree.ElementTree as ET

outputData = {}


def csvfile(filename):
    with open(f'{filename}.csv', newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    heading = data[0:1][0]
    data = data[1:]
    for i in range(len(data)):
        outputData[int(data[i][0])] = data[i]
    
    convertcsv(outputData, heading)
        

def convertcsv(outputData, heading):
    with open("output/output.csv", 'w') as f:
        fieldname = ['userid', 'firstname', 'surname', 'username', 'User', 'type', 'lastlogintime']
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        writer.writerow(outputData.keys())



def jsonfile(filename):
    f = open(f'{filename}.json',)
    jsonlist = json.load(f)
    
    for i in range(len(jsonlist)):
        outputData[int(jsonlist[i]['user_id'])] = jsonlist[i]

        

def xmlfile(filename):
    tree = ET.parse(f'{filename}.xml')
    root = tree.getroot()

    dic = {}
            
    for elem in root.findall('user'):
        for x in elem.iter():
            print(x)




if __name__ == "__main__":
    filename = "data/users"
    csvfile(filename) # converts to csvfile to dictionary
    # jsonfile(filename)  # converts to jsonfile to dictionary
    # xmlfile(filename) # converts to xmlfile to dictionary

    # for i in sorted(outputData.keys()):
    #     print(outputData[i])
    print(outputData)