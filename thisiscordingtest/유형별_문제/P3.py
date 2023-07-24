S = input()
cnt_0 = 0
cnt_1 = 0

for i in range(0,len(S)-2) :
  if S[i] != S[i+1] :
    if S[i] == "0":
      cnt_0 += 1
    else :
      cnt_1 += 1

print(min(cnt_0,cnt_1))
  