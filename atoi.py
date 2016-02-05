def myAtoi(str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        flag = 1
        n = len(str)
        i = 0
        result = 0
        if i < n and str[i] == "+":
            i += 1
        elif i < n and str[i] == "-":
            flag = -1
            i += 1
        while i < n:
            if str[i].isdigit():
                if result > 214748364 or (result == 214748364 and int(str[i]) >= 8):
                    if flag == 1:
                        return 2147483647
                    elif flag == -1:
                        return -2147483648
                else:
                    result = result * 10 + int(str[i])
            else:
                break
            i += 1
        return result * flag
myAtoi("12234")
print myAtoi("-12222435")
print myAtoi("+12222 435")
print myAtoi("12222435232132313")
print myAtoi(" 12222+.43.5")
print myAtoi("shadiuahdiu")
print myAtoi(" 12245+12")

                
            
        
