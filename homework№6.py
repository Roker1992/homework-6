# Задание №1

a = int(input())
zero = 0
for i in range(a):
    x = int(input())
    if x == 0:
        zero += 1
print(zero)

# Задание №2


x = int(input())
count = 0

for d in range(1, x + 1):
    if x % d == 0:
        count += 1

print(count)

# Задание №3

a = int(input())
b = int(input())

if a % 2 != 0:
    a += 1

for i in range(a, b + 1, 2):
    print(i, end=' ')
