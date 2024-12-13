# Two - sum problem

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        new = num[::]
        if num == new:
            return True
        else:
            return False
        