class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1 : return False
        stack = []
        par = {')': '(', '}': '{', ']':'['}

        for c in s :

            if c in par :
                if len(stack)==0: return False
                if par[c] != stack[-1] : return False
                stack.pop()
            else : stack.append(c)

        if len(stack) >0  : return False
        return True