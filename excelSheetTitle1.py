class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        # dicts = {"1":"A","2":"B","3":"C","4":"D","5":"E","6":"F","7":"G","8":"H","9":"I","10":"J","11":"K","12":"L","13":"M","14":"N","15":"O","16":"P","17":"Q","18":"R","19":"S","20":"T","21":"U","22":"V","23":"W","24":"X","25":"Y","26":"Z"}
        # if n <= 26:res = dicts[str(n)]
        # else:
	       # m = n/26
	       # r = n% 26
	       # res = dicts[str(m)] + dicts[str(r)]
        # return res
        # ord（）：将字母转换成数字；char（）：数字转换成字母
        ans = ''
        while num:
            ans = chr(ord('A') + (num - 1) % 26) + ans
            num = (num - 1) / 26
        return ans
        
        
        