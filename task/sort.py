import pandas as pd
import xml.etree.ElementTree as ET
import csv

#csv file
csvfile = pd.read_csv("data/users.csv")
csvfile.to_csv('output/csvusers.csv', index=False)


# xml file
xmlparse = ET.parse('data/users.xml')
root = xmlparse.getroot()

cols = ["userid", "firstname", "surname", "username", "type", "lastlogintime"]
rows = []

for i in root:
    userid = i.find('userid').text
    firstname = i.find('firstname').text
    surname = i.find('surname').text
    username = i.find('username').text
    type = i.find('type').text
    lastlogintime = i.find('lastlogintime').text

    rows.append(
        {
            "userid": userid,
            "firstname": firstname,
            "surname": surname,
            "username": username,
            "type": type,
            "lastlogintime": lastlogintime
        }
    )

df = pd.DataFrame(rows, columns=cols)
df.to_csv('output/xmlusers.csv', index=False)


#json file
jfile = pd.read_json('data/users.json')
jfile.to_csv('output/jsonusers.csv', index=False)




#combined csv
data1 = 'output/csvusers.csv'
data2 = 'output/xmlusers.csv'
data3 = 'output/jsonusers.csv'


li = [data1, data2, data3]
combined_csv = pd.concat([pd.read_csv(f) for f in li])
combined_csv.sort_values(['userid'], axis=0, ascending=[True], inplace=True)
combined_csv.to_csv('output/final_output.csv', index=False, encoding='utf-8-sig')
combined_csv.to_csv('result/users.csv', index=False, encoding='utf-8-sig')


outputfile = pd.read_csv('output/final_output.csv')
outputfile.to_json(path_or_buf='result/users.json', orient='records', lines=True)


# converting csv to xml 
f = open('output/final_output.csv')
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row)
f.close()

def convert_row(row):
    return """<Users>
    <User>
        <userid>%s</userid>
        <firstname>%s</firstname>
        <surname>%s</surname>
        <username>%s</username>
        <type>%s</type>
        <lastlogintime>%s</lastlogintime>
    </User>
    """% (row[0], row[1], row[2], row[3], row[4], row[5])

with open('result/users.xml', 'w') as fn:
    fn.write('\n'.join([convert_row(row) for row in data[1:]]))
