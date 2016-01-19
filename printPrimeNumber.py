import math
import random
class Solution:
    # @param a list of integers
    # @return an integer
    def printprimeNumber():
        res = []
        for i in range(2,100):
            prime = True 
            for j in range(2,i):
                if (i %j == 0):
                    prime = False
                    break
            if prime:
                res.append(i)
        print random.choice(res)
    printprimeNumber()