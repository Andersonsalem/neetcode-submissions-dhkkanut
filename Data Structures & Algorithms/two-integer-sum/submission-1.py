class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rep ={}

        for i in range(len(nums)):
            
            complement = target - nums[i]

            if complement in rep.keys():
                return [rep[complement], i]

            rep[nums[i]] = i