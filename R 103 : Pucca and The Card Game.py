import math

n = int(input())
a = list(map(int, input().split()))

i = 0
j = n - 1
k = 1
b = [0, 0]

while i <= j:
    if k == 1:
        k = 0
    else:
        k = 1
    if a[i] < a[j]:
        b[k] += a[j]
        j -= 1
    else:
        b[k] += a[i]
        i += 1

if b[0] >= b[1]:
    print("Pucca")
else:
    print("Garu")
