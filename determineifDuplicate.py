class Solution:
    # @param a list of integers
    # @return an integer
    def determindifDuplicate(A):
        if len(A) == 0:
            return False
        return len(A) != len(set(A))
       

    A = [1,3]
    print determindifDuplicate(A)