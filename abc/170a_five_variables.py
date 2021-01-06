# 自分の解答
x1, x2, x3, x4, x5 = map(int, input().split())

x = [x1, x2, x3, x4, x5]

count = 1

for n in range(len(x)):
    if x[n] == 0:
        print(count)
    else:
        count += 1

# 簡潔で分かりやすい解答例
x = input().split()
print(x.index("0")+1)  # indexメソッドは引数の値が何番目にあるか取得する
