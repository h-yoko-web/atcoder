import math
n = int(input())
X = list(map(int, input().split()))

man = 0
en = 0
cheby = 0
for x in X:
    man += abs(x)
    en += x**2
    cheby = max(cheby, abs(x))

print(man)
print(math.sqrt(en))
print(cheby)
