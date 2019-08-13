class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substr = ''
        length = 0
        
        for i in range(len(s)):
            
            if s[i] not in substr:
                substr += s[i]
                length = max(length,len(substr))
                
            else:
                substr = substr[substr.index(s[i])+1:] + s[i]
                
        return length
                
            
        
'''

def longestSubstr(s):

    d = ""
    f = ""
    print(s)
    for i in range(len(s)):
        print(f,"\t",d)
        if s[i] not in f:
            f += s[i]
        else:
            if len(d) < len(f):
                d = f
            f = f[f.index(s[i])+1::] + s[i]
          
    return max(len(d), len(f))



print(longestSubstr("abcbbab"))


'''