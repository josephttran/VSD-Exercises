def isVeryOdd(n):
    for i in str(n):
        if (int(i) % 2 == 0):
            return False
    return True

total = 0
reversibles = []

for i in range(0, 10000000, 1):
    if i in reversibles:
        continue

    if (i % 10 == 0):
        continue
    reversed = str(i)[::-1]

    result = (i + int(reversed))
    if (result % 2 == 0):
        continue

    if isVeryOdd(result):
        total += 1
        reversibles.append(i)
        reversibles.append(reversed)
print total
