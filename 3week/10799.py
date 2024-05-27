bar = list(input())
ans = 0
sta = []
for i in range(len(bar)):
    if bar[i] =="(":
        sta.append("(") #'('이 나오면 스택에 넣는다
    else:
        if bar[i-1]=="(": #')'가 나오고 이전 문자가 '('라면 레이저. 현재 쌓인 '('개수만큼 개수 더하기
            sta.pop()
            ans += len(sta)
        else: #')'가 나오고 이전 문자도 ')'라면 쇠막대기 끝머리 표현 
            sta.pop() #스택의 '('를 pop해줌
            ans+=1 #정답에 1 더하기
print(ans)