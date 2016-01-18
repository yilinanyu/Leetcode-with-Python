def searchRange( A, target):
        # write your code here
    if A is None:
        return [-1,-1]
    left = 0
    right = len(A)-1
    while left<= right:
        mid = left + (right - left)/2
        if target< A[mid]:
            right = mid -1
        elif target> A[mid]:
            left = mid +1
        else:
            list = [0,0]
            if A[left] == target:
                return list[0] = left
            if A[right] == target:
                return list[1] = right
            for i in range(mid, right+1):
                if num[i]!= target:
                    list[1] = i-1
                    break
            for i in range(left-1,mid,-1):
                if num[i]!= target:
                    list [0] = i+1
                    break
            return list 
    return [-1,-1]