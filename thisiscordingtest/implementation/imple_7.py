n = int(input())
clock,minute,second = 0,0,0
cnt = 0
while True :
  if clock == n and minute == 59 and second == 59:
    break
  second += 1

  if second == 60 :
    second = 0
    minute += 1
  
  if minute == 60:
    minute = 0 
    clock += 1
  
  if clock % 10 == 3 or minute % 10 == 3 or second % 10 == 3 :
    cnt += 1
  elif minute // 10 == 3 or second // 10 == 3 :
    cnt += 1

print(cnt)
  
  