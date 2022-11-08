def recursive_func(i):
    if i == 100:
        print(i, '번쨰 재귀함수 종료합니다')
        return
    print(i,'번쨰 재귀함수에서',i+1,'번째 재귀함수를 호출합니다')
    recursive_func(i+1)


recursive_func(1)