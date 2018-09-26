import json

def printProject(properties):
    print("#### PROJECT DETAILS ####")
    keys = properties.keys()
    for key in keys:
        print(key,':', properties[key])
    print('\n')

def assembleAreaList(properties):
    area = properties['area']
    if area =='':
        area = 'NO DATA'
        file.write(str(properties['id']))
        file.write('\n')
    if area not in areaList:
        areaList.append(area)

areaList = []

f = open('cgcapitalprojects_img.geojson.json', 'r')
res = json.load(f)

file = open('noAreaErrorLog','w')           
for p in res['features']:
    printProject(p['properties'])
    assembleAreaList(p['properties'])

print(areaList)

