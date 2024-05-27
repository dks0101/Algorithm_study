import sys
n, m = map(int, input().split())
str = dict()
cnt = 0
for _ in range(n):
    s = sys.stdin.readline() 
    #sys.stdin.readline() : 반복문으로 여러 줄을 입력받아야 할 때 input은 시간초과
    str[s] = True
for _ in range(m):
    c = sys.stdin.readline()
    if c in str.keys():
        cnt += 1
print(cnt)