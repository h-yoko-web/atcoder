
# n, x = map(int, input().split())
# vp = [map(int, input().split()) for _ in range(n)]
# v, p = [list(i) for i in zip(*vp)]

# inge = 0
# for i in range(n):
#     inge += v[i] * p[i] * 0.01
#     if inge > x:
#         print(i + 1)
#         exit()

# print(-1)

# n, x = map(int, input().split())

# inge = 0

# for i in range(n):
#     v, p = map(int, input().split())
#     inge += v * p * 0.01
#     if inge > x:
#         print(i + 1)
#         exit()

# print(-1)

N, X = map(int, input().split())
s = 0
for i in range(N):
    v, p = map(int, input().split())
    s += v*p
    if s > X*100:
        print(i+1)
        exit()
print(-1)
