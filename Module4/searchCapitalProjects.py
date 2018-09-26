import json

def search(properties):
    for key in searchJSON.keys():
        if searchJSON[key] == properties[key]:
            printProject(properties) 

def printProject(properties):
    print("#### PROJECT DETAILS ####")
    keys = properties.keys()
    for key in keys:
        print(key,':', properties[key])
    print('\n')

f = open('cgcapitalprojects_img.geojson.json', 'r')
capitalProjectsJSON = json.load(f)

searchFile = open('searchSpecifications.json','r')
searchJSON = json.load(searchFile)

for p in capitalProjectsJSON['features']:
    search(p['properties'])






