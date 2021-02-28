# Класс для создания одного узла дерева. Содержит строку данных, и ссылки на два других объекта
class Tree:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other

    def __gt__(self, other):
        return self.name > other

    def __eq__(self, other):
        return self.name == other

    # добавляем данные в левый дочерний узел
    def add_left(self, data):
        self.left = data

    # добавляем данные в правый дочерний узел
    def add_right(self, data):
        self.right = data

    # запрашиваем данные из левого дочернего узла
    def get_left(self):
        return self.left

    # запрашиваем данные из правого дочернего узла
    def get_right(self):
        return self.right

    # список ссылок на дочерние узлы
    def keys(self):
        return [self.left, self.right]


# получаем на вход ссылку на дерево и строку, рекурсивно обходим дерево,
# выбираем место (см. Д.Кнут, 3 том, главы про "Поиск", принципы работы с бинарными деревьями)
# и добавляем новый узел с указанной строкой
def process(tree, name):
    if name == tree:
        return

    elif name > tree:
        temp_tree = tree.get_right()
        if temp_tree != None:
            process(temp_tree, name)
        else:
            tree.add_right(Tree(name))
    elif name < tree:
        temp_tree = tree.get_left()
        if temp_tree != None:
            process(temp_tree, name)
        else:
            tree.add_left(Tree(name))
    return


# получаем на вход ссылку на дерево и представляем дерево пользователю в виде массива массивов.
# только для вывода на экран, не для дальнейшего использования в коде
def show(tree):
    res = "[" + str(tree) + ":"
    res2 = []

    for k in tree.keys():
        if k != None:
            res2.append(show(k))
        else:
            res2.append("''")

    res = res + ",".join(res2) + "]"
    return(res)


# Избыточная переменная counter, только для удовлетворения любопытства - сколько элементов из всех имеющихся
# просмотрит программа, в процессе поиска нужной строки. Если хочется посмотреть - надо снять
# символы комментария во всех строках, где упоминается переменная counter
# counter = 0

# Рекурсивный поиск заданной строки по дереву. Логику обхода дерева см. Д.Кнут, 3 том, главы про "Поиск",
# принципы работы с бинарными деревьями. Функция вернет True или False
def search(tree, name):
#    global counter
#    counter = counter + 1

    res = False
    if name == tree:
        return True

    elif name > tree:
        temp_tree = tree.get_right()
        if temp_tree != None:
            res = search(temp_tree, name)

    elif name < tree:
        temp_tree = tree.get_left()
        if temp_tree != None:
            res = search(temp_tree, name)

    return res


# тело программы
# задаем список строк, на основе которых будет заполняться дерево
l = ['Ella', 'Anna', 'Una', 'Arina', 'Miranda', 'Tanna', 'Flora', 'Allegra' ,'Fred']
# создаем корневой узел дерева вручную
t = Tree(l[0])

# проходим по списку и добавляем каждую строку в дерево
for name in l[1:]:
    process(t, name)

# смотрим, что получилось
print("RES: " + show(t))
# Попробуем найти в дереве произвольную строку
print(search(t, 'Anna'))
# print(counter)

