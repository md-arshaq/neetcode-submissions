class Solution:
    def maxArea(self, nums: List[int]) -> int:
        
        n = len(nums)

        i = 0
        j = n-1

        maxwater = 0
        
        while(i<j):
            curr = min(nums[i],nums[j])*(j-i)

            maxwater = max(maxwater,curr)

            if nums[i]<nums[j]:
                i+=1
            else:
                j-=1
        
        return maxwater
            