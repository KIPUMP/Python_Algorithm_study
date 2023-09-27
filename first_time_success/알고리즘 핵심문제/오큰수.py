import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
stk = []
result = [-1 for _ in range(n)]

for i in range(n) :
  while stk and arr[stk[-1]] < arr[i] :
    result[stk[-1]] = arr[i]
    stk.pop(-1)

  stk.append(i)

print(' ',join(map(str,result)))
