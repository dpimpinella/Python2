# Read in CSV file saved locally.
# MUST BE IN SAME DIRECTORY AS THE FILE.
file = open('9_2018_ACJ_daily_census_data.csv')

# Read in the first line of the file, cast it to a string, and then split the 
# string where there is a comma to get the headers from each column.
headers = str(file.readline()).split(',')

# We are interested in the racial make up of those who are incarcerated.
# Make a variable to store the number of inmates in each category, plus a 
# variable for the the total.
num_black = 0
num_white = 0
num_not_white_or_black = 0
total = 0


# Read in each line of the CSV using a for loop. 
for line in file:
        line = str(file.readline()).split(',')
        # Zip the two lists (headers and line) and form a dictionary.
        # An example of the output is below:
        # {'Age at Booking': '22',
        # 'Current Age\n': '24\n',
        # 'Date': '2018-09-01', 
        # 'Gender': 'M',
        # 'Race': 'B', '_id': '2'}
        line_data =  dict(zip(headers,line))
        # Use 'Race' as a key from the line_data dictionary, use if/elif/else 
        # to tally the results.
        if line_data['Race'] == 'B':
            num_black += 1
        elif line_data['Race'] == "W":
            num_white += 1
        else:
            num_not_white_or_black += 1
        total += 1


print('Number of incarcerated people who are black:', num_black)
print('Number of incarcerated people who are white:', num_white)
print('Number of incarcerated people who are not white or black:', num_not_white_or_black)
print('Total incarcerated:', total)










