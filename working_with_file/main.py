from pprint import pprint

with open('working_with_file\list_of_dishes.txt', encoding= 'utf-8') as file:
    cook_book = {}
    couter = 0
    name_key = ''
    for line in file:
        couter += 1
        if line == '\n':
            couter = 0
            continue
        elif couter == 1:
            name_key = line[0:-1]
            cook_book[name_key] = []
        elif couter == 2:
            continue
        else:
            cook_book[name_key].append(
                {'ingredient_name': line.split()[0],
                 'quantity': line.split()[2], 
                 'measure': line.split()[4]}
            )
