# бинарное дерево на основе словарей
# vars
d = dict({ 'Jenna': {
    'Inna' : {
        'Sviet' : {},
        'Marat' : {}
    },
    'Valeria' : {
        'Olga' : {},
        'Anna' : {}
    }
} })

str1 = 'Inna'
str2 = 'Sveta'

# рекурсивный обход дерева, поиск заданной строки
def process(d, name):
    res = False
    for k in d.keys():
        if k == name:
            return True
        else:
            res = process(d[k], name)
        if res == True:
            break
    return res


# тело программы
print(process(d, str2))

