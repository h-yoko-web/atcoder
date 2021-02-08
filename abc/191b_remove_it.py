n, x = map(int, input().split())
a = list(map(int, input().split()))

a_ = []
for i in a:
    if i != x:
        a_.append(i)

print(*a_)
