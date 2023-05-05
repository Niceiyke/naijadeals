import json

with open('jumia.json','r',encoding="utf8") as data:
    x=json.load(data)

    for i in x:
        print(i['name'])