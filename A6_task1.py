# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import sys


def memorysum(x, total):
    summa1 = sys.getsizeof(x)
    summa2 = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                summa2 += sys.getsizeof(key)
                summa2 += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                summa2 += sys.getsizeof(item)

    summa = summa1 + summa2
    total += summa
    # print(f'Current memory: {summa}')
    return total
# -----------------------------------------------------------------------------
# Реализация 1, через список


def real1():
    SIZE = 128
    total = memorysum(SIZE, total=0)

    arr = [random.randint(-1000, 1000) for i in range(SIZE)]  # 4824 на все
    total = memorysum(arr, total)

    index = len(arr) + 1
    total = memorysum(index, total)

    luck = 0
    total = memorysum(luck, total)

    for i in range(len(arr)):
        total = memorysum(i, total)
        if arr[i] < 0 and index == len(arr) + 1:
            index = i
            luck += 1
        elif arr[i] < 0 and arr[i] > arr[index]:
            index = i

    if luck != 0:
        print(f'Максимальное число из ряда минимальных: {arr[index]} ')
    else:
        (print('Нет отрицательных чисел'))

    print(f'Total = {total}')

    # Вывод 1: При использовании генератора списка в качестве входных данных
    # значение выделенной на все памяти была окло 8484 байта.
    # Это значение немного колеблется, так как каждый нуль из рандома
    # это 24 байта, а не 28. Большая доля памяти это итератор i в цикле
    # самого алгоритма поиска, это SIZE*28-4 = 3580, - почти половина.
    # Сам список вместе с элементами занимает 4824.
# -----------------------------------------------------------------------------
# Реализация 2, через кортеж


def real2():
    SIZE = 128
    total = memorysum(SIZE, total=0)

    arr = tuple([random.randint(-1000, 1000) for i in range(SIZE)])  # 4648
    total = memorysum(arr, total)

    index = len(arr) + 1
    total = memorysum(index, total)

    luck = 0
    total = memorysum(luck, total)

    for i in range(len(arr)):
        total = memorysum(i, total)
        if arr[i] < 0 and index == len(arr) + 1:
            index = i
            luck += 1
        elif arr[i] < 0 and arr[i] > arr[index]:
            index = i

    if luck != 0:
        print(f'Максимальное число из ряда минимальных: {arr[index]} ')
    else:
        (print('Нет отрицательных чисел'))

    print(f'Total = {total}')

    # Вывод 2: При использовании генератора кортежа в качестве входных
    # данных значение выделенной на все памяти 8308 байта
    # (если нет нулей в рандоме). Сам кортеж - 4648, что немного меньше
    # чем список, что ожидаемо.
# -----------------------------------------------------------------------------
# Реализация 3, через словарь


def real3():
    SIZE = 128
    total = memorysum(SIZE, total=0)

    arr = {i: random.randint(-1000, 1000) for i in range(SIZE)}
    total = memorysum(arr, total)

    index = len(arr)+1
    total = memorysum(index, total)

    luck = 0
    total = memorysum(luck, total)

    for i in range(len(arr)):
        total = memorysum(i, total)
        if arr[i] < 0 and index == len(arr) + 1:
            index = i
            luck += 1
        elif arr[i] < 0 and arr[i] > arr[index]:
            index = i

    if luck != 0:
        print(f'Максимальное число из ряда минимальных: {arr[index]} ')
    else:
        (print('Нет отрицательных чисел'))

    print(f'Total = {total}')

    # Вывод 3: При использовании генератора словаря (с ключами int) в качестве
    # входных данных значение выделенной на все памяти 15520 байта
    # (если нет нулей в рандоме). Сам кортеж - 11860. Это примерно в 2.5 раза
    # больше чем список, что неожиданно, т.к. я предполагал только
    # лишь удвоение памяти.


real1()
print('*'*10)

real2()
print('*'*10)

real3()
print('*'*10)


# Вывод: из трех вариантов самый эффективный по памяти -
# это использующий кортеж.

# OS Windows x64, Интерпретатор Python 3.8.8
