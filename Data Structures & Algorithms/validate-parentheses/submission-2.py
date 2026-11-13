class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        complements = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        vals = [")", "}", "]"]

        for i in s:
            if i not in vals:
                stack.append(i)
            else:
                if len(stack)<=0: return False
                if stack[-1] != complements[i] :
                    return False
                stack.pop()
        
        return True if len(stack)==0 else False
