class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = "".join(char for char in s if char.isalnum())
        n = len(s_)
        left = 0
        right = n-1
        for i in range(n//2 ) :
            if s_[left].lower() != s_[right].lower() : return False
            left+=1
            right-=1
        
        return True