#Даниил

import random
import itertools

# Генерируем 20 списков по 4 случайных числа
lists = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]

# Находим все уникальные пары
pairs = set()
for lst in lists:
    for pair in itertools.combinations(lst, 2):
        pairs.add(tuple(sorted(pair)))

pairs_list = list(pairs)
print(f"Уникальные пары ({len(pairs_list)}): {pairs_list}")

# Пользователь вводит число
num = int(input("Введите число: "))

# Считаем пары с суммой меньше числа
count = sum(1 for a, b in pairs_list if a + b < num)
print(f"Пар с суммой < {num}: {count}")
