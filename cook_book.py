import os
from pprint import pprint

path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path, encoding='utf-8') as file:
    cook_book = {}
    for menu in file:
        dish = menu.strip()
        count = int(file.readline().strip())
        temp_data = []
        for ingredients in range(count):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            temp_data.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.replace('\n', '')})
        cook_book[dish] = temp_data
        file.readline()
# pprint(cook_book)
# pprint(len(cook_book))

def get_shop_list_by_dishes(dishes, person_count):
  res = {}
  for i in dishes:
    for j in cook_book[i]:
      if j['ingredient_name'] in res.keys():
        res[j['ingredient_name']]['quantity'] += j['quantity']
      else:
        res[j['ingredient_name']] = {}
        res[j['ingredient_name']]['measure'] = j['measure']
        res[j['ingredient_name']]['quantity'] = j['quantity']*person_count
  return res

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


