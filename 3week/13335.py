n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
bridge = [0]*w
time = 0
while bridge:
    time += 1
    bridge.pop(0) #다리 위에 트럭이 올라간 것이므로 pop해줌
    if truck:
        if sum(bridge) + truck[0] <= l: #현재 다리의 합과 다음 트럭을 더했을 때 l이하라면 다리에 트럭 넣어주기
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)