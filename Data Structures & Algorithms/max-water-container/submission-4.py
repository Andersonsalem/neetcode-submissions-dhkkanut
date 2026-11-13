class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        lval = heights[l]
        rval = heights[r]

        h = min(lval, rval)
        vol = h * (r - l)

        while l < r:
            if lval > rval:
                r -= 1
                rval = heights[r]
            else:
                l += 1
                lval = heights[l]

            h = min(lval, rval)
            vol = max(vol, h * (r - l))
            
            

        return vol