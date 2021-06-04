# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def mergesort(data):

    def sort(data):
        if len(data) < 2:
            return data
        else:
            M = len(data) // 2  # M - middle
            L = sort(data[:M])  # L - left
            R = sort(data[M:])  # R - right
            return merge(L, R)

    def merge(L, R):
        result = []
        i, j = 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        while i < len(L):
            result.append(L[i])
            i += 1
        while j < len(R):
            result.append(R[j])
            j += 1
        return result

    result = sort(data)
    return result


N = 10

a = 0
b = 50

arr = [random.random()*(a+(b-a)) for i in range(N)]
print(f'Исходный массив:\n{arr}')
print('*' * 50)
arr2 = mergesort(arr)
print(f'Сортированыый:\n{arr2}')
