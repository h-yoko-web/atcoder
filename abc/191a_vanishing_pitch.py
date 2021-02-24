v, t, s, d = map(int, input().split())
print("No") if v*t <= d and d <= v*s else print("Yes")
