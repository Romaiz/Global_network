import csv
import json


def csv_to_json(csv_file, json_file):
    jsonList = []
    with open(csv_file, encoding="utf-8") as csvf:
        csvreader = csv.DictReader(csvf)

        for row in csvreader:
            jsonList.append(row)
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonList, indent=4)
        jsonf.write(jsonString)


# csvFile = "GEODATASOURCE-COUNTRY-BORDERS.CSV"
# jsonFile = "GEODATASOURCE-COUNTRY-BORDERS.json"

# csv_to_json(csvFile, jsonFile)
