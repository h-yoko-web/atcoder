h, w = map(int, input().split())

grid = []
for i in range(h):
    a = list(map(int, input().split()))
    grid.append(a)

array = []
for i in grid:
    for j in i:
        array.append(j)

ans = 0
for i in array:
    ans += i - min(array)

print(ans)
