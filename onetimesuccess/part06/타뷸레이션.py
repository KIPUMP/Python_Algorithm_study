f = [-1] * 37

for i in range(37) :
  f[i] = i if i < 2 else f[i-1] + f[i-2]

print(f[36])