for _ in range(int(input())) :
  stk1 = []
  stk2 = []

  for ch in input() :
    if ch == "<" :
      if len(stk1) :
        stk2.append(stk.pop())
    elif ch == ">" :
      if len(stk2) :
        stk1.append(stk2.pop())
    elif ch == "-" :
      if len(stk1) :
        stk1.pop()
    else :
      stk1.append(ch)
  print(''.join(stk1) + ''.join(reversed(Stk2)))