#Урок 1. Знакомство с Python
#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
N = int(input("Введите число "))
M = N * -1
list = [i for i in range(M, N + 1)]
print(list)

#Напишите программу, которая будет принимать
#на вход дробь и показывать первую цифру дробной части числа.
#Любую переменную можно проверить на тип (int, float или complex):


a = float(input("Введи дробное число"))
print(int(a * 10)%10)


#Напишите программу, которая принимает на
# вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
a = int(input("Введи число"))
if a % 5 == 0 and a % 10 == 0 or a % 15 ==0 and a % 30 != 0:
    print("Kratno")
else:
    print("Net")

    #Напишите программу, которая принимает на вход цифру, обозначающую день недели,
    # и проверяет, является ли этот день выходным.
a = int(input("Введите день недели "))
day = [i for i in range(1, 8)]
if a in day and a == 6 or a == 7:
   print("Выходной")
elif a < 1 or a > 7:
   print("Введите иное число")
else:
   print("Тяжелые будни")

#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для
# всех значений предикат.
for x in [1, 0]:
    for y [1, 0]:
        for z [1, 0]:
            if not(x or y or z) != (not x and not y and not z):
                print("Не истина")
            else: print("Верно")

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём
# X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).
x = int(input("Введите координаты х "))
y = int(input("Введите у "))
if x > 0 and y > 0:
    print("1-я плоскость")
elif x < 0 and y > 0:
    print("2-я плоскость")
elif x < 0 and y < 0:
    print("3-я плоскость")
elif x > 0 and y < 0:
    print("4-я плоскость")
elif x == 0 or y == 0:
    print("Ошибка ввода")
else:
    print("Ошибка ввода")

#Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).
a = int(input("Введите число от 1 до 4 "))
if a == 1:
    print("Координаты х - любое положительное число, координаты у - любое положительное число")
elif a == 2:
    print("Координаты х - любое отрицательное число, координаты у - любое положительное число")
elif a == 3:
    print("Координаты х - любое отрицательное число, координаты у - любое отрицательное число")
elif a == 4:
    print("Координаты х - любое положительное число, координаты у - любое отрицательное число")
else:
    print("Введите число от 1 до 4")

    #Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
    # между ними в 2D пространстве.
x_1 = int(input("Введите x1 "))
y_1 = int(input("Введите y1 "))
x_2 = int(input("Введите x2 "))
y_2 = int(input("Введите y2 "))
dist = (x_2 - x_1)**2 + (y_2 - y_1)**2
res = math.sqrt(dist)
print(res)