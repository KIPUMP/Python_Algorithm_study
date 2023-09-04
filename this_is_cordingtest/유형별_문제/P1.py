N = int(input())
travel = list(map(int,input().split()))

people = len(travel)
group = 0

while people > 0 :

  coward = max(travel)
  people -= coward
  travel.remove(coward)
  group += 1


print(group)


