import sys

T = int(input())

for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    # input을 대신해서 sys.stdin.readline()을 사용함.
    n = a + b
    print(n)