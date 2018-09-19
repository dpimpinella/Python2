import csv

total_black_inmates = 0
total_white_inmates = 0

file = open ('9_2018_ACJ_daily_census_data.csv')
reader = csv.DictReader()

for row in reader:
    if row['date'] == '2018-09-17':
        if 