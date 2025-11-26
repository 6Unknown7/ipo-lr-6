#Даниил

count = int(input('Введите количество строки: '))
if (count <= 0):
    print('Ошибка')
else:
    list = []
    string_count = 0
    for i in range(count):
        string = input('\nВведите строки: ')
        list.append(string)
        string_count+=1
print ('Строк:',string_count, 'шт.')
