class Solution(object):
    def isPalindrome(self, x):
        
        y = str(x)

        return y == y[::-1]
        
