def my_cook_book():
    with open('file.txt', encoding='utf-8') as f:
        cook_book = dict()
        while True:
            dish = f.readline().strip()
            cook_book[dish] = []
            for _ in range(int(f.readline())):
                cook_book[dish].append(dict(zip(['ingredient_name', 'quantity', 'measure'],
                                                (f.readline().strip().split(' | ')))))
            if not f.readline():
                break
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    buy_list = {}
    for dish in dishes:
        for ingredients in my_cook_book()[dish]:
            if ingredients['ingredient_name'] in buy_list:
                ingredients['quantity'] = buy_list[ingredients['ingredient_name']]['quantity'] + \
                                          int(ingredients['quantity'])
            buy_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                        'quantity': int(ingredients['quantity']) * person_count}
    return buy_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))

