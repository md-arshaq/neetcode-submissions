class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]*(len(nums)+1)

        pre = 1
        for i in range(len(nums)):
            pre = pre*nums[i]
            pref.append(pre)
        
        suf = 1

        for i in range(len(nums)-1,-1,-1):
            suf*=nums[i]
            suff[i] = suf
        
        res = []
        for i in range(len(nums)):
            res.append(pref[i]*suff[i+1])
        
        return res
