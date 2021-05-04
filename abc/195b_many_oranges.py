# A, B, W = map(int, input().split())

# inf = 10000000000000


# for n in range(1, 1000001):
#     if A*n <= 1000*W and 1000*W <= B*n:
#         m = min(inf, n)
#         M = max(-inf, n)

# if m == inf or M == -inf:
#     print("UNSATISFIABLE")
# else:
#     print(m, M)

import math
a, b, w = map(int, input().split())
upper = int(math.floor(1000*w/a))
lower = int(math.ceil(1000*w/b))
if lower > upper:
    print("UNSATISFIABLE")
else:
    print(lower, upper)
