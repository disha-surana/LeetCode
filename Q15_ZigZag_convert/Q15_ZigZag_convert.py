class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        ar = [""] * numRows
        
        j = 0
        flag = True
        
        for i in range(len(s)): 
            
            ar[j] += s[i]
            
            if j == numRows-1:
                flag = -1
            elif  j==0:
                flag = 1
                
            j += flag
               
        st = ""
        
        for i in range(numRows):
            st += ar[i] 
            
            
        return st