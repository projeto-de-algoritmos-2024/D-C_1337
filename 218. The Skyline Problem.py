from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def getSkyline(self, buildings):
        dict1 = defaultdict(list)
        for start, end, height in buildings:
            dict1[start].append([1, height])
            dict1[end].append([-1, height])
            
        res = []
        prev = -1
        ans = SortedList()
        ans.add(0)
        
        for i in sorted(dict1.keys()):
            for f, h in dict1[i]:
                if f == -1:
                    ans.remove(h)
                else:
                    ans.add(h)
                    
            if ans[-1] != prev:
                prev = ans[-1]
                res.append([i, ans[-1]])
                
        return res