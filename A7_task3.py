# Массив размером 2m+1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random
import statistics


def median(data, L, R):

    M = len(data) // 2

    if L >= R:
        return data[M]

    pivot = data[M]
    i, j = L, R

    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    if M < i:
        data[M] = median(data, L, j)
    elif j < M:
        data[M] = median(data, i, R)

    return data[M]


a = 0
b = 100

m = 10
size = 2*m+1

arr = [random.randint(a, b) for _ in range(size)]

median1 = median(arr, 0, len(arr)-1)
print(median1)

median2 = statistics.median(arr)  # для сравнения
print(median2)
