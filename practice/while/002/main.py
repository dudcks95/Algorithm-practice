while True :
    try :
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
    # try문으로 실행하고 예외적인 값이 입력될때 except문을 실행시켜
    # 프로그램을 종료한다.