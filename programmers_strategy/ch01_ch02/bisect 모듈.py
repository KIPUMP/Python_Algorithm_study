# import bisect
# result = []
# for score in [33,99,77,70,89,90,100] :
#   pos = bisect.bisect([60,70,80,90], score)   # score 기준 삽입
#   grade = 'FDCBA'[pos]
#   result.append(grade)
# print(result)

from bisect import bisect_left,bisect_right

a = [2,3,6,6,6,10,12,15]

l = bisect_left(a,6)    # bisect_left(배열,찾을 원소)
r = bisect_right(a,6)   # bisect_right(배열,찾을 원소)

print(r-l)               # 배열에 목표 값(6)이 몇 개 있는지 확인