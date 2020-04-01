import random
n = int(input("размер списка n = "))
A = []
B = []
for i in range(n):
    A.append(random.randint(0, 99))
    if A[i] % 2 == 0:
        B.append(A[i])

print("Список A:")
print(A)
print("Список B:")
print(B)