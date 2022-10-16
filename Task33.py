# Задача 33.
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите k = '))

def function(k):
    result = ''
    x = 'x'
    for i in range(k+1):
        a = random.randint(0,100)
        result = f'{a}*{x}**{i}+{result}'
    print(result[:-7])
    with open('Task33_file1.txt', 'w') as data1:
        data1.write(result[:-7])

    with open('Task33_file2.txt', 'w') as data2:
        data2.write(result[:-7])

function(k)

