class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = {}
        for i in range(len(nums)):
            if nums[i] in remains.keys():
                return [remains[nums[i]], i] 
            remains[target - nums[i]] = i

            