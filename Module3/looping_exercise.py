file = open('looping_exercise.txt', 'w')

num_Rows = 11
count_to = 10


for y in list(range(0,num_Rows)):
    for x in list(range(0,count_to + 1)):
        file.write(str(x))
    count_to = count_to - 1    
    file.write('\n')

file.flush()
file.close()
