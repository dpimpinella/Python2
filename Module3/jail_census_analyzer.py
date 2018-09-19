import csv

total_black_inmates = 0
total_white_inmates = 0

file = open ('9_2018_ACJ_daily_census_data.csv', newline='')
reader = csv.DictReader(file)

for row in reader:
    if row['Date'] == '2018-09-17':
        if row['Race'] == 'B':
            total_black_inmates += 1
        if row['Race'] == 'W':
            total_white_inmates += 1

file.close()

print("Total inmates: ", total_white_inmates + total_black_inmates)
print("Total white inmates: ", total_white_inmates)
print("Total black inmates: ", total_black_inmates)