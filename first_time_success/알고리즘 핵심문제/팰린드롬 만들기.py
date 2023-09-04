from collections import Counter
word = list(input())
word.sort()
count = Counter(word)
odd = 0
odd_alpha = ''
ans = ''
for i in count :
  if count[i] % 2 != 0 :
    odd += 1 
    odd_alpha += i
  
  for _ in range(count[i]//2) :
    ans += i

if odd > 1 :
  print("I'm sorry Hansoo")
elif odd == 0 :
  print(ans + ans[::-1])
else :
  print(ans + odd_alpha + ans[::-1])