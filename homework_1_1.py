print("Введите три числа")
A = []
A.append(int(input("a=")))
A.append(int(input("b=")))
A.append(int(input("c=")))

if A.count(A[0]) > 1 or A.count(A[1]) > 1:
    print("У нас есть пара!")
