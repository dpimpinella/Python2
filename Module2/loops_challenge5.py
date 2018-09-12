listoflists = [['mn','pa','ut'],['b','p','c'],['echo','charlie','tango']]
labels = {"state":"US State Abbr: ", "element":"Chemical Element: ", "alpha":"Phonetic Call: "} 

keys = list(labels.keys())
print(keys)

for key in keys:
    k = key.strip("'")
    keyString = '%('+ key + ')s'
    print(keyString %(labels))

