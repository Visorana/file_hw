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


print(my_cook_book())
