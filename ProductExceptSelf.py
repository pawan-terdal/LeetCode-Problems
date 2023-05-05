class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        prefix = postfix = 1

        # build the prefix first

        for i in range(0,len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        # build the postfix now
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
      
'''
O(n) space complexity
O(n) size complexity
'''
