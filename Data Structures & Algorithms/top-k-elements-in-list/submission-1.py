class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter

        counted = Counter(nums)

        counted = sorted(counted.items(), key=lambda x: x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(counted[i][0])
        
        return res