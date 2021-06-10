# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

s = input('Введите строку \n')

summa = set()

for i in range(len(s)):
    if i == 0:
        for j in range(len(s)-1, i, -1):
            hash_s = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            summa.add(hash_s)
    else:
        for j in range(len(s), i, -1):
            hash_s = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            summa.add(hash_s)

print(f'{len(summa)} различных подстрок в строке {s}')
