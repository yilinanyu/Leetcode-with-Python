def removeElement(A, elem):
    # write your code here
    if len(A) == 0 or A is None:
        return None
    for i in range(len(A)):
        if A[i] != elem:
            continue
        else:
            A.remove(elem)
            continue
    return A

A = [1,2,3,45]
elem = 2
print removeElement(A, elem)