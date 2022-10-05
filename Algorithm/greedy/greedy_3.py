# s = input()
# result = 0

# for i in s:
#     if int(i) <=1 or result <=1 : 
#         result += int(i)
#     else :
#         result *= int(i)

# print(result)

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <=1 :
        result += num
    else :
        result *= num
print(result)