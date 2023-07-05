def sequential_search(n,target,array) :
  for i in range(n) :
    if array[i] == target :
      return i + 1
name_data = input().split()
n = int(name_data[0])
target = name_data[1]

name_arr = list(input().split())

print(sequential_search(n,target,name_arr))