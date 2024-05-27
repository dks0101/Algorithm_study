a, b =  map(int, input().split())
ans = 1 #연산 최솟값
while(b!=a):
    ans += 1
    temp = b
    if b%10==1:#b를 10으로 나눈 나머지가 1이면 b를 10으로 나눠줌
        b = b//10
    elif b%2 == 0:#b를 2로 나눈 나머지가 0이면 b를 2로 나눔
        b = b//2

    if temp == b:#만들 수 없는 경우
        print(-1)
        break
else:
    print(ans)