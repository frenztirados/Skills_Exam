import json
import csv

with open('vaccination.json') as json_file:
    data = json.load(json_file)

vaccination_data = data['records']
vaccinejson = open('vaccinejson.csv', 'w')

csvwriter=csv.writer(vaccinejson)

count = 0
for vaccine in vaccination_data:
    if count == 0:

        head = vaccine.keys()
        csvwriter.writerow(head)
        count += 1
    csvwriter.writerow(vaccine.values())
vaccinejson.close()