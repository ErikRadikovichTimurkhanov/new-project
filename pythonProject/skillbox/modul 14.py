# задача 2
print("Введите первую точку")

x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    k = 1
else:
    k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)

# задача 3
def sum_N(N):
    count = 0
    while N > 0:
        n = N % 10
        count += n
        N //= 10
    print('Сумма чисел: ', count)
    return count
def count_N(N):
    count = 0
    while N > 0:
        n = N // 10
        count += 1
        N //= 10
    print('Количество цифр в числе:  ', count)
    return count
N = int(input('Введите число N '))
summ = sum_N(N)
count = count_N(N)
res = summ - count
print('Разность суммы и количества цифр: ', res)