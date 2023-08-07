from bisect import bisect_left,bisect_right

a = [2,3,6,6,6,10,12,15]
l = bisect_left(a,6)
r = bisect_right(a,6)

print(r-l)          # 배열에 목표 값(6)이 몇 개 있는지 확인