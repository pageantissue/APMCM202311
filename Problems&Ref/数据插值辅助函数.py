import random

import numpy as np

a = int(input('input smaller number a: '))
b = int(input('input larger number b: '))


arr = [0]*12
step = (b - a) / 12
arr[0] = a

for i in range(1,12):
    num = arr[i-1] + step + random.randint(-100,230)
    if num > b:
        num = b
    arr[i] = np.ceil(num)


for x in arr:
    print(x)