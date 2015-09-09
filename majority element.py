class Solution(object):
    def majorityElement(self, num):
      candidate, count = None, 0
      for e in num: 
          if count == 0:
              candidate, count = e, 1
          elif e == candidate:
              count += 1
          else:
              count -= 1 
      return candidate