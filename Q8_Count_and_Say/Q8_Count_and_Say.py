class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n<1:
            return "0"
    
        num = "1"   # Base Case n=1
         
        for i in range(n-1):
            j=0
            temp = ""   
            count = 1
            while(j < len(num)):
                
                if (j+1 < len(num)) and num[j] == num[j+1]: #couting consecutive occurences
                    count += 1
                else:
                    temp += str(count) + str(num[j])  # if not same consecutive number, store ocuurence_number
                    count = 1
                j += 1
            
            num =  temp
            
        return num
            
            
            
            