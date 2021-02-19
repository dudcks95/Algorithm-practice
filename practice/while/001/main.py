T = 1
while T:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
        # a와 b의 입력값이 0일때 while문을 중단
    c = a + b
    print(c)


