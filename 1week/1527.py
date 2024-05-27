a, b = map(int, input().split())
Q = [4, 7]
ans = 0
while len(Q) > 1:
    F = Q[0]
    Q.pop(0)
    print(F)
    print(Q)
    if F <= b:
        if a<=F:
            ans +=1
            Q.append(F*10+4)
            Q.append(F*10+7)
print(ans)
