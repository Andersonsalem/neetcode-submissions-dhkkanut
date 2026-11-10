class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = {}
        for i in range(len(nums)):
            if nums[i] in remains.keys():
                return [remains[nums[i]], i]
            r = target - nums[i]
            remains[r] = i

            