n = int(input())


array = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(i):
        if abs(array[i][1] - array[j][1]) <= abs(array[i][0] - array[j][0]):
            ans += 1

print(ans)
