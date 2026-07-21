from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in range(len(nums)):
            freq[nums[i]]+=1

        s = []
        for key,v in freq.items():
            s.append([v,key])
        
        s.sort(reverse=True)
        res = []

        for i in range(k):
            res.append(s[i][1])
        
        return res

