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
    return dict_shop_by_dishes

with open('working_with_file\Бородино1.txt', encoding='utf-8') as f:
    all_lines = []
    lines_1 = f.readlines()
    lines_1 += ['Бородино1.txt\n']
    all_lines += [lines_1]
# pprint(lines_1)

with open('working_with_file\Бородино2.txt', encoding='utf-8') as f:
    lines_2 = f.readlines()
    lines_2 += ['Бородино2.txt\n']
    all_lines += [lines_2]
# pprint(lines_2)

with open('working_with_file\Бородино3.txt', encoding='utf-8') as f:
    lines_3 = f.readlines()
    lines_3 += ['Бородино3.txt\n']
    all_lines += [lines_3]
# pprint(lines_3)

with open('working_with_file\Test_document.txt', 'w', encoding='utf-8') as f:

    for lines in sorted(all_lines, key=len):
        f.write(''.join(lines[-1]))
        f.write(str(len(lines) - 1) + '\n')
        f.write(''.join(lines[:-1]))
# pprint(all_lines)

dishesss = ['Оладьи', 'Глазунья']
pprint(get_list_shop_by_dishes(dishesss,2))