num = int(input())
# 배열의 크기를 미리 정해놓고 하는 방식을 찾지못함
num_list = list(map(int, input().split()))
print(min(num_list), max(num_list))