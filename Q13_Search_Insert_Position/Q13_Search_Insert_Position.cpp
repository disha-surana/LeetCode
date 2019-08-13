class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        int end=nums.size(),i;
        
        if(target <= nums[0])
            return 0;
        
        for(i=1;i<end;i++)
        {
            if(nums[i]>=target)
                return i;
        }
        return i;
        
    }
};