def radixChange(num,radix) :
  if num  == 0 :
    return 0
  while num :
    num,digit = divmod(num,radix)
    nums.append(str(digit))
  return ''.join(reversed(nums))

def solution(n) :
  return int(radixChange(n,3)[::-1],3)      # int(진법이 있는 문자열, 진법)