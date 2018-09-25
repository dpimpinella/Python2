
file = open('9_2018_ACJ_daily_census_data.csv')
headers = str(file.readline()).split(',')

num_black = 0
num_white = 0
total = 0
line ="line text"

for x in file:
        line = str(file.readline()).split(',')
        line_data =  dict(zip(headers,line))
        if line_data['Race'] == 'B':
            num_black += 1
        elif line_data['Race'] == "W":
            num_white += 1
        total += 1


print('Number of black inmates:', num_black)
print('Number of white inmates:', num_white)
print('Total inmates:', total)










