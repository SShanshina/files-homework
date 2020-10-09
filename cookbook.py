from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    recipes = file.readlines()


def split(my_list, delimiter='\n'):
    result = [[]]
    for item in my_list:
        if item == delimiter:
            result.append([])
        else:
            result[-1].append(item)
    return result


cook_book = {}
for my_list in split(recipes):
    for element in my_list:
        element = element.strip()
        dish_name = my_list[0].strip()
        ing_number = my_list[1].strip()
        ing_list = my_list[2:]
        dict_list = []
    for ing in ing_list:
        ing = ing.split('|')
        ing_name = ing[0].strip()
        quantity = int(ing[1].strip())
        measure = ing[2].strip()
        ing_dict = {'ingredient_name': ing_name, 'quantity': quantity, 'measure': measure}
        dict_list.append(ing_dict)
        cook_book[dish_name] = dict_list

pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    dishes = dishes.split(',')
    key_list = []
    quantity_list = []
    shop_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            key = ingredient['ingredient_name']
            key_list.append(key)
            ing_quantity = ingredient['quantity']
            ing_quantity = ing_quantity * person_count
            if ing_quantity in quantity_list:
                ing_quantity = ing_quantity * quantity_list.count(ing_quantity)
                quantity_list.append(ing_quantity)
            else:
                quantity_list.append(ing_quantity)
            ing_measure = ingredient['measure']
            shop_dict[key] = {'quantity': ing_quantity, 'measure': ing_measure}
    return shop_dict


pprint(get_shop_list_by_dishes((input('Введите названия блюд через запятую: ')), (int(input('Введите количество персон: ')))))