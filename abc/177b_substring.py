# S = input()
# T = input()

# count = 0
# flg = 0

# # aaabbbccc
# # abc

# for n in range(1, len(T)):
#     if T[0:n] in S:
#         count += 1
#         if count == len(T):
#             flg = 1


# print(0) if flg == 1 else print(len(T) - count)

S = input()
T = input()

cnt = 10 ** 9
for i in range(len(S) - len(T) + 1):
    tmp = 0
    for j in range(len(T)):
        if i + j < len(S) and S[i + j] == T[j]:
            continue
        else:
            tmp += 1
    cnt = min(cnt, tmp)

print(cnt)
