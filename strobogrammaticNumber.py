class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strobogrammatic = ["6","9","1","8","0"]
        for i in range(len(num)):
            if num[i] not in strobogrammatic:
                return False
            elif num[i] == "6":
                if num[~i] != "9":
                    return False
            elif num[i] == "9":
                if num[~i] != "6":
                    return False
            else:
                if num[i] != num[~i]:
                    return False
        return True