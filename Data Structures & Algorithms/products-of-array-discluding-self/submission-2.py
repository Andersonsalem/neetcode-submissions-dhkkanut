class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        n = len(nums)
        mult = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        suf = 1
        for i in range(n-2, -1, -1):
            suf *= nums[i+1]
            res[i] = suf * res[i] 
        
        return res