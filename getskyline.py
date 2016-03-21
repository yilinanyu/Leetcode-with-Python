class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = collections.defaultdict(list)
        
        for x, y, h in buildings:
            dic[x].append(-h)
            dic[y].append(h)
        
        heap = [0]
        counter = collections.Counter([0])
        heapq.heapify(heap)
        ans = []
        
        for x, values in sorted(dic.items()):
            for h in values:
                if h < 0:
                    heapq.heappush(heap, h)
                    counter[h] += 1
                else:
                    counter[-h] -= 1
                
            while counter[heap[0]] == 0:
                heapq.heappop(heap)
            
            height = -heap[0]
            if not ans or height != ans[-1][1]:
                ans.append([x, height])
        return ans