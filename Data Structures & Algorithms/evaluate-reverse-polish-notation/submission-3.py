class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens :
            if c == '+' or c == '-' or c== '*' or c== '/' and len(stack)>=2:
                b = stack.pop()
                a = stack.pop()
                if c == "+" : stack.append(a+b)
                if c == "-" : stack.append(a-b)
                if c == "*" : stack.append(a*b)
                if c == "/" : stack.append(int(a/b))
            else : stack.append(int(c))
        
        return stack.pop()
