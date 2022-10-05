n = int(input())
x = list(map(int, input().split()))
x.sort()
group = 0
party = 0

for i in x :
    party += 1
    if party >=i :
        group +=1
        party = 0

print(group)
        

    
