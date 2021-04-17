import sys

S = input()

for i in range(len(S)):
    if i % 2 == 0 and S[i].islower() == False:
        print("No")
        sys.exit()
    elif i % 2 != 0 and S[i].islower():
        print("No")
        sys.exit()

print("Yes")
