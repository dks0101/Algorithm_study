n = int(input())
num = sorted(list(map(int, input().split())))
x = int(input())
answer = 0
a = 0 #start
b = n-1 #end
while a<b:
    if num[a] + num[b] == x:
        answer += 1
        a+=1
    elif num[a] + num[b] > x:
        b-=1
    else:
        a+=1
print(answer)
