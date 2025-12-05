#Даниил

# Запрашиваем у пользователя строку для поиска
search_string = input('Введите строку для поиска: ')
    
# Открываем файл для чтения
with open('text.txt', 'r', encoding='utf-8') as file:
# Читаем все строки из файла
    lines = file.readlines()
    
# Список для хранения найденных строк
found_lines = []
    
# Поиск строк, содержащих искомую подстроку
for line in lines:
# Убираем лишние пробелы и символы перевода строки
    cleaned_line = line.strip()
# Проверяем, содержит ли строка искомую подстроку
    if search_string in cleaned_line:
        found_lines.append(cleaned_line)
    
# Выводим результаты поиска
print(f"\nНайдено строк: {len(found_lines)}")
print("Найденные строки:")
for i, line in enumerate(found_lines, 1):
    print(f"{i}. {line}")
    
# Сортируем найденные строки по длине (от самой короткой к самой длинной)
sorted_lines = sorted(found_lines, key=len)
    
# Выводим отсортированные строки
print("\nОтсортированные строки (по длине):")
for i, line in enumerate(sorted_lines, 1):
    print(f"{i}. {line} (длина: {len(line)} символов)")

