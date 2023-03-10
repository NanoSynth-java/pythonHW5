import re

import numexpr as result

# Задача №1. Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод
# 8-5+2-1
# Вывод
# 4

print(result.evaluate('8-5+2-1'))

# Задача №2. Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)
#
# Формат ввода
# Вводится строка.
#
# Формат вывода
# Выведите слова из строки по одному.
#
# Пример 1
# Ввод
#
# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод
#
# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland


res = 'Wake the fuck up Samurai. We have a city to burn'

s2 = re.sub(r'\s+', '\n', res)
print(s2)
