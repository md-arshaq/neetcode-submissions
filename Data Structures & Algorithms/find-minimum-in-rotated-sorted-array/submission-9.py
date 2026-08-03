class Solution:
    def findMin(self, arr: List[int]) -> int:
        # brute force

        # return min(nums)

        # binary-search
        n = len(arr)

        minval = float("inf")

        low = 0
        high = n-1

        while(low<= high):
            mid = (low+high)//2
            
            if arr[mid]<=arr[high]:
                minval = min(minval,arr[mid])
                high = mid-1
            else:
                minval = min(minval,arr[low])
                low = mid+1
        
        return minval