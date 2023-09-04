n = int(input())
company = set()
for _ in range(n) :
  name,el = input().split()
  if el == "enter" :
    company.add(name)
  else :
    if name in company :
      company.discard(name)
  
for name in sorted(company,reverse=True) :
  print(name)