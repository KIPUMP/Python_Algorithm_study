stack  = []                

stack.append(1)
stack.append(2)
stack.append(5)
stack.pop()             # 5 제거
stack.append(3)
stack.append(9)         # 9 제거
stack.pop()


print(stack[-1])        #최상단 노드 출력

stack.reverse()

for i in stack:
    print(i, end = " ")  #최상단 노드 출력 방법 1

print()

stack.reverse()         #stack 원상태로 뒤집기

print(stack[::-1])      #최상단 노드 출력 방법 2


