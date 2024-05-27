from sys import stdin

n, k = map(int, stdin.readline().split()) #식탁 길이 n, 햄버거 먹을 수 있는 기리 k
table = list(stdin.readline().rstrip()) #햄버거와 사람의 위치 문자열
ans = 0 # 먹을 수 있는 사람의 수

#n만큼 table 리스트를 돌면서 table[i]가 사람이라면
#i-k~i+k+1까지 돌기. -> i번째 사람은 i-k~i+k+1의 햄버거 먹을 수 있음
for i in range(n):
    if table[i] == 'P':
        for j in range(i - k, i + k + 1):
            if -1 < j < n:
                if table[j] == 'H':
                    table[j] = '-'#해당 번호의 햄버거 먹음
                    ans += 1
                    break

print(ans)