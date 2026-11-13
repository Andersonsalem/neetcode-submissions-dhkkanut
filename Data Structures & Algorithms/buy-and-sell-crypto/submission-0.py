class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        curr_prof = 0

        for i in range(1, len(prices)):
            tent = prices[i] - lowest

            if prices[i] < lowest:
                lowest = prices[i]

            curr_prof = max(0, curr_prof, tent)
        return curr_prof