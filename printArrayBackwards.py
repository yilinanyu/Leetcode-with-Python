class Solution:
    # @param a list of integers
    # @return an integer
    def printArryaBackwords(A):
        if len(A) == 0:
            return None
        print A[::-1]
    A = [1,1,3,4,55]
    printArryaBackwords(A)