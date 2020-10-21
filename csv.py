


with open('csv.csv', 'r') as name_list:
    name_list = name_list.read().splitlines()


    for line in name_list:
        row_parsed = line.split(",")
        print(row_parsed[0] + " is " + row_parsed[1] + " and is " + row_parsed[2] + " years old.")


