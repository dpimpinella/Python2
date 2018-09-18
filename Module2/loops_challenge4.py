first_range = range(1,5)
second_range = range(5,8)

for multiple1 in first_range:
    for multiple2 in second_range:
        product = multiple1 * multiple2
        print("%d|%d|%d" %(multiple1,multiple2,product))