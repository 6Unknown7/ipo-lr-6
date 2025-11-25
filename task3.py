count = int(input('Введите количество строки: '))
if (count <= 0):
    print('Ошибка')
else:
    list = []
    for i in range(count):
        string = input('\nВведите строки:')
        list.append(string)
    print(list)
#доделать 