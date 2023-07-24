num = input()
result = 0
arr = []

for i in num :
  arr.append(i)
arr.sort()
while len(arr) > 0 :
  if result == 0 :
    result += int(arr[0])
  elif result > 0 :
    result *= int(arr[0])
  arr.remove(arr[0])

print(result)