n, x = map(int, input().split())
s = input()

for marubatsu in s:
    if marubatsu == "x" and x != 0:
        x -= 1
    elif marubatsu == "o":
        x += 1
    else:
        pass

print(x)
