class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            compl = target-nums[i]
            if compl in nums[i+1:]:
                return [i,(nums[i+1:].index(compl) + 1 + i)]
                    
        