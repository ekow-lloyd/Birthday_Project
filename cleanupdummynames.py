import json
try:
    with open ("bDay_db.json", 'r') as readFile:
        bday = json.load(readFile)

    bday.pop("shrek")

    with open ('bDay_db.json', 'w')as writeFile:
        bday = json.dump(bday, writeFile)
except KeyError:
    print("object not present in database")