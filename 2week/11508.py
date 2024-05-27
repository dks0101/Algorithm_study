from sys import stdin
n = int(stdin.readline())
list = []
sum = 0
for i in range(n):
    list.append(int(stdin.readline())) #가격을 list에 추가
list.sort(reverse=True) #리스트 역순으로 정렬
for i in range(n):
    if i%3 != 2: #리스트에서 3의 배수 자리에 있는 값 빼고 모두 더하기
        sum += list[i]
print(sum)