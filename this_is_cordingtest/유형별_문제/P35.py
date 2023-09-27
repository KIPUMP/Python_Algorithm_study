import sys
input = sys.stdin.readline
n = int(input())
d = [0] * n
d[0] = 1
idx_2,idx_3,idx_5 = 0,0,0
next_2,next_3,next_5 = 2,3,5

for i in range(1,n) :
    
    d[i] = min(next_2,next_3,next_5)
    
    if d[i] == next_2 :
        idx_2 += 1
        next_2 = d[idx_2] * 2
    if d[i] == next_3 :
        idx_3 += 1
        next_3 = d[idx_3] * 3
    if d[i] == next_5 :
        idx_5 += 1
        next_5 = d[idx_5] * 5
        
        
print(d[n-1])
        







