#Даниил

import random

# Создаем список из 25 случайных чисел от -50 до 50
nums = [random.randint(-50, 50) for _ in range(25)]

print("Список:", nums, end='\n\n')

# Считаем положительные, отрицательные и нули
pos = sum(1 for num in nums if num > 0)  # Сокращенный цикл
neg = sum(1 for num in nums if num < 0)
zeros = sum(1 for num in nums if num == 0)
total = len(nums)

# Выводим статистику
print("СТАТИСТИКА:")
print(f"Положительные: {pos} шт. ({pos/total*100:.1f}%)")
print(f"Отрицательные: {neg} шт. ({neg/total*100:.1f}%)")
print(f"Нули: {zeros} шт. ({zeros/total*100:.1f}%)")
print(f"Всего: {total} шт.", end='\n\n')

# Находим мин и макс
print("ЭКСТРЕМУМЫ:")
print(f"Максимум: {max(nums)}")
print(f"Минимум: {min(nums)}")

