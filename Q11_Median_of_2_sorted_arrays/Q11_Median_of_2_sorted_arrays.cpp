class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int> nums3;
    
        int m = nums1.size(), n = nums2.size();
        
        nums3.reserve(m+n);
        
        int i=0,j=0,k=0;
        float median;
        
        while(i<m && j<n)
        {
            if(nums1[i]<=nums2[j])
                nums3[k++] = nums1[i++];
            else
                nums3[k++] = nums2[j++];
        }
        
        while(i<m)
            nums3[k++] = nums1[i++];
        
        while(j<n)
            nums3[k++] = nums2[j++];
            
        int m1 = ((m+n)/2);
        
        if((m+n)%2==0)
        {
            int m2 = m1-1;
            median = ((float)(nums3[m1] + nums3[m2]))/2.0;
        }
        else
            median = (float)(nums3[m1]);
        
        return median;
        
    }
};

/* OR

    std::vector<int> result;
    result.reserve(nums1.size() + nums2.size());
    
    std::merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), std::back_inserter(result));

    if(result.size() == 0) 
        return 0;

    return result.size() % 2 != 0 
            ? result[result.size() / 2]
            : (result[result.size() / 2 - 1] + result[result.size() / 2]) / 2.0;

*/