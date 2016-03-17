def isUniqueChar(s):
        if len(s) > 128:
                return False
        
        char_set = [False] * 256
        for c in s:
                if char_set[ord(c)]:
                        return False
                
                char_set[ord(c)] = True
                
        return True