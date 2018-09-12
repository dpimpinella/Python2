given_string = 'askaliceithinkshe\'llknow'

for position, letter in enumerate(given_string):
    if ((position%2) == 0):
        print(given_string[position], end = " ")