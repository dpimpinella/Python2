names_list = []

with open('people.txt') as input_file:
    header = input_file.readline()
    for line in input_file:
        name_and_age = str(line).split(',')
        names_list.append(name_and_age)

names_list.sort(key = lambda x: x[1])

with open('people_sorted.txt', 'w') as output_file:
    output_file.write(header)
    for item in names_list:
        output_line = ",".join(item)
        output_file.write(output_line)

        
        

