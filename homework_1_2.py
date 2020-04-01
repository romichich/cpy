import math
import numpy
a = 2*50**(-1)
b = 8.5
n = 2

#1
print('-' * 50)
print("Исходные данные (for)")
print('-' * 50)

for i in [2, 1, 8.3]:
    print("i = "+str(i))
    y = i * b - a * b ** 2
    if y >= 0:
        y = math.sqrt(y)
        print("y = "+str(y))
        z = y * math.tan(n/4) - math.exp(1+b)
        print("z = "+str(z))
    else:
        print("не корректные входные данные для вычилсения y")

#2
print('-' * 50)
print("Исходные данные (while)")
print('-' * 50)

i = 1
while i <= 3:
    print("i = "+str(i))
    y = i * b - a * b ** 2
    if y >= 0:
        y = math.sqrt(y)
        print("y = "+str(y))
        z = y * math.tan(n/4) - math.exp(1+b)
        print("z = "+str(z))
    else:
        print("не корректные входные данные для вычилсения y")
    i += 0.5

#3
print('-' * 50)
print("Исходные данные (двойной цикл)")
print('-' * 50)

for b in numpy.arange(2, 3, 0.5):
    for n in [3, -6, 0.2, 2.8]:
        print("i = " + str(i))
        y = i * b - a * b ** 2
        if y >= 0:
            y = math.sqrt(y)
            print("y = " + str(y))
            z = y * math.tan(n / 4) - math.exp(1 + b)
            print("z = " + str(z))
        else:
            print("не корректные входные данные для вычилсения y")
