class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s == "":
            return ""
        
        sub = s[0]
        
        for i in range(len(s)):
            
            j = i+1
            while s[i] in s[j:]:
                ind = s.find(s[i],j)
                temp = s[i:ind+1]
                j = ind+1
                if temp == temp[::-1] and (len(sub) < len(temp)):
                    sub = temp
                 
        return sub