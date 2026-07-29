from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq = defaultdict(int)

        n = len(s)

        j = 0

        i = 0

        res = 0

        while(i<n):
            while s[i] in freq:
                freq[s[j]]-=1
                
                if not freq[s[j]]:
                    del freq[s[j]]
            

                j+=1
            
            freq[s[i]]+=1

            res = max(i-j+1,res)

            i+=1
                
            
        return res
