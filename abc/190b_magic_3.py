n, s, d = map(int, input().split())

X = []
Y = []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for x, y in zip(X, Y):
    if x < s and y > d:
        print("Yes")
        exit()

print("No")
