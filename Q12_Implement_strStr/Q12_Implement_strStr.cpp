class Solution {
public:
    int strStr(string haystack, string needle) {
        
        if(needle == "")
            return 0;
        else if(haystack.length() < needle.length())
            return -1;
        
        int len = haystack.length()-needle.length()+1;
        
        for(int i=0; i< len; i++)
        {
            int j=0,k=i;
            while(j < needle.length())
            {
                if(haystack[k]!=needle[j]){
                    break;
                }
                else{
                    k++; j++;
                }
            }
            
            if(j==needle.length())
                return i;
                
        }
        
        return -1;
        
    }
};