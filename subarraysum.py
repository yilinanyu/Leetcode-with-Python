def subarraySum(self, A):
    hs = {0：-1}
    sum = 0
    for i in range(len(A)):
        # if A[i] == 0:
        #     return [i, i]
        sum += A[i]
        if sum in hs:
            return [hs[sum] + 1, i]
        hs[sum] = i
    return 