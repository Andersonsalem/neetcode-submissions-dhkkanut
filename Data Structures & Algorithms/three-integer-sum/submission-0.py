class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            elems_list = self.twosum(nums, i + 1, target)
            for elems in elems_list:
                results.append([nums[i]] + elems)
        return results

    def twosum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        left = start
        right = len(nums) - 1
        pairs = []
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                pairs.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return pairs