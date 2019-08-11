class Solution:
    
    def dayOfYear(self, date: str) -> int:
            
            
        month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
                
            
        yy_mm_dd = date.split("-")
                
            
        yy = int(yy_mm_dd[0])
                
        mm = int(yy_mm_dd[1])
                
        dd = int(yy_mm_dd[2])
                
                
        days = dd
            
            
        for i in range(mm):
                    
                    
            days += month_days[i]
                        
                        
            if i==2 and ((yy%400 == 0) or (yy%100 != 0 and yy%4==0)):
                            
                days += 1
                    
                
        return days
                
            