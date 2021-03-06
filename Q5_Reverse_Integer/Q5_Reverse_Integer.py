class Solution:
    def reverse(self, x: int) -> int:
        
        neg = False
        if x < 0 :
            neg = True
            x *= -1
            
        rev = 0
        
        while x > 0:
            rev = rev * 10 + (x%10)
            x //= 10
            
        if neg:
            rev *= -1 
            
        if (rev > 2**31 -1) or (rev < -1 *(2**31)):
            return 0
        
        return rev