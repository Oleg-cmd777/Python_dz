# Урок 4. Данные, функции и модули в Python. Продолжение
# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001
import math
from math import pi
d = int(input("Введите число "))
print(f'число Пи с точностью  {d} равно {round(pi, d)}')

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def mnojit(n):
    i = 2
    lst = []
    while i * i <= n:
        while n % i == 0:
            lst.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        lst.append(n)
    return lst
print(mnojit(180))

# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через словари удобно, но необязательно
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def unical(lst):
    result = []
    for char in lst:
        if lst.count(char) < 2:
            result.append(char)
    return result
print(unical([4,7,7,5,6,6,8,8,3,9,9,9,4,3]))# выведет [5]

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

# Вариант и идея Стоуна.
# from random import randint as ri

def createEquation():# Вариант и идея Стоуна.
    degree = int(input("Введите макс. степень многочлена"))
    equation = ''
    for d in range(degree, -1, -1):
        coef = ri(-20, 20)
        if d == degree:
            if coef > 0:
                equation += str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += '-' + str(abs(coef)) + 'x^' + str(d)
        else:
            if coef > 0:
                equation += ' + ' + str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += ' - ' + str(coef) + 'x^' + str(d)
eq1 = createEquation()
print(eq1.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^'))
eq2 = createEquation()
print(eq2.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^'))
with open('sem4.txt', 'w') as data:
    data.write(eq1)

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
# Версия Стоуна. Идея чуть менее чем полностью принята у тов. Стоуна.

from HW4 import createEquation # Версия Стоуна. Идея чуть менее чем полностью принята у тов. Стоуна.

def readEquation():# Версия Стоуна. Идея чуть менее чем полностью принята у тов. Стоуна.

firstEquation = createEquation()
equation = {}

 firstEquation = firstEquation.replace(" + ", " +").replace(" - ", " -").split()[:-2]

 for i in range(len(firstEquation)):
  firstEquation[i] = firstEquation[i].replace("+", "").split("x^")
  equation[int(firstEquation[i][1])] = int(firstEquation[i][0])
  return equation
 word = readEquation()
 word2 = readEquation()

 print(word)
 print(word2)
for i in range(max(len(word), len(word2))):
 first = word.get(i)
 second = word2.get(i)
 if first != None or second != None:
  finalWord[i] = (first if first != None else 0) + (second if second != None else 0)
print(finalWord)
