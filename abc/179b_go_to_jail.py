n = int(input())
count = 0
status = "No"
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        count += 1
        if count == 3:
            status = "Yes"
    else:
        count = 0

print("Yes") if status == "Yes" else print("No")
