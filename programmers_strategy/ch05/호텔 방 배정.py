import sys
sys.setrecursionlimit(10**6)

def find_emptyroom(chk,rooms) :
  if chk not in rooms :
    rooms[chk] = 1
    return chk
  empty = find_emptyroom(rooms[chk],rooms)
  rooms[chk] = empty + 1
  return empty

def solution(k,room_number) :
  rooms = dict()
  for num in room_number :
    chk_in = find_emptyroom(num,rooms)
  return list(rooms)
