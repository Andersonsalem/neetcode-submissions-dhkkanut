class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        remainder = {}

        for i in range(len(numbers)):
            curr = numbers[i]
            r = target - curr
            if curr in remainder.keys():
                return [remainder[curr]+1, i+1]
            else:
                remainder[r] = i