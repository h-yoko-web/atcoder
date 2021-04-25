
n = int(input())
A, B = [], []

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if A.index(min(A)) != B.index(min(B)):
    print(max(min(A), min(B)))
else:
    print(min(min(A)+min(B), max(sorted(A)
                                 [1], min(B)), max(min(A), sorted(B)[1])))
