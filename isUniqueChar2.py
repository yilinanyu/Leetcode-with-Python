def isUniqueChar(s):
        a = [0] * 8
        index = 0
        shift = 0
        for c in s:
                index = ord(c) / 32
                shift = ord(c) % 32
                if a[index] & (1 << shift):
                        return False
                a[index] |= (1 << shift)
                
        return True