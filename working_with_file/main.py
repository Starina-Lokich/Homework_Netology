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
                {'ingredient_name': line.split(' | ')[0],
                 'quantity': line.split(' | ')[1], 
                 'measure': line.split(' | ')[2][:-1]}
            )

def get_list_shop_by_dishes(dishes, person_count):
    dict_shop_by_dishes = {}
    for dish in dishes:
        for key_cook_book in cook_book.keys():
            if dish == key_cook_book:
                for ingredient in cook_book[dish]:
                    if ingredient['ingredient_name'] in dict_shop_by_dishes.keys():
                        dict_shop_by_dishes[ingredient['ingredient_name']]['quantity'] = \
                            dict_shop_by_dishes[ingredient['ingredient_name']]['quantity'] + int(ingredient['quantity']) * person_count
                    else:
                        dict_shop_by_dishes[ingredient['ingredient_name']] = {
                            'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count
                            }
                        # print(dict_shop_by_dishes)
    return dict_shop_by_dishes

dishesss = ['Оладьи', 'Глазунья']
pprint(get_list_shop_by_dishes(dishesss,2))