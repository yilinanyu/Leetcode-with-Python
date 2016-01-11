class Solution:
    # @param {integer} n
    # @return {integer}
    #
# 解法I：预处理+从高位向低位枚举1的出现次数
# 预处理数组ones，ones[x]表示[0, 10 ^ x)范围内包含的1的个数

# 由高位向低位依次遍历数字n的每一位digit

# 记digit右边（低位）数字片段为n，size为当前位数，cnt为1的总数

# 若digit > 1，则cnt += digit * ones[size - 1] + 10 ^ (size - 1)

# 若digit = 1，则cnt += n + ones[size - 1] + 1
    def countDigitOne(self, n):
        if n < 0:
            return 0
        ones, x = [0], 0
        while 10 ** x <= 0x7FFFFFFF:
            ones.append(ones[x] * 10 + 10 ** x)
            x += 1
        cnt, size = 0, len(str(n))
        for digit in str(n):
            digit = int(digit)
            size -= 1
            n -= digit * 10 ** size
            if digit > 1:
                cnt += digit * ones[size] + 10 ** size
            elif digit == 1:
                cnt += n + ones[size] + 1
        return cnt