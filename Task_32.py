# Определить индексы элементов массива, 
# значения которых принадлежат заданному диапазону, 
# т.е. не меньше заданного минимума и не больше заданного максимума.

import random
array = [random.randint(0, 100) for i in range(20)]
print(array)

min_val = int(input('Минимум диапазона: '))
max_val = int(input('Максимум диапазона: '))

for i in range(len(array)):
    print(i) if min_val <= array[i] <= max_val else None
