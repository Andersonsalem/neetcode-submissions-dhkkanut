class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        sum = target - 1

        while sum != target:
            sum = numbers[l] + numbers[r]

            if sum > target: r-=1
            if sum < target: l+=1
        return [l + 1, r + 1]