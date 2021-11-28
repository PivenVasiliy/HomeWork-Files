from pprint import pprint
import os

path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        composition = []
        for item in range(counter):
            ingridient, quantity, measure = file.readline().split('|')
            composition.append(
                {'ingredient_name': ingridient, 'quantity': int(quantity), 'measure': measure}
            )
        cook_book[dish_name] = composition
        file.readline()
    print(f'cook_book =\n{cook_book}')

print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for item in cook_book[dish]:
            item['quantity'] *= person_count
            if item['ingredient_name'] not in shop_list:
                shop_list[item['ingredient_name']] = {'quantity': item['quantity'], 'measure': item['measure']}
            else:
                shop_list[item['ingredient_name']]['quantity'] += item['quantity']
    pprint(shop_list)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
