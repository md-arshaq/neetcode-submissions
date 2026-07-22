from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for word in strs:
            mpp = [0]*26
            
            for i in word:
                mpp[ord(i)-ord("a")]+=1

            freq[tuple(mpp)].append(word)
            
        res = []
        
        for key,val in freq.items():
            res.append(val)

        return res
