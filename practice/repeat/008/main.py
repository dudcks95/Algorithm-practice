
N, X = map(int, input().split())

number_list = list(map(int,input().split()))

for i in range(N):
    if number_list[i] < X :
        print(number_list[i], end=" ")
        # end를 이용해서 출력값을 한줄로 나열
