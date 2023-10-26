def find_emptyroom(chk,rooms) :
  if chk not in rooms :
    rooms[chk] = 1
    return chk
  return find_emptyroom(chk+1,rooms)

def solution(arr) :
  