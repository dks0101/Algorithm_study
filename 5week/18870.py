n = input()
num = list(map(int, input().split()))
num2 = sorted(set(num))
dict = {num2[i] : i for i in range(len(num2))}
for i in num:
    print(dict[i], end = ' ')