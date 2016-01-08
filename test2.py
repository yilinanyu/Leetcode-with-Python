res = []
nums = [1,2,3,5]
for i in nums:
    for j in nums:
        res.append(i * j)
        res.append(i * i)
print res       
# if num in res:
#     return True
# else:
#     return False