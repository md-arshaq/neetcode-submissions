class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for i in strs:
            freq[tuple(sorted(i))].append(i)
        
        res = []
        for key,val in freq.items():
            res.append(val)

        return res
