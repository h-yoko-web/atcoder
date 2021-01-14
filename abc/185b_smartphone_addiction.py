import sys
sys.setrecursionlimit(10**6)

N, M, T = map(int, input().split())

A_B = [list(map(int, input().split())) for _ in range(M)]
batery = N
before = 0

for m in range(M):
    batery -= A_B[m][0] - before
    if batery <= 0:
        print("No")
        sys.exit()
    batery += A_B[m][1] - A_B[m][0]
    before = A_B[m][1]
    batery = min(N, batery)

if before + batery - T <= 0:
    print("No")
else:
    print("Yes")
