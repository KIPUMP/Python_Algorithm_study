def solution(s) :
  cnt = 0
  for i in s :
    if s[i] == ' ' :
      cnt = 0 
      continue
    if cnt % 2 == 0 :
      s[i] = s[i].upper()
    else :
      s[i] = s[i].lower()
    cnt += 1
  
  return ''.join(s)