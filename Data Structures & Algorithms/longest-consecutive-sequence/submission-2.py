class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)

        maxi = 1
        for num in seen:
            if num-1 not in seen:
                curr = 1
                while((num+curr) in seen):
                    curr+=1

                    maxi = max(maxi,curr)
        
        return maxi
