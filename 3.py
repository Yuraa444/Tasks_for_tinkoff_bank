n = int(input())

while n >= 1:
    n = n / 10

striiing = str(n)

if '.' in striiing:
    w = (striiing[striiing.index('.') + 1:])
else:
    print('Число не дробное')

v = int(w)

count = []

while v > 0:
    digit = v % 10
    if digit == 0:
        count.append(digit)
    v = v // 10

print(len(count))
