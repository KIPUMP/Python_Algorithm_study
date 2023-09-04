N = input()
sum_left = 0
sum_right = 0
for i in range(len(N)//2) :
  sum_left += int(N[i])

for i in range(len(N)//2 , len(N)) :
  sum_right += int(N[i])

if sum_left == sum_right :
  print("LUCKY")
else :
  print("READY") 

