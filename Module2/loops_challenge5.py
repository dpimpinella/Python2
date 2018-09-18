listoflists = [['mn','pa','ut'],['b','p','c'],['echo','charlie','tango']]
labels = {"state":"US State Abbr: ", "element":"Chemical Element: ", "alpha":"Phonetic Call: "} 

keys = list(labels.keys())
print(keys)

for key in keys:

    # 2 problems: quotes in list of keys, using 'key' as variable in %s string concatenation
    # print(keys): ['state', 'element', 'alpha']  - quotes will break dictionary access
    k = key.strip("'")

    # print("%(key)s" %(labels)): will not work, will interpret 'key' literally, not as variable from for loop
    # create keyString to avoid this problem
    keyString = "%({})s".format(key)
    print(keyString %(labels))

