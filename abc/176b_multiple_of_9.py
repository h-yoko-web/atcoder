N = input()
count = 0

for n in N:
    count += int(n)

print("No") if count % 9 != 0 else print("Yes")
