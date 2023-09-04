n,k = map(int,input().split())
arr_1 = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))

for _ in range(k) :
  a = min(arr_1)
  b = max(arr_2)
  arr_1.remove(a)
  arr_1.append(b)
  arr_2.remove(b)
  arr_2.append(a)


print(sum(arr_1))