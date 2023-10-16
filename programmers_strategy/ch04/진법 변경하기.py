def radixChange(num,radix) :
  if num == 0 :
    return '0'
  nums = []
  while num :
    num , digit = divmod(num,radix)
    nums.append(str(digit))
  return ''.join(reversed(nums))

print(radixChange(2000,3))