n = int(input())

sset = set(input() for i in range(n))

for s in sset:
    if "!" + s in sset:
        print(s)
        exit()

print("satisfiable")
