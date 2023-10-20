def solution(s) :
  change,zero = 0,0
  while s != '1' :
    num = s.count('1')
    zero += len(s) - num
    s = bin(num)[2:]          # 앞의 두 자리는 제외

  return [change,zero]

