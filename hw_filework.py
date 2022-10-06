import os

cur_path = os.getcwd()
dir_name = 'files'
file_name = 'recipes.txt'
full_path = os.path.join(cur_path, dir_name, file_name)




# with open(full_path, 'rt', encoding='utf8') as file:
    # # cook_book = {}
    #
    # # ingredients = []
    # for line in file:
    #     name_blish = line.strip()
    #     structure_blish = {'ingredients_name': name_blish, 'employees':[]}
    #     qty_ingredients = file.readline()
    #     for i in range(int(qty_ingredients)):
    #         emp = file.readline()
    #         print(emp)
    #         ingredients, quantity, measure = emp.strip().split(' | ')
    #         structure_blish['employees'].append({'ingredients': ingredients,
    #                                              'quantity': quantity,
    #                                              'measure': measure})
    #         blank_line = file.readline()
    #         #         deps.append(dep)
    #     cook_book[name_blish] = ingredients.append(line)
    # print(cook_book)

# deps = []
'''cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    cook_book =
    {blish_name: [{ingredient_name:'', quantity:'', measure:''}
                  {ingredient_name:'', quantity:'', measure:''}
                  {ingredient_name:'', quantity:'', measure:''}]
    }
    '''
cook_book = {}
ingredients = []
with open (full_path, 'rt', encoding='utf8') as file:
    for l in file:
        blish_name = l.strip()  # Берем первую строку - название блюда
        # cook_book = {'blish_name': blish_name}  # Создаем словарь с ключом название блюда и списком со словарем
        cook_book = {blish_name : ingredients}
        ingredients_count = file.readline()  # Считываем кол-во ингридиентов в каждом блюде
        for qty_ingr in range(int(ingredients_count)):  # Цикл кол-во итераций равно кол-ву ингредиентов в каждом блюде
            ingr = file.readline()  # Считываем очередной ингредиент
            ingredient_name, quantity, measure = ingr.strip().split(' | ')  # распаковали строку в список на данные ингредиента
            # print(ingredient_name, quantity, measure)
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        print(cook_book)
# with open(full_path, 'rt', encoding='utf8') as file:
#     for l in file:
#         blish_name = l.strip()
#         dep = {"name": blish_name, "structure": []}
#         employees_count = file.readline()
#         for i in range(int(employees_count)):
#             emp = file.readline()
#             ingredient_name, quantity, measure = emp.strip().split(' | ')
#             dep["structure"].append({'ingredient_name': ingredient_name,
#                                      'quantity': quantity,
#                                      'measure': measure,
#                                      })
#         blank_line = file.readline()
#         deps.append(dep)
#
# print(deps)