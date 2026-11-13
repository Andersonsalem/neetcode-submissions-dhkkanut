class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = ["+", "-", "/", "*"]

        for i in tokens:

            if i in ops:
                y = stack.pop()
                x = stack.pop()

                if i == "+":
                    stack.append(x+y)
                elif i == "-":
                    stack.append(x-y)
                elif i == "*":
                    stack.append(x*y)
                else:
                    if y != 0 :
                        stack.append(int(x/y))
                    else:
                        stack.append(0)
            else:
                stack.append(int(i))
        
        return int(stack[-1])