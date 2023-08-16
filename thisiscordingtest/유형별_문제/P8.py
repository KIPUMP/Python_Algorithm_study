import sys
input = sys.stdin.readline
S = input()
arr = []
for i in S :
  arr.append(i)
sum_val = 0
new_arr = []
for i in arr :
  if i.isalpha() :
    new_arr.append(i)
  elif i.isdigit() :
    sum_val += int(i)

new_arr.sort()
new_arr.append(str(sum_val))

for i in new_arr :
  print(i,end="")

  