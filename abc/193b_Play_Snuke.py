n = int(input())
apx = [input().split() for _ in range(n)]
apx = [[int(item) for item in row] for row in apx]

price = float("inf")

for l in apx:
    if l[0] < l[2] and price > l[1]:
        price = l[1]

print(price if price != float("inf") else -1)
