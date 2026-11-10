class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = math.prod(nums)

        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] = total//nums[i]
            else:
                res[i] = int(math.prod(nums[0:i]) * math.prod(nums[i+1:]))
        return res